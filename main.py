# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "prueba de devops"

def sum(x, y):
    return x + y


def is_greater_than(number_1, number_2):
    return number_1 > number_2


def login(username, password):
    if ((username == "uskokrum2010") and (password == "123456")):
        return True
    else:
        return False

app.run(host="0.0.0.0")