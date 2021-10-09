import json

from flask import Flask

from Domain.manageIntervention import ManageIntervention
from Domain.manageTechnicien import ManageTechnicien

manageTechnicien = ManageTechnicien("Database/EasySav.db")
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

@app.route('/technicien/<idtech>')
def getInterventionByTechnicien(idtech):
    dictInterventions = manageTechnicien.recupererInterventionsByTechnicien(idtech)
    jsonIntervention = json.dumps(dictInterventions)
    return jsonIntervention

@app.route('/technicienajd/<idtech>')
def getInterventionByTechnicienAujourdhui(idtech):
    dictInterventions = manageTechnicien.recupererInterventionsByTechnicienAujourdui(idtech)
    jsonIntervention = json.dumps(dictInterventions)
    return jsonIntervention

@app.route('/cancelIntervention/<idIntervention>')
def getInterventionForCancel(idIntervention):
    manageTechnicien.annulerIntervention(idIntervention)
    return f"cancel ok"


if __name__ == '__main__':
    app.run()
