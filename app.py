from flask import Flask, render_template
from random import randint

def incrfun(x):
    return x + 1

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page Here!"

@app.route("/hello")
def hello():
    return "Hello World Page Here!"

@app.route("/hello/<string:name>/")
def sayhello(name):
    quotes = [ "'Look at the sky. We are not alone. The whole universe is friendly to us and conspires only to give the best to those who dream and work.' -- Dr A P J Abdul Kalam ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'An investment in knowledge pays the best interest.' -- Benjamin Franklin",
        "'The best preparation for tomorrow is doing your best today.' -- H. Jackson Brown, Jr.",
        "'Good, better, best. Never let it rest. 'Til your good is better and your better is best.' -- St. Jerome",
        "'The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.' -- Helen Keller"  ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]

    # For passing single variable
    # return render_template('test.html',name=name)
    # For passing multiple variables
    return render_template('test.html',**locals())

@app.route("/members")
def members():
    return "Members Page Here"

@app.route("/members/<string:name>/")
def getMember(name):
    prefix = 'Member with name: '
    return (prefix + name)
    # return name

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
