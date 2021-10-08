from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Bienvenue sur Easy Sav"


@app.route('/helloWorld')
def helloworld():
    return "Hello world Easy Sav"


@app.route('/getAllInterventions')
def getAllInterventions():
    return True


if __name__ == '__main__':
    app.run()
