from flask import Flask
from Domain.manageIntervention import ManageIntervention

manageIntervention = ManageIntervention("Database/EasySav.db")

app = Flask(__name__)


@app.route('/')
def hello():
    return "Bienvenue sur Easy Sav"


@app.route('/helloWorld')
def helloworld():
    return "Hello world Easy Sav"


@app.route('/getAllInterventions')
def getAllInterventions():
    listInterventions = manageIntervention.recupererInterventions()
    for intervention in listInterventions:
        print(intervention.lieu)
    return "yop"


if __name__ == '__main__':
    app.run()
