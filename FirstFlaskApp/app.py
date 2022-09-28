# Flask looks for a file called "app.py"
# You can anme this file anything, but if it's not app.py, you have to set the name as an environment variable:
# FLASK_APP = [].py flask run
# You have to immediately state "flask run" otherwise on a next line it reverts to looking for app.py 

from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension


# request represents web requests
# if you want access to a query string, it happens with request.args

app = Flask(__name__)

app.config['SECRET_KEY'] = "SSS0122"
debug = DebugToolbarExtension(app)

# To switch enviroment variable, FLASK_ENV=development or =production, and again, flask rund immediately after.
# Without changing this varaible, env is automatically set to development and debugger is off.
# You can "set" this variable in the given virtual environment with:
# export FLASK_ENV=development; it appears you cannot do this with the file name command above.
# IF you *close* the ubuntu window or the venv, you have to reset this variable - it defaults to production.
# You can set this in the bash profile if you want it to be permanent. I tried this and it didn't work...

# Adding routes:
# (the mapping of urls)

# For Jinja, variables will have 2 sets of curly braces {{}} - whatever is in the 
# two sets of braces will evaluate as Python

# root (home page)
@app.route('/')
def home_page():
    # html = """
    # <html>
    #     <body>
    #         <h1>Dis da place!</h1>
    #         <a href='/yodawg'>Let 'em out!</a>
    #         <a href='/gtfoh'>Well, Bye!</a>
    #     </body>
    # </html>
    # """
    return render_template("hello.html")

@app.route('/form')
def show_from():
    return render_template("form.html")

@app.route('/form_2')
def show_from_2():
    return render_template("form_2.html")

COMPLIMENTS = [
    "great",
    "greater",
    "greatest",
    "humble",
    "clever",
    "outspoken",
    "softspoken",
    "who cares mate?"
]

@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing=choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)

@app.route('/greet_2')
def get_greeting_2():
    username = request.args["username"]
    wants = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)
    return render_template("greet_2.html", username=username, wants_compliments=wants, compliments=nice_things)

@app.route('/lucky')
def lucky_number():
    num = randint(1, 10)
    return render_template('lucky.html', lucky_num=num, msg="You are so lucky!")

@app.route('/spell/<word>')
def spell_word(word):
    return render_template('spell_word.html', word=word.upper())

@app.route('/hello')
def say_hello():
    """Shows hello page"""
    html = """
    <html>
        <body>
            <h1>YO DAWG!</h1>
            <a href='/'>Hizzouse!</a>
            <a href='/gtfoh'>Well, Bye!</a>
        </body>
    </html>
    """
    return html

@app.route('/gtfoh')
def gtfoh():
    html = """
    <html>
        <body>
            <h1>Hey man! #$W%& off!</h1>
            <a href='/'>Hizzouse!</a>
            <a href='/yodawg'>Let 'em out!</a>
        </body>
    </html>
    """
    return html

@app.route('/geiwo')
def didimao():
    # print(request.args) (this gets printed on the ubuntu venv ImmutableMultiDict object)
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Dis wut we got: {term}, showin' you in {sort} orduh"

# # to define a post route, we need to pass in argument methods=["POST"] 
# @app.route("/putit", methods=["POST"])
# def puts():
#     html = """
#     <html>
#         <body>
#             <h1>Yeah I KNOW you want it!</h1>
#             <a href='/'>Hizzouse!</a> 
#         </body>
#     </html>
#     """
#     return html

# # You can check post requests on a second Ubuntu window (one that is not running the flask app server) with:
# # curl -X POST http://127.0.0.1:5000/post

# @app.route("/putit", methods=["GET"])
# def gets():
#     html = """
#     <html>
#         <body>
#             <h1>Here't is!</h1>
#             <a href='/'>Hizzouse!</a> 
#         </body>
#     </html>
#     """
#     return html

# Generally speaking, you don't have to specify methods=["GET"] because that's the default 

@app.route('/add-comment')
def add_comment_form():
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type ='text' placeholder='comment' name='comment'/>
        <input type ='text' placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
"""
# the 'name' attribute represents how this data will be saved when it's sent to the server

@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form["username"]
    print(request.form)
    return f"""
    <h1>Saved {username}'s "{comment}" text!</h1>
    <ul>
    <li>Username: {username}</li>
    <li>Comment: {comment}</li>
    </ul>
    """

    # "args" and "form" will be used a lot

    # wrapping a variable in lt/gt brackets in the app.route path:
    # @app.route('/user/<username>')

@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>This is the '{subreddit}' subreddit!</h1>"

    # The lt/gt brackets pass that word as an argument to the view handler function.

POSTS = {
    1: "I like",
    2: "I don't like",
    3: "Whatever",
    4: "Pi"
}

# Notice the int: below - this turns the id into a number, whereas it would be a string and cause a key error otherwise: 
@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, "Wrong-o Moosebreath!")
    return f"<p>Words of wisdom: {post}</p>"

# It is not uncommon to have more than one variable in the url 

@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit, post_id):
    return f"<h1> Viewing comments for post with id: {post_id} from the {subreddit} Subreddit</h1>"

# Distinction between route variables and query strings: 
# URL Parameter is for subject of the page, Query Parameter is for additional information
