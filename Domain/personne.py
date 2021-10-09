import abc
from abc import ABC


class Personne(ABC):
    def __init__(self, nom, prenom, numeroTelephone):
        self.nom = nom
        self.prenom = prenom
        self.numeroTelephone = numeroTelephone
        self.idPersonne = None

    @abc.abstractmethod
    def modifierInformations(self, ):
        pass
