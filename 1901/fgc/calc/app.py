from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

#Version 1:
# @app.route('/add')
# def addition():
#     """Add a and b."""
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     answer = add(a, b)
#     return str(answer)

# @app.route('/sub')
# def subtraction():
#     """Add a and b."""
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     answer = sub(a, b)
#     return str(answer)

# @app.route('/mult')
# def multiply():
#     """Add a and b."""
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     answer = mult(a, b)
#     return str(answer)

# @app.route('/div')
# def divide():
#     """Add a and b."""
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     answer = div(a, b)
#     return str(answer)
 
#Version 2:
action = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
    }

@app.route('/math/<opera>')
def operation(opera):
    """Perform math operation utilizing a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = action[opera](a, b)
    return str(answer)

 