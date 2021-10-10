from Domain.personne import Personne


class Technicien(Personne):
    def __init__(self, nom, prenom, numeroTelephone, numeroEmploye):
        super.__init__()
        self.nom = nom
        self.prenom = prenom
        self.numeroTelephone= numeroTelephone
        self.numeroEmploye = numeroEmploye
        self.interventions = {}







