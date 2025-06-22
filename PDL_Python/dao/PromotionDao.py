import oracledb
from oracledb import Error
from dao.ConnectionDao import ConnectionDao
from model.Promotion import Promotion

class PromotionDao(ConnectionDao):

    def __init__(self):
        super().__init__()

    """
        :return la promotion correspond à 
        :param 
    """
    def get(self, id : int):

        returnValue = Promotion()
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            ma_requete = f"SELECT * FROM PROMOTION WHERE IDPROMOTION = {id}"
            cursor.execute(ma_requete)
            line = cursor.fetchone()
            if line:
                colonnes = [col[0] for col in cursor.description]
                dict_infos_promotion = dict(zip(colonnes, line))
                returnValue = Promotion( id= dict_infos_promotion["IDPROMOTION"],
                                         statut= dict_infos_promotion["STATUT"])
        except Error as error:
            print(f"Une erreur est survenu lors de l'initialisation de la promotion, {error}")
        finally:
            if connection in locals():
                connection.close()
            if cursor in locals():
                cursor.close()
        return returnValue