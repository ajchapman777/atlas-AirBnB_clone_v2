#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask
<<<<<<< HEAD
=======


>>>>>>> 9d62034d0a23e99b6ee95796f6b8b267ca591a39
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
<<<<<<< HEAD
""" Prints a Message when / is called """
return 'Hello HBNB!'


if __name__ == "__main__":
""" Main Function """
app.run(host='0.0.0.0', port=5000)
=======
    """ Prints a Message when / is called """
    return 'Hello HBNB!'


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
>>>>>>> 9d62034d0a23e99b6ee95796f6b8b267ca591a39
