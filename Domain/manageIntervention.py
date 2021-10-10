from Database.manageSqlLite import ManageSqlLite


class ManageIntervention:
    def __init__(self, databaseName):
        self.sql = ManageSqlLite(databaseName)

    def interventionAjouter(self, dateIntervention, lieu, numeroSerie, numeroEmploye):
        cmdInsert = f"INSERT INTO Intervention(dateIntervention, lieu, numeroSerie, numeroEmploye)" \
                    f"VALUES ('{dateIntervention}', '{lieu}', '{numeroSerie}', {numeroEmploye})"
        self.sql.executeSqlCommande(cmdInsert)
        self.sql.commmit()

    def interventionSupprimer(self, numeroIntervention):
        cmdDelete = f"DELETE FROM Intervention where numeroIntervention={numeroIntervention}"
        self.sql.executeSqlCommande(cmdDelete)
        self.sql.commmit()


    def interventionModifier(self, **kwargs):
        pass

    def assignerIntervention(self, Intervention):
        pass

    def recupererInterventions(self):
        cmdSelect = f"SELECT * FROM Intervention"
        self.sql.executeSqlCommande(cmdSelect)
        listInterventions = {}
        for row in self.sql.sqlCursor:
            listInterventions.update({row[0]: {
                "dateIntervention": row[1],
                "lieu": row[2],
                "compteRendu": row[3],
                "reussiteIntervention": row[4],
                "tempsIntervention": row[5],
                "numeroSerie": row[6],
                "numeroEmploye": row[7]
            }})
        return listInterventions

    def interventionRecupererById(self, numeroIntervention):
        cmdSelect = f"SELECT * FROM Intervention where numeroIntervention = {numeroIntervention}"
        self.sql.executeSqlCommande(cmdSelect)
        listInterventions = {}
        for row in self.sql.sqlCursor:
            listInterventions.update({row[0]: {
                "dateIntervention": row[1],
                "lieu": row[2],
                "compteRendu": row[3],
                "reussiteIntervention": row[4],
                "tempsIntervention": row[5],
                "numeroSerie": row[6],
                "numeroEmploye": row[7]
            }})
        return listInterventions

#
# objet = ManageIntervention("../Database/EasySav.db")
# objet.interventionAjouter("25/05/2022", "Saint-André-Lez-Lille", "AZERTY1234", 1)
