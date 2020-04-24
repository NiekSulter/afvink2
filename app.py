from flask import Flask, request, render_template
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def convert():
    if request.method == 'POST':
        x = request.form['text']
        x = ''.join(x.split())
        output = Seq(x, generic_dna)
        output = output.translate()
        return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)

