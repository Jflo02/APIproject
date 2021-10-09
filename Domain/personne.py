import abc
from abc import ABC


class Personne(ABC):
    @abc.abstractmethod
    def modifierInformations(self, ):
        pass
