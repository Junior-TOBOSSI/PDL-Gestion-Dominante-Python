import oracledb
from oracledb import Error
from dao.ConnectionDao import ConnectionDao
from dao.FiliereDao import FiliereDao
from dao.DominanteDao import DominanteDao
from model import Dominante
from model.Etudiant import Etudiant

class EtudiantDao(ConnectionDao):

    def __init__(self):
        super().__init__()

    """
        :return la liste de tous les étudiants de la base de données
    """
    def getAll(self):
        returnValue = []
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user = self._username, 
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ETUDIANT")
            colonnes = [col[0] for col in cursor.description]
            for line in cursor.fetchall():
                dict_infos_etud = dict(zip(colonnes, line))
                filiere = FiliereDao().get(dict_infos_etud["IDFILIERE"])
                dominante = Dominante()
                if dict_infos_etud["IDDOMINANTE"]:
                    dominante = DominanteDao().get(dict_infos_etud["IDDOMINANTE"])
                returnValue.append(Etudiant( id = dict_infos_etud["IDETUDIANT"], nom= dict_infos_etud["NOM"],
                                      prenom= dict_infos_etud["PRENOM"], classement= dict_infos_etud["CLASSEMENT"],
                                       mot_de_passe= dict_infos_etud["MOTDEPASSE"], filiere= filiere,
                                     promotion= dict_infos_etud["IDPROMOTION"], date_de_naissance= dict_infos_etud["DATENAISSANCE"],
                                       dominante_finale= dominante))
        except oracledb.Error as error :
            print("une erreur est survenue :", error)
        finally :
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return returnValue

    """
           :return la liste de tous les étudiants de la base de données
       """

    def get(self, id :int):
        returnValue = None
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user=self._username,
                password=self._password,
                dsn=self._dsn
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM ETUDIANT WHERE IDETUDIANT = {id}")
            colonnes = [col[0] for col in cursor.description]
            for line in cursor.fetchall():
                dict_infos_etud = dict(zip(colonnes, line))
                filiere = FiliereDao().get(dict_infos_etud["IDFILIERE"])
                dominante = Dominante()
                if dict_infos_etud["IDDOMINANTE"]:
                    dominante = DominanteDao().get(dict_infos_etud["IDDOMINANTE"])
                returnValue = Etudiant(id=dict_infos_etud["IDETUDIANT"], nom=dict_infos_etud["NOM"],
                                            prenom=dict_infos_etud["PRENOM"], classement=dict_infos_etud["CLASSEMENT"],
                                            mot_de_passe=dict_infos_etud["MOTDEPASSE"], filiere=filiere,
                                            promotion=dict_infos_etud["IDPROMOTION"],
                                            date_de_naissance=dict_infos_etud["DATENAISSANCE"],
                                            dominante_finale=dominante)
        except oracledb.Error as error:
            print("une erreur est survenue :", error)
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return returnValue

    """
        :return une deux valeurs 
        la première un boolean qui est à true si l'étudiant connecté est dans la base de données
        la deuxième l'étudiant connecté si boolean est true sinon None 
    """
    def isEtudiant(self, etud : Etudiant) :

        return_etudiant = None
        connection = None
        cursor = None
        try:
            connection = oracledb.connect(
                user = self._username, 
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            ma_requete = f"SELECT * FROM ETUDIANT WHERE IDETUDIANT = :1 AND MOTDEPASSE = :2"
            parametres = (etud.id, etud.mot_de_passe)
            cursor.execute(ma_requete, parametres)
            line = cursor.fetchone()
            if line:
                colonnes = [col[0] for col in cursor.description]
                dict_infos_etud = dict(zip(colonnes, line))
                filiere = FiliereDao().get(dict_infos_etud["IDFILIERE"])
                dominante = Dominante()
                if dict_infos_etud["IDDOMINANTE"] :
                    dominante = DominanteDao().get(dict_infos_etud["IDDOMINANTE"])
                return_etudiant = Etudiant( id = dict_infos_etud["IDETUDIANT"], nom= dict_infos_etud["NOM"],
                                      prenom= dict_infos_etud["PRENOM"], classement= dict_infos_etud["CLASSEMENT"],
                                       mot_de_passe= dict_infos_etud["MOTDEPASSE"], filiere= filiere,
                                     promotion= dict_infos_etud["IDPROMOTION"], date_de_naissance= dict_infos_etud["DATENAISSANCE"],
                                       dominante_finale= dominante)
        except Error as error:
            print(f"Une erreur est survenue lors de la vérification d'accessibilité, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return return_etudiant

    """
        :return l'étudiant avec ses identifiants modifiés
    """
    def updateProfil(self, etudiant : Etudiant):

        return_etudiant = None
        connection = None
        cursor = None
        try :
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            requete = "UPDATE ETUDIANT SET MOTDEPASSE = :1 WHERE IDETUDIANT = :2"
            parameters = (etudiant.mot_de_passe, etudiant.id)
            cursor.execute(requete, parameters)
            connection.commit()
            return_etudiant = self.isEtudiant( Etudiant( id = etudiant.id, mot_de_passe = etudiant.mot_de_passe))
            print(return_etudiant.mot_de_passe)
        except Error as error:
            print(f"Une erreur est survenu lors de la modification du profil etudiant, ({error})")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return return_etudiant

    """
        :return 1 si l'étudiant à pu être ajouté à la base de données
        sinon 0
    """
    def add(self, etudiant : Etudiant):

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
            requete = "INSERT INTO ETUDIANT (IDETUDIANT, NOM, PRENOM, CLASSEMENT, MOTDEPASSE, IDPROMOTION, IDFILIERE, DATENAISSANCE) VALUES ( :1, :2, :3, :4, :5, :6, :7, :8)"
            parametres = (etudiant.id, etudiant.nom, etudiant.prenom, etudiant.classement, etudiant.mot_de_passe, etudiant.promotion, etudiant.filiere.id, etudiant.date_de_naissance)
            cursor.execute(requete, parametres)
            connection.commit()
            returnValue = cursor.rowcount
        except Error as error :
            print(f"Une erreur est survenu lors de l'ajout de l'étudiant, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return returnValue

    """
        :return 1 si l' étudiant à pu être 
        sinon 0
    """
    def update(self, etudiant : Etudiant) :

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
            requete = "UPDATE ETUDIANT SET NOM = :1, PRENOM = :2, CLASSEMENT = :3, MOTDEPASSE = :4, IDPROMOTION = :5, IDFILIERE = :6, DATENAISSANCE = :7 WHERE IDETUDIANT = :8"
            parametres = (etudiant.nom, etudiant.prenom, etudiant.classement, etudiant.mot_de_passe, etudiant.promotion, etudiant.filiere.id, etudiant.date_de_naissance,  etudiant.id)
            cursor.execute(requete, parametres)
            connection.commit()
            returnValue = cursor.rowcount
        except Error as error:
            print(f"Une erreur est survenu lors de l'ajout de l'étudiant, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return returnValue

    """
        :return 1 si l'étudiant à pu être supprimé de la base de données 
        sinon 0
    """
    def supprimer(self, id : int):

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
            requete = f"DELETE ETUDIANT WHERE IDETUDIANT = {id}"
            cursor.execute(requete)
            cursor.commit()
        except Error as error:
            print(f"Une erreur est survenu lors de la suppression de l'étudiant {error}")
        finally :
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()

    """
    :return une liste dont le premier élément est le nombre de places restantes fise et le second élément est le
    nombre de place restantes fisa
    """
    def get_place_restante_id(self, idDominante : int):

        return_value = []
        connection = None
        cursor = None
        try :
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            requete = f"SELECT COUNT(*) AS COUNT FROM ETUDIANT WHERE IDDOMINANTE = {idDominante}"
            cursor.execute(requete)
            values = cursor.fetchone()[0]
            rest_fise = DominanteDao().get(idDominante).place_max - values
            return_value.append(rest_fise)
            rest_apprentis = DominanteDao().get(idDominante).place_max_apprentis - values
            return_value.append(rest_apprentis)
        except Error as error:
            print(f"Une erreur est survenu lors de l'accès à la table étudiant, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return return_value

    """
        :return la liste des étudiants sans dominantes
    """
    def getEtudiantSansDominante(self, idFiliere : int):

        connection = None
        cursor = None
        return_value = [] # contiendra la liste des étudiants sans dominantes de la filiere concerné
        try:
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            requete = "SELECT * FROM ETUDIANT WHERE IDDOMINANTE IS NULL"
            cursor.execute(requete)
            colonne = [col[0] for col in cursor.description]
            lines = cursor.fetchall()
            for line in lines:
                dict_infos_etud = dict(zip(colonne, line))
                return_value.append(Etudiant(id=dict_infos_etud["IDETUDIANT"], nom=dict_infos_etud["NOM"],
                                            prenom=dict_infos_etud["PRENOM"]))
        except Error as error:
            print(f"Une erreur s'est produit lors de la récupération des étudiants, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return return_value

    """
        :return tous les étudiants de la filiere
        :param 
    """
    def get_all_filiere(self, id_filiere : int):

        connection = None
        cursor = None
        returnValue = [] # contiendra la liste des étudiants de la filiere concerné
        try:
            connection = oracledb.connect(
                user = self._username,
                password = self._password,
                dsn = self._dsn
            )
            cursor = connection.cursor()
            requete = f"SELECT IDETUDIANT FROM ETUDIANT WHERE IDFILIERE = {id_filiere}"
            cursor.execute(requete)
            returnValue = cursor.fetchall()
        except Error as error:
            print(f"Une erreur s'est produit lors de la récupération des étudiants, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()

    """
        :return 1 si la dominante finale de l'étudiant à pu être modifier 
        sinon 0
    """
    def updateDominante(self, id_dominante, id_etudiant):

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
            requete = "UPDATE ETUDIANT SET IDDOMINANTE = :1 WHERE IDETUDIANT = :2"
            parametres = (id_dominante, id_etudiant)
            cursor.execute(requete, parametres)
            connection.commit()
            returnValue = cursor.rowcount
        except Error as error:
            print(f"Une erreur est survenu lors de l'ajout de l'étudiant, {error}")
        finally:
            if cursor in locals():
                cursor.close()
            if connection in locals():
                connection.close()
        return returnValue

"""
    if __name__ == "__main__":
        EtudiantDao().get_place_restante_id(2)
"""
