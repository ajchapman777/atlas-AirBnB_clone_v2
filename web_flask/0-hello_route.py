#!.usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask
app = Flask(__name_)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'

if _name_=="_main_":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
