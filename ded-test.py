import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question

# import sys
# sys.path.insert(0, './lib/')
from lib.dir import Directions

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch

def new_session():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent("QueryIntent")

def get_route(origin, destination):
    print '='*88

    # origin = "walmart"
    # destination = "sunset park"

    print Directions
    print ". ".join([origin, destination])
    directions = Directions(origin, destination)
    print directions

    instructions = directions.instructions
    print ". ".join(instructions)

    directions_msg = render_template('route', directions = "Hello. Hello.")
    return statement(directions_msg)

if __name__ == '__main__':
    app.run(debug=True)
