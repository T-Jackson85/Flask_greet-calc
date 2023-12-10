# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def addition():
    """ Add Paremeters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)

@app.route("/sub")
def subtraction():
    """ Subtract Paremeters"""

    a = int(request.args.get('a'))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)

@app.route("/mult")
def multiplication():
    """ Multiply Parameters"""
    
    a = int(request.args.get('a'))
    b = int(request.args.get("b"))

    result = mult(a,b)

    return str(result)

@app.route("/div")
def division():
    """ Divide Parameters"""
    
    a = int(request.args.get('a'))
    b = int(request.args.get("b"))

    result = div(a,b)

    return str(result)

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("math/<oper>")
def operations(oper):
    """ Does all math on Parameters"""
    
    a = int(request.args.get('a'))
    b = int(request.args.get("b"))

    result = operators[oper](a,b)

    return str(result)


    







