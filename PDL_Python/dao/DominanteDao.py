import oracledb
from oracledb import Error
from dao.ConnectionDao import ConnectionDao
from model.Dominante import Dominante

class DominanteDao(ConnectionDao):

    def __init__(self):
        super().__init__()

    """
        :return la liste de toutes les dominantes dans la base de données
    """
    def getAll(self):
        list_dominantes = []
        connection = None
        cursor = None
        try :
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM DOMINANTE ORDER BY IDDOM ASC")
            for row in cursor.fetchall():
                colonnes = [col[0] for col in cursor.description]
                row_dict = dict(zip(colonnes, row))
                ma_dominante = Dominante(row_dict["IDDOM"], row_dict["NOMLONG"], row_dict["SIGLE"], row_dict["PLACEMAX"], row_dict["PLACESAPPRENTIS"] )
                list_dominantes.append(ma_dominante)
        except oracledb.Error as e :
            print("Erreur" , e)
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return list_dominantes

    """
        :return la domiannte qui correspond à 
        :param id 
    """
    def get(self, id : int):
        returnValue = Dominante()
        connection = None
        cursor = None
        if not id:
            return returnValue
        try:
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            ma_requete = f"SELECT * FROM DOMINANTE WHERE IDDOM = {id}"
            cursor.execute(ma_requete)
            line = cursor.fetchone()
            if line:
                colonnes = [col[0] for col in cursor.description]
                row_dict = dict(zip(colonnes, line))
                returnValue = Dominante(row_dict["IDDOM"], row_dict["NOMLONG"], row_dict["SIGLE"], row_dict["PLACEMAX"], row_dict["PLACESAPPRENTIS"] )
        except Error as error:
            print(f"Une erreur s'est produit lors de l'accès à la table dominante, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return returnValue

    """
        :return 1 si une nouvelle dominante à pu être ajoutée
        sinon 0
    """
    def add(self, dominante : Dominante):
        returnValue = 0
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            requete = "INSERT INTO DOMINANTE(IDDOM, NOMLONG, SIGLE, PLACEMAX, PLACESAPPRENTIS VALUES(:1, :2, :3, :4, :5)"
            parametres = (dominante.id, dominante.nom_long, dominante.sigle, dominante.place_max, dominante.place_max_apprentis)
            cursor.execute(requete, parametres)
            connection.commit()
            returnValue = cursor.rowcount
        except Error as error:
            print(f"Une erreur est survenue lors de l'ajout d'une nouvelle dominante, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()

    """
        :return 1 si la dominante a pu être modifié
        sinon 0
    """
    def update(self, dominante : Dominante):
        returnValue = 0
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user=self._username,
                password=self._password,
                dsn=self._dsn
            )
            cursor = connection.cursor()
            requete = "UPDATE DOMINANTE SET NOMLONG = :1, SIGLE = :2, PLACEMAX = :3, PLACESAPPRENTIS = :4 WHERE IDDOM = :5"
            parametres = (dominante.nom_long, dominante.sigle, dominante.place_max, dominante.place_max_apprentis, dominante.id)
            cursor.execute(requete, parametres)
            connection.commit()
            returnValue = cursor.rowcount
        except Error as error:
            print(f"Une erreur est survenue lors de la mise à jour de la dominante, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()

    """
        :return 1 si la dominante à pu être supprimé
        sinon 0
    """
    def supprimer(self, id: int):
        returnValue = 0
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user=self._username,
                password=self._password,
                dsn=self._dsn
            )
            cursor = connection.cursor()
            requete = f"DELETE DOMINANTE WHERE IDDOM = {id}"
            cursor.execute(requete)
            connection.commit()
            returnValue = cursor.rowcount
        except Error as error:
            print(f"Une erreur est survenue lors de la suppression de la dominante, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()

    def get_by_sigle(self, sigle :str):

        return_value = None
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user=self._username,
                password=self._password,
                dsn=self._dsn
            )
            cursor = connection.cursor()
            requete = f"SELECT * FROM DOMINANTE WHERE SIGLE = {sigle}"
            cursor.execute(requete)
            for row in cursor.fetchall():
                colonnes = [col[0] for col in cursor.description]
                row_dict = dict(zip(colonnes, row))
                return_value = Dominante(row_dict["IDDOM"], row_dict["NOMLONG"], row_dict["SIGLE"],
                                         row_dict["PLACEMAX"], row_dict["PLACESAPPRENTIS"])
        except Error as error:
            print(f"Une erreur est survenue lors de la suppression de la dominante, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return return_value