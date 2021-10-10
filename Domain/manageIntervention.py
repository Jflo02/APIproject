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

    def interventionModifierPatch(self, dict):
        cmdUpdate = f"UPDATE Intervention SET "
        for key, value in dict.items():
            if key == "numeroIntervention":
                numeroIntervention = value
            else:
                cmdUpdate += f"{key} = '{value}', "
        cmdUpdate = cmdUpdate[:-2]
        cmdUpdate += f" WHERE numeroIntervention = {numeroIntervention}"
        print(cmdUpdate)
        self.sql.executeSqlCommande(cmdUpdate)
        self.sql.commmit()

    def recupererInterventions(self):
        cmdSelect = f"SELECT * FROM Intervention INNER JOIN Produit on Intervention.numeroSerie = Produit.numeroSerie INNER JOIN TypeProduit TP on TP.codeBarre = Produit.codeBarre INNER JOIN Technicien T on T.numeroEmploye = Intervention.numeroEmploye"
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
                "type": row[13],
                "numeroEmploye": row[7],
                "nomEmploye": row[15],
                "prenomEmploye": row[16]
            }})
        print(listInterventions)
        return listInterventions

    def interventionRecupererById(self, numeroIntervention):
        cmdSelect = f"SELECT * FROM Intervention INNER JOIN Produit on Intervention.numeroSerie = Produit.numeroSerie INNER JOIN TypeProduit TP on TP.codeBarre = Produit.codeBarre INNER JOIN Technicien T on T.numeroEmploye = Intervention.numeroEmploye where numeroIntervention = {numeroIntervention}"
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
                "type": row[13],
                "numeroEmploye": row[7],
                "nomEmploye": row[15],
                "prenomEmploye": row[16]
            }})
        return listInterventions

objet = ManageIntervention("../Database/EasySav.db")
objet.recupererInterventions()
