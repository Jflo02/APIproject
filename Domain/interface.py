import requests
from Database.manageSqlLite import ManageSqlLite


class Interface:
    def __init__(self):
        self.utilisateur = None
        self.numeroEmploye = None
        self.tabUtilisateur = {"1": "technicien", "2": "operatrice"}
        self.choixTechnicien = {"1": "voirInterventionsJour", "2": "voirInterventions", "3": "faireCompteRendu"}
        self.choixOperatrice = {"1": "voirToutesInterventions", "2": "voirInterventionID",
                                "3": "modifierIntervention", "4": "supprimerIntervention"}
        self.choix = None
        self.sql = ManageSqlLite('Database/EasySav.db')
        print("Bienvenu dans Easy SAV !")

    def quiUtilise(self):
        while True:
            try:
                self.utilisateur = self.tabUtilisateur[
                    input("Tapez 1 si vous êtes un technicien, 2 si vous etes une operatrice\n")]
                if self.utilisateur == "technicien":
                    self.numeroEmploye = int(input("Veuillez entrer votre numero d'employe : \n"))
            except KeyError:
                print('Veuillez entrer une valeur correcte..')
            except ValueError:
                print('Veuillez entrer une valeur correcte..')
            else:
                break
        return self.utilisateur

    def faireChoix(self):
        if self.utilisateur == "technicien":
            while True:
                try:
                    self.choix = self.choixTechnicien[input("1. Voir vos interventions du jour\n"
                                                            "2. Voir toutes vos interventions\n"
                                                            "3. Faire le compte rendu d une intervention\n")]
                except KeyError:
                    print('Veuillez entrer une valeur correcte..')
                else:
                    break
            return self.choix
        elif self.utilisateur == "operatrice":
            while True:
                try:
                    self.choix = self.choixOperatrice[input("1. Voir toutes les interventions\n"
                                                            "2. Voir une intervention\n"
                                                            "3. Modifier une intervention\n"
                                                            "4. Supprimer une intervention\n")]
                except KeyError:
                    print('Veuillez entrer une valeur correcte..')
                else:
                    break
            return self.choix

    def lancerAction(self, action):
        if action == "voirInterventionsJour":
            return self.voirInterventionsJour()
        if action == "voirInterventions":
            return self.voirInterventions()
        if action == "voirToutesInterventions":
            return self.voirToutesInterventions()
        if action == 'voirInterventionID':
            return self.voirInterventionID()

    #Methode Generique de formatage de réponse intervention
    def formatIntervention(self, url):
        reponse = requests.get(url)
        reponseDict = reponse.json()
        strFormatee = "\n"
        for numIntervention in reponseDict:
            strFormatee += f"L'intervention numero {numIntervention} :\n"
            for key in reponseDict[numIntervention]:
                if key == "numeroSerie":
                    sqlCommande = f"Select type From TypeProduit " \
                                  f"inner join Produit on TypeProduit.codeBarre = Produit.codeBarre " \
                                  f"WHERE Produit.numeroSerie = '{reponseDict[numIntervention][key]}'"
                    self.sql.executeSqlCommande(sqlCommande)
                    for row in self.sql.sqlCursor:
                        strFormatee += f"    Produit concerné : {row[0]}\n"
                if key == "numeroEmploye":
                    sqlCommande = f"Select nom, prenom From Technicien WHERE numeroEmploye = {reponseDict[numIntervention][key]} "
                    self.sql.executeSqlCommande(sqlCommande)
                    for row in self.sql.sqlCursor:
                        strFormatee += f"    Technicien en charge : {row[0]} {row[1]}\n"
                strFormatee += f"    {key} : {reponseDict[numIntervention][key]}\n"
        print(strFormatee)
        return True

    #Methode Technicien
    def voirInterventionsJour(self):
        url = f'http://127.0.0.1:5000/technicienajd/{self.numeroEmploye}'
        return self.formatIntervention(url)

    def voirInterventions(self):
        url = f'http://127.0.0.1:5000/technicien/{self.numeroEmploye}'
        return self.formatIntervention(url)

    #Methode Operatrice
    def voirToutesInterventions(self):
        url = 'http://127.0.0.1:5000/interventions'
        return self.formatIntervention(url)

    def voirInterventionID(self):
        idIntervention = input("Quelle intervention souhaitez-vous voir ?\n")
        url = f'http://127.0.0.1:5000/interventions/{idIntervention}'
        return self.formatIntervention(url)

    def fin(self):
        fin = input("Taper q pour quitter ou autre chose pour continuer\n")
        if fin == "q":
            print("Byyyye")
            return True
        else:
            return False
