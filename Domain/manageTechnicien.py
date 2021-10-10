from Database.manageSqlLite import ManageSqlLite
from datetime import date

class ManageTechnicien:
    def __init__(self, databaseName):
        self.sql = ManageSqlLite(databaseName)
        self.aujourdhui = date.today().strftime("%d/%m/%Y")

    def modifierInformations(self, **kwargs):
        cmdUpdate = f"UPDATE Technicien SET "
        for key, value in kwargs.items():
            if key == "numeroEmploye":
                numeroClient = value
            else:
                cmdUpdate += f"{key} = '{value}', "
        cmdUpdate = cmdUpdate[:-2]
        cmdUpdate +=f" WHERE numeroEmploye = {numeroClient}"
        self.sql.executeSqlCommande(cmdUpdate)
        self.sql.commmit()


    def recupererInterventionsByTechnicien(self, numeroEmploye):
        cmdSelect= f"SELECT * from Intervention where numeroEmploye={numeroEmploye}"
        self.sql.executeSqlCommande(cmdSelect)
        dicorecuperer = {}
        for row in self.sql.sqlCursor:
            dicorecuperer.update({row[0]: {
                "dateIntervention": row[1],
                "Lieu": row[2],
                "numeroSerie": row[6],
            }})
        return dicorecuperer

    def recupererInterventionsByTechnicienAujourdui(self, numeroEmploye):
        cmdSelect= f"SELECT * from Intervention where numeroEmploye={numeroEmploye} AND dateIntervention = '{self.aujourdhui}'"
        self.sql.executeSqlCommande(cmdSelect)
        dicorecuperer = {}
        for row in self.sql.sqlCursor:
            dicorecuperer.update({row[0]: {
                "dateIntervention": row[1],
                "Lieu": row[2],
                "numeroSerie": row[6],
            }})
        return dicorecuperer


# tech1 =ManageTechnicien("../Database/EasySav.db")
# tech1.modifierInformations(numeroEmploye=10,nom="Nyffels")
# # # inter1= Intervention("24/04/2010","Marseille",'C001')
# # tech1.recupererInterventionsByTechnicien(4)
# # inter1.numeroIntervention = 1
# #
# # tech1.annulerIntervention(inter1)




