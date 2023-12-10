from flask import Flask

app = Flask(__name__)

@app.route('/welcome')

def say_welcome():
    return "Welcome!"

@app.route('/welcome/<home>')

def home_greeting(home):
    return "Welcome Home!"

@app.route('/welcome/<back>')

def wel_back(back):
    return "Welcome Back"
