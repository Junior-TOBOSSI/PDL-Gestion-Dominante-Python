import oracledb
from oracledb import Error
from dao import ConnectionDao
from model.Admin import Admin


class AdminDao(ConnectionDao):


    def __init__(self):
        super().__init__()

    """
        :return les données complètes de l'admin dont on cherche à vérifier l'identité
    """
    def isAdmin(self, admin : Admin):

        returnValue = Admin()
        connection = None
        cursor = None
        try:
            #on établit la connection
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            ma_requete = "SELECT * FROM ADMIN WHERE IDADMIN = :1 AND MOTDEPASSE = :2"
            parametres = (admin.id, admin.mot_de_passe)
            cursor.execute(ma_requete, parametres)
            line = cursor.fetchone()
            colonnes = [col[0] for col in cursor.description]
            if line:
                dict_admin = dict(zip(colonnes, line))
                returnValue = Admin(id = dict_admin["IDADMIN"], nom = dict_admin["NOM"],
                                    prenom = dict_admin["PRENOM"], mot_de_passe= dict_admin["MOTDEPASSE"])
        except Error as err:
            print(f"Une erreur a une lieu {err}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return returnValue

    """
        :return 1 si les données de l'admin ont pu être modifié
        sinon 1
    """
    def update(self, id, mot_de_passe):

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
            ma_requete = "UPDATE ADMIN SET MOTDEPASSE = :1 WHERE IDADMIN = :2"
            parametre = (mot_de_passe, id)
            cursor.execute(ma_requete, parametre)
            connection.commit()
            returnValue = cursor.rowcount
        except Error as error:
            print(f"Des erreurs sont survenues lors de la modification du profil admin, {error}")
        finally :
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return returnValue






