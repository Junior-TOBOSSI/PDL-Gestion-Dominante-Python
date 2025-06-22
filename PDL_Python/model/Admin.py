class Admin:

    def __init__(self, id = 0, nom = "Nom admin", prenom = "prenom admin", mot_de_passe = "Inconnu"):
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__mot_de_passe = mot_de_passe

    @property
    def id(self):
        return self.__id

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def mot_de_passe(self):
        return self.__mot_de_passe

    @mot_de_passe.setter
    def mot_de_passe(self, nouveau_mdp):
        self.__mot_de_passe = nouveau_mdp