import json

from flask import Flask
from flask import jsonify
from flask import request

from Domain.manageIntervention import ManageIntervention
from Domain.manageTechnicien import ManageTechnicien

manageTechnicien = ManageTechnicien("Database/EasySav.db")
manageIntervention = ManageIntervention("Database/EasySav.db")

app = Flask(__name__)


@app.route('/interventions', methods=['POST', 'GET'])
def getAllInterventions():
    if request.method == 'GET':
        dictInterventions = manageIntervention.recupererInterventions()
        # jsonInterventions = json.dumps(dictInterventions)
        return jsonify(dictInterventions)
    elif request.method == 'POST':
        jsonToDict = request.get_json()
        print(jsonToDict)
        manageIntervention.interventionAjouter(jsonToDict["dateIntervention"], jsonToDict["lieu"], jsonToDict["numeroSerie"], jsonToDict["numeroEmploye"])
        return jsonToDict


@app.route('/interventions/<id>')
def getInterventtionById(id):
    dictInterventions = manageIntervention.interventionRecupererById(id)
    # jsonInterventions = json.dumps(dictInterventions)
    return jsonify(dictInterventions)


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
