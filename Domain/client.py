from Domain.personne import Personne


class Client(Personne):
    def __init__(self, nom, prenom, numeroTelephone, adresse, numeroClient):
        super.__init__(nom, prenom, numeroTelephone)
        self.adresse = adresse
        self.numeroClient = numeroClient

    def modifierInformations(self, **kwargs):
        pass
