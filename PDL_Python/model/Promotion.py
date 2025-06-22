
class Promotion:
    
    def __init__(self, id = 0, statut = 0):
        self.__id = id
        self.__statut = statut

    @property
    def id(self):
        return self.__id