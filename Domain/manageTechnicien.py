from datetime import date

from Database.manageSqlLite import ManageSqlLite


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
        cmdUpdate += f" WHERE numeroEmploye = {numeroClient}"
        self.sql.executeSqlCommande(cmdUpdate)
        self.sql.commmit()

    def recupererInterventionsByTechnicien(self, numeroEmploye):
        cmdSelect = f"SELECT * FROM Technicien INNER JOIN Intervention I on Technicien.numeroEmploye = I.numeroEmploye INNER JOIN Produit P on P.numeroSerie = I.numeroSerie INNER JOIN TypeProduit TP on TP.codeBarre = P.codeBarre where Technicien.numeroEmploye={numeroEmploye}"
        self.sql.executeSqlCommande(cmdSelect)
        dicorecuperer = {}
        for row in self.sql.sqlCursor:
            print(row)
            dicorecuperer.update({row[4]: {
                "dateIntervention": row[5],
                "lieu": row[6],
                "compteRendu": row[7],
                "reussiteIntervention": row[8],
                "tempsIntervention": row[9],
                "numeroSerie": row[10],
                "type": row[15],
                "numeroEmploye": row[8],
                "nomEmploye": row[1],
                "prenomEmploye": row[2]
            }})
        print(dicorecuperer)
        return dicorecuperer

    def recupererInterventionsByTechnicienAujourdui(self, numeroEmploye):
        cmdSelect = f"SELECT * FROM Technicien INNER JOIN Intervention I on Technicien.numeroEmploye = I.numeroEmploye INNER JOIN Produit P on P.numeroSerie = I.numeroSerie INNER JOIN TypeProduit TP on TP.codeBarre = P.codeBarre where Technicien.numeroEmploye={numeroEmploye}"
        self.sql.executeSqlCommande(cmdSelect)

        dicorecuperer = {}
        for row in self.sql.sqlCursor:
            dicorecuperer.update({row[0]: {
                "dateIntervention": row[5],
                "lieu": row[6],
                "compteRendu": row[7],
                "reussiteIntervention": row[8],
                "tempsIntervention": row[9],
                "numeroSerie": row[10],
                "type": row[15],
                "numeroEmploye": row[8],
                "nomEmploye": row[1],
                "prenomEmploye": row[2]
            }})
        return dicorecuperer

# tech1 =ManageTechnicien("../Database/EasySav.db")
# # tech1.modifierInformations(numeroEmploye=10,nom="Nyffels")
# # # # inter1= Intervention("24/04/2010","Marseille",'C001')
# tech1.recupererInterventionsByTechnicien(2)
# # # inter1.numeroIntervention = 1
# # #
# # # tech1.annulerIntervention(inter1)
