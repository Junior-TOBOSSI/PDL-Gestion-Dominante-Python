class Dominante:
    
    def __init__(self, id = 0, nom_long = "Inconnu", sigle = "Inconnu", place_max = 0, place_max_apprentis = 0):
        self.__id = id
        self.__nom_long = nom_long
        self.__sigle = sigle
        self.__place_max = place_max
        self.__place_max_apprentis = place_max_apprentis

    @property
    def id(self):
        return self.__id
    
    @property
    def nom_long(self):
        return self.__nom_long
    
    @property
    def sigle(self):
        return self.__sigle
    
    @property
    def place_max(self):
        return self.__place_max
    
    @property
    def place_max_apprentis(self):
        return self.__place_max_apprentis