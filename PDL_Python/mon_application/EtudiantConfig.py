from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLineEdit,QApplication
from PyQt5.QtWidgets import QMessageBox, QFrame, QTableWidgetItem


class EtudiantConfig(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Gestion dominantes")
        self.setWindowIcon(QIcon("../data/iconeBarre.ico"))
        self.setMinimumSize(461, 328)
        from gui_ui.connection_user import Ui_Frame_User
        self.frame_user = QFrame()
        self.ui_frame_user = Ui_Frame_User()
        self.ui_frame_user.setupUi(self.frame_user)
        self.setCentralWidget(self.frame_user)
        self.ui_frame_user.case_mdp.setEchoMode(QLineEdit.Password)
        self.ui_frame_user.btn_se_connecter.clicked.connect(self.on_interface_etudiant)

    def on_interface_etudiant(self):

        from model import Etudiant

        from dao import EtudiantDao

        etudiant_dao = EtudiantDao()

        id = int(self.ui_frame_user.case_id.text())

        mdp = self.ui_frame_user.case_mdp.text()

        etu_entre = Etudiant(id = id, mot_de_passe = mdp)

        mon_etudiant = etudiant_dao.isEtudiant(etu_entre)

        if mon_etudiant :
            # on définit le protrait de l'étudiant connecté
            self.__etudiant = mon_etudiant

            from gui_ui.interface_etudiant import Interface_etudiant

            self.frame_interface_etudiant = QFrame()

            self.ui_frame_interface_etudiant = Interface_etudiant()

            self.ui_frame_interface_etudiant.setupUi(self.frame_interface_etudiant)

            self.frame_interface_etudiant.setStyleSheet(QApplication.instance().styleSheet())

            self.ui_frame_interface_etudiant.__dict__.values()

            self.setCentralWidget(self.frame_interface_etudiant)

            self.ui_frame_interface_etudiant.btn_choix.clicked.connect(self.on_choix_etudiant)
            self.ui_frame_interface_etudiant.btn_dominante.clicked.connect(self.on_dominante_finale)
            self.ui_frame_interface_etudiant.pushButton.clicked.connect(self.on_profil)

        else:
            QMessageBox.information(self, "Identification..", "L'authentification n'a pas abouti !")


    def on_profil(self):
        self.ui_frame_interface_etudiant.stackedWidget.setCurrentIndex(2)
        self.ui_frame_interface_etudiant.case_id.setText(str(self.__etudiant.id))
        self.ui_frame_interface_etudiant.case_id.setReadOnly(True)
        self.ui_frame_interface_etudiant.case_ddn.setText(str(self.__etudiant.date_de_naissance))
        self.ui_frame_interface_etudiant.case_ddn.setReadOnly(True)
        self.ui_frame_interface_etudiant.case_nom.setText(self.__etudiant.nom)
        self.ui_frame_interface_etudiant.case_nom.setReadOnly(True)
        self.ui_frame_interface_etudiant.case_prenom.setText(self.__etudiant.prenom)
        self.ui_frame_interface_etudiant.case_prenom.setReadOnly(True)
        self.ui_frame_interface_etudiant.case_filiere.setText(self.__etudiant.filiere.nom)
        self.ui_frame_interface_etudiant.case_filiere.setReadOnly(True)
        self.ui_frame_interface_etudiant.case_mdp.setText(self.__etudiant.mot_de_passe)
        self.ui_frame_interface_etudiant.case_mdp.setReadOnly(True)

        self.ui_frame_interface_etudiant.btn_modifier.clicked.connect(self.on_modifier_profil)
        self.ui_frame_interface_etudiant.btn_valider.clicked.connect(self.on_valider_profil)
        self.ui_frame_interface_etudiant.btn_valider.setEnabled(False)

    def on_modifier_profil(self):

        self.ui_frame_interface_etudiant.btn_valider.setEnabled(True)
        self.ui_frame_interface_etudiant.case_mdp.setReadOnly(False)

    def on_valider_profil(self):

        from dao.EtudiantDao import EtudiantDao
        from model.Etudiant import Etudiant

        mdp = self.ui_frame_interface_etudiant.case_mdp.text()

        etudiant_dao = EtudiantDao()

        nouveau_profil = etudiant_dao.updateProfil( Etudiant( id = self.__etudiant.id, mot_de_passe = mdp))

        if nouveau_profil :
            self.__etudiant = nouveau_profil

            QMessageBox.information(self, "Modification", "Modification effectuée avec succès :)")
            self.ui_frame_interface_etudiant.btn_valider.setEnabled(False)
        else :
            QMessageBox.information(self, "Modification", "Modification non effectuée :(")
            self.ui_frame_interface_etudiant.btn_valider.setEnabled(False)
            self.ui_frame_interface_etudiant.case_mdp.setReadOnly(True)


    def on_dominante_finale(self):

        self.ui_frame_interface_etudiant.stackedWidget.setCurrentIndex(1)

        if not self.__etudiant.dominante_finale.id ==  0 :
            self.ui_frame_interface_etudiant.entete.setText("Félicitations, la dominante retenue après délibération est : ")
            self.ui_frame_interface_etudiant.label.setText(f"{self.__etudiant.dominante_finale.nom_long} ({self.__etudiant.dominante_finale.sigle})")
        else :
            self.ui_frame_interface_etudiant.label.setText("")


    def on_choix_etudiant(self):

        from dao.DominanteDao import DominanteDao
        self.index_choix = 0
        self.list_dom_choisi = []

        dominante_dao = DominanteDao()
        self.list_dominantes = dominante_dao.getAll()

        self.ui_frame_interface_etudiant.stackedWidget.setCurrentIndex(0)
        self.ui_frame_interface_etudiant.tableWidget.setColumnCount(3)
        self.ui_frame_interface_etudiant.tableWidget.setRowCount(len(self.list_dominantes))
        self.ui_frame_interface_etudiant.tableWidget.setHorizontalHeaderLabels(["Choix", "ID DOM", "NOM DOM"])

        for index, dom in enumerate(self.list_dominantes):
            self.ui_frame_interface_etudiant.tableWidget.setItem(index, 2, QTableWidgetItem(dom.nom_long))
            self.ui_frame_interface_etudiant.tableWidget.setItem(index, 1, QTableWidgetItem(str(dom.id)))


        self.ui_frame_interface_etudiant.tableWidget.cellClicked.connect(self.on_cell_dominante)
        self.ui_frame_interface_etudiant.reprendre.clicked.connect(self.on_reprendre_choix)
        self.ui_frame_interface_etudiant.envoyer.clicked.connect(self.on_envoyer_choix)
        self.ui_frame_interface_etudiant.envoyer.setEnabled(False)

    def on_reprendre_choix(self):
        for index in range(len(self.list_dominantes)) :
            self.ui_frame_interface_etudiant.tableWidget.setItem(index, 0, None)
        self.list_dom_choisi.clear()
        self.index_choix = 0
        self.ui_frame_interface_etudiant.envoyer.setEnabled(False)

    def on_envoyer_choix(self):

        from dao.ChoixDao import ChoixDao
        from model.Choix import Choix
        from dao.DominanteDao import DominanteDao

        choix_dao = ChoixDao()
        dominante_dao = DominanteDao()

        current_id_choix = choix_dao.current_id_choix()
        ids = []

        # création du numéro de choix pour chaque dominante choix
        for i in range(self.__etudiant.filiere.nombre_choix):
            current_id_choix += 1
            ids.append(current_id_choix)

        # création de la liste des dominantes sur la base de id de dominantes

        dominantes = []

        for i in range(self.__etudiant.filiere.nombre_choix):
            dominantes.append(dominante_dao.get(self.list_dominantes[i]))

        is_envoyer = choix_dao.add(Choix(ids, self.__etudiant, dominantes))

        if is_envoyer :
            QMessageBox.information(self, "Envoyer", "Vos choix ont bien été prises en compte")
        else:
            QMessageBox.information(self, "Envoyer", "vos choix n'ont pas pu être envoyés")


    def on_cell_dominante(self, row, column):

        if(self.index_choix < self.__etudiant.filiere.nombre_choix):
            if not self.ui_frame_interface_etudiant.tableWidget.item(row, 0) :
                self.index_choix += 1
                self.ui_frame_interface_etudiant.tableWidget.setItem(row, 0, QTableWidgetItem(str(self.index_choix)))
                print(str(self.ui_frame_interface_etudiant.tableWidget.item(row, 1).text()))
                self.list_dom_choisi.append(str(self.ui_frame_interface_etudiant.tableWidget.item(row, 1).text()))
                if (self.index_choix == self.__etudiant.filiere.nombre_choix):
                    self.ui_frame_interface_etudiant.envoyer.setEnabled(True)

        else :
            QMessageBox.information(self, "Limit..", f"Nombre de choix maximum ({self.__etudiant.filiere.nombre_choix}) atteint")