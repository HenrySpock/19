from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__) #python looks for this to know it is the main app file
app.config['SECRET_KEY'] = "so-secret"
debug = DebugToolbarExtension(app)

@app.route('/welcome')
def welcome():
    return "Welcome!"

@app.route('/welcome/home')
def welcome_home():
    return "Welcome home!"

@app.route('/welcome/back')
def welcome_back():
    return "Welcome back!"