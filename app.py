from flask import Flask, request, render_template
import biopython

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def convert():
    if request.method == 'POST':
        output = request.form['text']
        return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
