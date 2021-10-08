from technicien import Technicien
from Database.manageSqlLite import ManageSqlLite

class ManageTechnicien:
    def __init__(self, databaseName):
        self.sql = ManageSqlLite(databaseName)

    def modifierInformations(self, **kwargs):
        pass

    def assignerIntervention(self, Intervention):
        pass

    def annulerIntervention(self, Intervention):
        pass

    def recupererInterventions(self, numeroEmploye):
        cmdSelect= f"SELECT * from Intervention where numeroEmploye="
        self.sql.executeSqlCommande(cmdSelect)
        for row in self.sql.sqlCursor:
            return print(row)


tech1 =ManageTechnicien("../Database/EasySav.db")
tech1.recupererInterventions()





