import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch

def new_session():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent("QueryIntent")

def get_route():
    directions = " ".join(["First path", "Second path"])
    directions_msg = render_template('route', directions=directions)
    return statement(directions_msg)

if __name__ == '__main__':
    app.run(debug=True)
