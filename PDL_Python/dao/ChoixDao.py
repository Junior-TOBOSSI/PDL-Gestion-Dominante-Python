import oracledb
from oracledb import Error
from dao.ConnectionDao import ConnectionDao
from dao.EtudiantDao import EtudiantDao


class ChoixDao(ConnectionDao):

    def __int__(self):
        super().__init__()

    """
        :return l'index du dernier enrégistrement de la table choix
    """
    def current_id_choix(self):

        return_value = 0
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            requete = "SELECT COUNT(*) AS COUNT FROM CHOIX"
            cursor.execute(requete)
            returnValue = cursor.fetchone()[0]
        except Error as error:
            print("Une erreur est survenue dans la connexion à la table choix")
        finally:
            if connection in locals():
                connection.close()
            if cursor in locals():
                cursor.close()
        return return_value

    """
        :return le nombre de choix qui ont pu être inséré dans la base de données
    """
    def add(self, choix):

        return_value = 0
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            for i in range (len(choix.ids)) :
                requete = "INSERT INTO CHOIX (NUMCHOIX, IDDOM, IDETUDIANT) VALUES ( :1, :2, :3)"
                parameters = (choix.ids[i], choix.etudiant.id, choix.dominantes[i].id)
                cursor.execute(requete, parameters)
                connection.commit()
        except Error as error:
            print(f"Une erreur est survenue lors de l'ajout des choix, ({error})")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return return_value

    """
        :return la liste de tous les étudiants ayant choisi
        :param dominante
    """
    def getListEtudiant(self, id_dominante : int):

        return_value = []
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user=self._username,
                password=self._password,
                dsn=self._dsn
            )
            cursor = connection.cursor()
            requete = f"SELECT IDETUDIANT FROM CHOIX WHERE IDDOM = {id_dominante}"
            cursor.execute(requete)
            lines = cursor.fetchall()
            for id_etudiant in lines:
                return_value.append(EtudiantDao().get(id_etudiant[0]))
        except Error as error:
            print(f"Une erreur est survenue lors de la récupération des étudiants pour cette dominante, ({error})")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return return_value

    """
        :return la liste de tous les id_dominante choisi par un étudiant
    """
    def get_all_choix(self, id_etudiant : int):
        return_value = []
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user=self._username,
                password=self._password,
                dsn=self._dsn
            )
            cursor = connection.cursor()
            requete = f"SELECT IDDOMINANTE FROM CHOIX WHERE IDETUDIANT= {id_etudiant} ORDER BY NUMCHOIX ASC"
            cursor.execute(requete)
            for id_etudiant in cursor.fetchall():
                return_value.append(id_etudiant[0])
        except Error as error:
            print(f"Une erreur est survenue lors de la récupération des étudiants pour cette dominante, ({error})")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return return_value

    def dict_dom_place(self):

        return_value = None
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            requete = ("SELECT SIGLE, COUNT(SIGLE) AS COUNT FROM CHOIX INNER JOIN DOMINANTE ON CHOIX.IDDOM = DOMINANTE.IDDOM GROUP BY SIGLE ORDER BY SIGLE")
            cursor.execute(requete)
            lines = cursor.fetchall()
            return_value = dict(lines)
        except Error as error:
            print("Une erreur est survenu lors de l'accès aux tables choix et dominante")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return return_value

"""
if __name__ == "__main__":
    ChoixDao().dict_dom_place()
"""

