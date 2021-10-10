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
        cmdSelect= f"SELECT * FROM Intervention INNER JOIN Produit on Intervention.numeroSerie = Produit.numeroSerie INNER JOIN TypeProduit TP on TP.codeBarre = Produit.codeBarre INNER JOIN Technicien T on T.numeroEmploye = Intervention.numeroEmploye where Technicien.numeroEmploye={numeroEmploye}"
        self.sql.executeSqlCommande(cmdSelect)
        dicorecuperer = {}
        for row in self.sql.sqlCursor:
            dicorecuperer.update({row[0]: {
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
        print(dicorecuperer)
        return dicorecuperer

    def recupererInterventionsByTechnicienAujourdui(self, numeroEmploye):
        cmdSelect= f"SELECT * FROM Intervention INNER JOIN Produit on Intervention.numeroSerie = Produit.numeroSerie INNER JOIN TypeProduit TP on TP.codeBarre = Produit.codeBarre INNER JOIN Technicien T on T.numeroEmploye = Intervention.numeroEmploye where Technicien.numeroEmploye={numeroEmploye}"
        self.sql.executeSqlCommande(cmdSelect)
        dicorecuperer = {}
        for row in self.sql.sqlCursor:
            dicorecuperer.update({row[0]: {
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
        return dicorecuperer


tech1 =ManageTechnicien("../Database/EasySav.db")
# tech1.modifierInformations(numeroEmploye=10,nom="Nyffels")
# # # inter1= Intervention("24/04/2010","Marseille",'C001')
tech1.recupererInterventionsByTechnicien(3)
# # inter1.numeroIntervention = 1
# #
# # tech1.annulerIntervention(inter1)




