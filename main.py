from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Page d\'accueil</h1>'

@app.route('/contact')
def contact():
    return '<h1>Page de contact</h1>'

if __name__ == "__main__":
    app.run(debug=True)