import json

from flask import Flask

from Domain.manageIntervention import ManageIntervention

manageIntervention = ManageIntervention("Database/EasySav.db")

app = Flask(__name__)


@app.route('/interventions')
def getAllInterventions():
    dictInterventions = manageIntervention.recupererInterventions()
    jsonInterventions = json.dumps(dictInterventions)
    return jsonInterventions


@app.route('/interventions/<id>')
def getInterventtionById(id):
    dictInterventions = manageIntervention.interventionRecupererById(id)
    jsonInterventions = json.dumps(dictInterventions)
    return jsonInterventions


if __name__ == '__main__':
    app.run()
