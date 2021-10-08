from Domain.personne import Personne


class Technicien(Personne):
    def __init__(self, nom, prenom, numeroTelephone, numeroEmploye):
        super.__init__(nom, prenom, numeroTelephone)
        self.numeroEmploye = numeroEmploye
        self.interventions = {}

    def modifierInformations(self, **kwargs):
        pass

    def assignerIntervention(self, Intervention):
        pass

    def annulerIntervention(self, Intervention):
        pass

    def recupererInterventions(self, ):
        pass
