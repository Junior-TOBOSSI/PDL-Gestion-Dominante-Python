from datetime import datetime

from model.Filiere import Filiere
from model.Dominante import Dominante
from model.Promotion import Promotion


class Etudiant:
    
    def __init__(self, id = 0, nom = "Inconnu", prenom = "Inconnu", classement = 0, mot_de_passe = "Inconnu", filiere = Filiere(), promotion = 0, date_de_naissance = datetime(1, 11, 14), dominante_finale = Dominante()):
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__classement = classement
        self.__mot_de_passe = mot_de_passe
        self.__filiere = filiere
        self.__promotion = promotion
        self.__date_de_naissance = date_de_naissance
        self.__dominante_finale = dominante_finale

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
    def classement(self):
        return self.__classement
    
    @property
    def mot_de_passe(self):
        return self.__mot_de_passe
    
    @property
    def filiere(self):
        return self.__filiere
    
    @property
    def promotion(self):
        return self.__promotion
    
    @property
    def date_de_naissance(self):
        return self.__date_de_naissance
    
    @property
    def dominante_finale(self):
        return self.__dominante_finale
    
    @nom.setter
    def setNom(self, nom):
        if isinstance(nom, str):
            self.__nom = nom
        else :
            print("Le nom est une chaine de caractere !")
    
    @prenom.setter
    def setPrenom(self, prenom):
        if isinstance(prenom, str):
            self.__prenom = prenom
        else :
            print("Le prenom est une chaine de caractere !")

    @classement.setter
    def setClassement(self, classement):
        if isinstance(classement, int):
            self.__classement = classement
        else:
            print("Le classement doit être un entier")

    @filiere.setter
    def setFiliere(self, filiere):
        if isinstance(filiere, Filiere):
            self.__filiere = filiere
        else:
            print("La filiere est de type Filiere")


    @dominante_finale.setter
    def setDominante_finale(self, dominante_finale):
        if isinstance(dominante_finale, Dominante):
            self.__dominante_finale = dominante_finale
        else :
            print("La dominante finale est de type Dominante")

    @date_de_naissance.setter
    def setDate_de_naissance(self, date_de_naissance : datetime):
        self.__date_de_naissance = date_de_naissance