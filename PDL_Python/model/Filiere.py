class Filiere:
    
    def __init__(self, id = 0, nom = "Inconnu", nombre_choix = 0):
        self.__id = id
        self.__nom = nom
        self.__nombre_choix = nombre_choix

    @property
    def nom(self):
        return self.__nom

    @property
    def id(self):
        return self.__id

    @property
    def nombre_choix(self):
        return self.__nombre_choix