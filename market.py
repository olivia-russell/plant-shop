from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Larger Hello World!!</h1>'

@app.route('/about')
def about_page():
    return '<h1>About Page</h1>'