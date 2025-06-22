from datetime import datetime

class Etape:
    def __init__(self, id = 0, nom = "Inconnu", date_de_debut = datetime(1, 11, 14)):
        self.__id = id
        self.__nom = nom
        self.__date_de_debut = date_de_debut

    @property
    def id(self):
        return self.__id

    @property
    def nom(self):
        return self.__nom

    @property
    def date_de_naissance(self):
        return self.__date_de_debut