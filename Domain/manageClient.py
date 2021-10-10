from Database.manageSqlLite import ManageSqlLite


class ManageClient:
    def __init__(self, databaseName):
        self.sql = ManageSqlLite(databaseName)


    def modifierInformations(self, **kwargs):
        cmdUpdate = f"UPDATE Client SET "
        for key, value in kwargs.items():
            if key == "numeroClient":
                numeroClient = value
            else:
                cmdUpdate += f"{key} = '{value}', "
        cmdUpdate = cmdUpdate[:-2]
        cmdUpdate +=f" WHERE numeroClient = {numeroClient}"
        self.sql.executeSqlCommande(cmdUpdate)
        self.sql.commmit()

#
# client1=ManageClient("../Database/EasySav.db")
# client1.modifierInformations(numeroClient=2, nom="Petit")