from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    html = """ <h1>Dis da PLACE</h1> """
    return html

# Hello v1
# @app.route('/hello')
# def hello():
#     return "Hello"

# Hello v2
@app.route('/hello')
def hello():
    html = """ <h1>HELLO</h1> """
    return html

# Goodbye v1
# @app.route('/goodbye')
# def goodbye():
#     return "Goodbye"

# # Goodbye v2
@app.route('/goodbye')
def goodbye():
    html = """ <h1>GOODBYE</h1> """
    return html

@app.route('/search')
def search():
    term = request.args["term"]
    return f"<h1>SEARCH PAGE</h1> <p>Search results for: {term}<p>"