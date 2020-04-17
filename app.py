from flask import Flask, request, render_template
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


app = Flask(__name__)


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
