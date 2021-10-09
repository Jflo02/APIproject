class Interface:
    def __init__(self):
        self.utilisateur = None
        self.tabUtilisateur = {"1": "technicien", "2": "operatrice"}
        self.choixTechnicien = {"1": "voirIntervention", "2": "faireCompteRendu"}
        self.choixOperatrice = {"1": "voirIntervention", "2": "modifierIntervention",
                                "3": "supprimerIntervention"}
        self.choix = None
        print("Bienvenu dans Easy SAV !")

    def quiUtilise(self):
        while True:
            try:
                self.utilisateur = self.tabUtilisateur[
                    input("Tapez 1 si vous êtes un technicien, 2 si vous etes une operatrice\n")]
            except KeyError:
                print('Veuillez entrer une valeur correcte..')
            else:
                break
        return self.utilisateur

    def faireChoix(self):
        if self.utilisateur == "technicien":
            while True:
                try:
                    self.choix = self.choixTechnicien[input("1. Voir vos interventions du jour\n"
                                                            "2. Faire le compte rendu d une intervention\n")]
                except KeyError:
                    print('Veuillez entrer une valeur correcte..')
                else:
                    break
            return self.choix
        elif self.utilisateur == "operatrice":
            while True:
                try:
                    self.choix = self.choixOperatrice[input("1. Voir toutes les interventions\n"
                                                            "2. Modifier une intervention\n"
                                                            "3. Supprimer une intervention\n")]
                except KeyError:
                    print('Veuillez entrer une valeur correcte..')
                else:
                    break
            return self.choix

    def fin(self):
        fin = input("Taper q pour quitter ou autre chose pour continuer\n")
        if fin == "q":
            print("Byyyye")
            return True
        else:
            return False
