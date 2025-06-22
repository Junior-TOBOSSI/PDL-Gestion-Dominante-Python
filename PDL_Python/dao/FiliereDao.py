import oracledb
from oracledb import Error
from dao.ConnectionDao import ConnectionDao
from model.Filiere import Filiere

class FiliereDao(ConnectionDao):

    def __init__(self):
        super().__init__()

    """
        :return la filiere qui correspond à l'id de la filiere passée en parametre
    """
    def get(self, id : int):

        returnValue = Filiere()
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            ma_requete = f"SELECT * FROM FILIERE WHERE IDFILIERE = {id}"
            cursor.execute(ma_requete)
            line = cursor.fetchone()
            if line:
                colonnes = [col[0] for col in cursor.description]
                dict_infos_filiere = dict(zip(colonnes, line))
                returnValue = Filiere( dict_infos_filiere["IDFILIERE"],
                                       dict_infos_filiere["NOM"],
                                       dict_infos_filiere["NOMBRECHOIX"])
        except Error as error:
            print(f"Une erreur est survenue, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return returnValue