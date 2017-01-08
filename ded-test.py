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

    region = ", las vegas"

    print Directions
    print ". ".join([origin + region, destination + region])
    directions = Directions(origin + region, destination + region)
    print directions

    instructions = directions.instructions

    # Remove excess instruction: "Walk to [region]"
    instructions = instructions[:len(instructions) - 1]

    print ". ".join(instructions)

    directions_msg = render_template('route', directions = ". ".join(instructions))
    return statement(directions_msg)

if __name__ == '__main__':
    app.run(debug=True)
