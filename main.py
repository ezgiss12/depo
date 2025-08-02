import os
from flask import Flask, render_template

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/devam')
def devam():
    return render_template('devam.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(host='0.0.0.0', port=port, debug=True)
