import oracledb
from oracledb import Error

from dao import EtudiantDao, ChoixDao
from dao.ConnectionDao import ConnectionDao
from model.Etape import Etape
from datetime import datetime

class TraitementDao(ConnectionDao):

    def __init__(self):
        super().__init__()

    """
        :return la liste de toutes les étapes dans la base de données
    """
    def getAllEtapes(self):

        list_etapes = []
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user=self._username,
                password=self._password,
                dsn=self._dsn
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ETAPE ORDER BY IDETAPE ASC")
            for row in cursor.fetchall():
                colonnes = [col[0] for col in cursor.description]
                row_dict = dict(zip(colonnes, row))
                mon_etape= Etape( id  = row_dict["IDETAPE"], nom = row_dict["NOMETAPE"], date_de_debut = row_dict["DATEDEDEBUT"])
                list_etapes.append(mon_etape)
        except oracledb.Error as e:
            print("Erreur", e)
        finally:
            if connection in locals():
                connection.close()
            if cursor in locals():
                cursor.close()
        return list_etapes

    """
        :return 1 si la date d'un étape à pu être validé 
        sinon 0
    """
    def update(self, dateStr : str, id : int):
        returnValue = 0
        connection = None
        cursor = None
        try :
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            date = datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S")
            requete = f"UPDATE ETAPE SET DATEDEBUT = :1 WHERE IDETAPE = : 2"
            parametres = (date, id)
            cursor.execute(requete, parametres)
            connection.commit()
        except Error as error:
            print(f"Une erreur est survenu lors de la modification de table Etape, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()

    """
        Cette méthode lance l'étape de traitement des étudiants
        On itère à travers tous les étudiants. Pour chaque étudiant on récupère ses choix.
        On itère à travers les choix de l'étudiant. Si une dominante choisi est libre on insère l'étudiant.
        Sinon on passe à son choix suivant 
    """
    def lancerTraitement(self, id_filiere):
        # on commence par récupérer tous les apprenants correspond à la filiere
        liste_etudiant = EtudiantDao().get_all_filiere(id_filiere)

        # on itère sur cette liste
        for id_etudiant in liste_etudiant:
            #on récupère tous les choix de l'étudiant
            liste_choix = ChoixDao().get_all_choix(id_etudiant)
            # on itère sur la liste des id de dominantes choisies
            for id_dominante in liste_choix:
                #on cherche à voir s'il y a de la place dans la dominante
                if id_filiere == 1:
                    if EtudiantDao().get_place_restante_id(id_dominante)[0] == 0:
                        continue
                elif id_filiere == 2:
                    if EtudiantDao().get_place_restante_id(id_dominante)[1] == 0:
                        continue
                else :
                    # il y a de la place donc on ajoute l'étudiant
                    ligne_modifie = EtudiantDao().updateDominante(id_dominante, id_etudiant)
                    if ligne_modifie == 1:
                        break # on passe à l'étudiant suivant


