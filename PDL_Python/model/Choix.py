from model import Dominante
from model.Etudiant import Etudiant


class Choix:

    def __init__(self, ids : list[int], etudiant : Etudiant, dominantes : list[Dominante]):
        self.__ids = ids
        self.__etudiant = etudiant
        self.__dominantes = dominantes

    @property
    def ids(self):
        return self.__ids

    @property
    def etudiant(self):
        return self.__etudiant

    @property
    def dominantes(self):
        return self.dominantes