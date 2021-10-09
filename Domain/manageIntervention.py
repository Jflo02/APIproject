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
        listInterventions = []
        for row in self.sql.sqlCursor:
            listInterventions.append(Intervention(row[1], row[2], row[6]))
        self.sql.closeConnection()
        return (listInterventions)

    def interventionRecupererById(self, numeroIntervention):
        cmd_select = f"SELECT * FROM Intervention where numeroIntervention = {numeroIntervention}"
        self.sql.executeSqlCommande(cmd_select)
        for row in self.sql.sqlCursor:
            var = Intervention(row[1], row[2], row[6])
        self.sql.closeConnection()
        return var
