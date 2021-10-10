from Domain.personne import Personne


class Client(Personne):
    def __init__(self, nom, prenom, numeroTelephone, adresse, numeroClient):
        super.__init__()
        self.nom = nom
        self.prenom = prenom
        self.numeroTelephone = numeroTelephone
        self.adresse = adresse
        self.numeroClient = numeroClient




