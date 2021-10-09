from Database.manageSqlLite import ManageSqlLite
from Domain.intervention import Intervention


class ManageIntervention:
    def __init__(self, databaseName):
        self.sql = ManageSqlLite(databaseName)

    def interventionAjouter(self, dateIntervention, lieu, compteRendu, reussiteIntervention, tempsIntervention,
                            numeroSerie, numeroEmploye):
        pass

    def interventionSupprimer(self, numeroIntervention):
        pass

    def interventionModifier(self, **kwargs):
        pass

    def assignerIntervention(self, Intervention):
        pass

    def annulerIntervention(self, Intervention):
        pass

    def recupererInterventions(self):
        cmd_select = f"SELECT * FROM Intervention"
        self.sql.executeSqlCommande(cmd_select)
        listInterventions = {}
        for row in self.sql.sqlCursor:
            listInterventions.update({row[0]: {
                "dateIntervention": row[1],
                "Lieu": row[2],
                "numeroSerie": row[6],
                "numeroEmploye": row[7]
            }})
        return listInterventions

    def interventionRecupererById(self, numeroIntervention):
        cmd_select = f"SELECT * FROM Intervention where numeroIntervention = {numeroIntervention}"
        self.sql.executeSqlCommande(cmd_select)
        listInterventions = {}
        for row in self.sql.sqlCursor:
            listInterventions.update({row[0]: {
                "dateIntervention": row[1],
                "Lieu": row[2],
                "numeroSerie": row[6],
                "numeroEmploye": row[7]
            }})
        return listInterventions
#
# objet = ManageIntervention("../Database/EasySav.db")
# objet.recupererInterventions()
