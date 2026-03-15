from flask import Flask

"""
It create an instance of the Flask Class,
Which will be your WSGI (web Server Gateway Interface) application.
"""
# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Learn Flask. This should be an important things."

@app.route("/index")
def index():
    return "Welcome to Index Page."

if __name__ == "__main__":
    app.run(debug=True)

