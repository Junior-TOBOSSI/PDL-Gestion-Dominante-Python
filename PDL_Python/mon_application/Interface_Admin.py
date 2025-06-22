
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QFrame, QMessageBox, QTableWidgetItem, QVBoxLayout

from dao import TraitementDao, ChoixDao
from model import Filiere, Dominante
from model.Choix import Choix
from mon_application import AdminConfig
from dao.AdminDao import AdminDao
from dao.DominanteDao import DominanteDao
from dao.EtudiantDao import EtudiantDao
from dao.FiliereDao import FiliereDao
from model.Etudiant import Etudiant
from datetime import datetime
from mon_application.Visuels import Visuels

class Interface_Admin(AdminConfig):

    def __init__(self, admin_profil):

        super().__init__()
        self.admin = admin_profil
        self.setMinimumSize(461, 328)
        from gui_ui import Interface_admin
        self.frame_interface_admin = QFrame()
        self.ui_frame_interface_admin = Interface_admin()
        self.ui_frame_interface_admin.setupUi(self.frame_interface_admin)
        self.ui_frame_interface_admin.detail_menu.hide()
        self.setCentralWidget(self.frame_interface_admin)


        self.ui_frame_interface_admin.btn_profil.clicked.connect(self.on_profil_admin)
        self.ui_frame_interface_admin.menu_admin.clicked.connect(self.on_menu_admin)

        self.show_detail_menu = False
        self.tableEtudiant = False
        self.tableDominante = False
        self.tableEtape = False
        self.font = QFont()
        self.font.setPointSize(8)

        self.ui_frame_interface_admin.btn_dominante.clicked.connect(self.on_click_dominante)
        self.ui_frame_interface_admin.btn_etudiant.clicked.connect(self.on_click_etudiant)
        self.ui_frame_interface_admin.btn_etape.clicked.connect(self.on_click_etape)

        self.ui_frame_interface_admin.stackedWidget.setCurrentWidget(self.ui_frame_interface_admin.pageAjouterEtudiant)
        self.ui_frame_interface_admin.btn_ajouter_etudiant.clicked.connect(self.on_click_ajouter_etudiant)

    def on_profil_admin(self):

        self.ui_frame_interface_admin.stackedWidget.setCurrentWidget(self.ui_frame_interface_admin.pageProfil)
        self.ui_frame_interface_admin.case_profil_mdp.setReadOnly(True)

        self.ui_frame_interface_admin.case_profil_id.setText(str(self.admin.id))
        self.ui_frame_interface_admin.case_profil_nom.setText(self.admin.nom)
        self.ui_frame_interface_admin.case_profil_prenom.setText(self.admin.prenom)
        self.ui_frame_interface_admin.case_profil_mdp.setText(self.admin.mot_de_passe)
        self.ui_frame_interface_admin.btn_modifier.clicked.connect(self.on_click_modify)
        self.ui_frame_interface_admin.btn_valider.clicked.connect(self.on_click_validate)

    def on_click_modify(self):

        self.ui_frame_interface_admin.case_profil_mdp.setReadOnly(False)
        self.ui_frame_interface_admin.btn_valider.setEnabled(True)

    def on_menu_admin(self):
        if self.show_detail_menu :
            self.ui_frame_interface_admin.detail_menu.hide()
            self.show_detail_menu = False
        else :
            self.ui_frame_interface_admin.detail_menu.show()
            self.show_detail_menu = True

    def on_click_validate(self):
        adminDao = AdminDao()

        id_admin = self.ui_frame_interface_admin.case_profil_id.text()
        mot_de_passe = self.ui_frame_interface_admin.case_profil_mdp.text()
        ligne_update = adminDao.update(id_admin, mot_de_passe) # on récupère le nombre de ligne affectée par la modification

        if ligne_update == 1 :
            QMessageBox.information(self, "Succes", "Vos modifications ont été prises en compte")
        else :
            QMessageBox.information(self, "Echec", "Vos modifications n'ont pas été prises en compte")


    def on_click_dominante(self):

        # on configure les différents boutons
        self.ui_frame_interface_admin.stackedWidget.setCurrentWidget(self.ui_frame_interface_admin.pageDominante)

        if not self.tableDominante:
            self.tableDominante = True

            self.ui_frame_interface_admin.btn_vers_ajouter_dominante.clicked.connect(self.on_click_vers_ajouter_dominante)
            self.ui_frame_interface_admin.btn_voir_dominante.clicked.connect(self.on_click_voir_dominante)
            self.ui_frame_interface_admin.btn_supprimer_dominante.clicked.connect(self.on_click_supprimer_dominante)
            self.ui_frame_interface_admin.btn_valider_dominante.clicked.connect(self.on_click_valider_dominante)
            self.ui_frame_interface_admin.btn_dominante_visuels.clicked.connect(self.on_click_voir_visuels)

            # on remplit le tableau avec les différents éléments

            dominanteDao = DominanteDao()
            listDominantes = dominanteDao.getAll()

            self.ui_frame_interface_admin.tableDominantes.setRowCount(len(listDominantes))
            self.ui_frame_interface_admin.tableDominantes.setColumnCount(5)
            self.ui_frame_interface_admin.tableDominantes.setHorizontalHeaderLabels(["id", "nom", "sigle", "placeMax", "placeMaxAppr."])
            self.ui_frame_interface_admin.tableDominantes.setFont(self.font)
            self.ui_frame_interface_admin.tableDominantes.verticalHeader().setVisible(False)

            for index, dom in enumerate(listDominantes):
                idItem = QTableWidgetItem(str(dom.id))
                nomItem = QTableWidgetItem(dom.nom_long)
                sigleItem = QTableWidgetItem(dom.sigle)
                placeMaxItem = QTableWidgetItem(str(dom.place_max))
                placeMaxAppItem = QTableWidgetItem(str(dom.place_max_apprentis))

                self.ui_frame_interface_admin.tableDominantes.setItem(index, 0, idItem)
                self.ui_frame_interface_admin.tableDominantes.setItem(index, 1, nomItem)
                self.ui_frame_interface_admin.tableDominantes.setItem(index, 2, sigleItem)
                self.ui_frame_interface_admin.tableDominantes.setItem(index, 3, placeMaxItem)
                self.ui_frame_interface_admin.tableDominantes.setItem(index, 4, placeMaxAppItem)


    def on_click_etudiant(self):

        # on parametre les differents boutonns
        self.ui_frame_interface_admin.stackedWidget.setCurrentWidget(self.ui_frame_interface_admin.pageEtudiant)

        if not self.tableEtudiant:
            self.tableEtudiant = True
            self.ui_frame_interface_admin.btn_vers_ajouter_etudiant.clicked.connect(self.on_click_vers_ajouter_etudiant)
            self.ui_frame_interface_admin.btn_forcer_inscription.clicked.connect(self.on_click_forcer_inscription)
            self.ui_frame_interface_admin.btn_suppr_etudiant.clicked.connect(self.on_click_suppr_etudiant)
            self.ui_frame_interface_admin.btn_valider_etudiant.clicked.connect(self.on_click_valider_etudiant)


            # on remplit le tableau avec les différents éléments

            etudiantDao = EtudiantDao()
            listEtudiants = etudiantDao.getAll()

            self.ui_frame_interface_admin.tableEtudiant.setRowCount(len(listEtudiants))
            self.ui_frame_interface_admin.tableEtudiant.setColumnCount(7)
            self.ui_frame_interface_admin.tableEtudiant.setHorizontalHeaderLabels(["id", "nom", "prenom", "classement", "filiere", "promo", "dominante"])
            self.ui_frame_interface_admin.tableEtudiant.verticalHeader().setVisible(False)
            self.ui_frame_interface_admin.tableEtudiant.setFont(self.font)

            self.ui_frame_interface_admin.tableEtudiant.setUpdatesEnabled(False)

            for index, etud in enumerate(listEtudiants):

                items = [
                    QTableWidgetItem(str(etud.id)),
                    QTableWidgetItem(etud.nom),
                    QTableWidgetItem(etud.prenom),
                    QTableWidgetItem(str(etud.classement)),
                    QTableWidgetItem(etud.filiere.nom),
                    QTableWidgetItem(str(etud.promotion)),
                    QTableWidgetItem(etud.dominante_finale.sigle)
                ]

                for col, item in enumerate(items):
                    self.ui_frame_interface_admin.tableEtudiant.setItem(index, col, item)

            self.ui_frame_interface_admin.tableEtudiant.setUpdatesEnabled(True)


    def on_click_etape(self):
        self.ui_frame_interface_admin.stackedWidget.setCurrentWidget(self.ui_frame_interface_admin.pageEtape)

        if not self.tableEtape :
            self.tableEtape = True

            self.ui_frame_interface_admin.btn_valider_etape.clicked.connect(self.on_click_valider_etape)
            self.ui_frame_interface_admin.btn_lancer_etape.clicked.connect(self.on_click_lancer_etape)

            # on remplit le tableau avec les différents éléments

            etapeDao = TraitementDao()
            listeEtapes = etapeDao.getAllEtapes()

            self.ui_frame_interface_admin.tableEtape.setRowCount(len(listeEtapes))
            self.ui_frame_interface_admin.tableEtape.setColumnCount(3)
            self.ui_frame_interface_admin.tableEtape.setHorizontalHeaderLabels(["id", "nom", "date de début"])
            self.ui_frame_interface_admin.tableEtape.setFont(self.font)
            self.ui_frame_interface_admin.tableEtape.verticalHeader().setVisible(False)


            for index, etape in enumerate(listeEtapes):
                idItem = QTableWidgetItem(str(etape.id))
                nomItem = QTableWidgetItem(etape.nom)
                dateItem = QTableWidgetItem(str(etape.date_de_naissance))


                self.ui_frame_interface_admin.tableEtape.setItem(index, 0, idItem)
                self.ui_frame_interface_admin.tableEtape.setItem(index, 1, nomItem)
                self.ui_frame_interface_admin.tableEtape.setItem(index, 2, dateItem)


    def on_click_vers_ajouter_dominante(self):

        self.ui_frame_interface_admin.stackedWidget.setCurrentWidget(self.ui_frame_interface_admin.pageAjouterDominante)

        # on paramètre les boutons sur l'interface ajouter une dominante

        self.ui_frame_interface_admin.btn_ajouter_dominante.clicked.connect(self.on_click_ajouter_dominante)

    def on_click_vers_ajouter_etudiant(self):

        self.ui_frame_interface_admin.stackedWidget.setCurrentWidget(self.ui_frame_interface_admin.pageAjouterEtudiant)
        self.ui_frame_interface_admin.btn_ajouter_etudiant.clicked.connect(self.on_click_ajouter_etudiant)

    def on_click_supprimer_dominante(self):

        # on détermine la ligne sélectionnée
        rowSelected = self.ui_frame_interface_admin.tableDominantes.currentRow()

        # on sélectionne l'idée correspondant à cette dominante
        id_dominante = int(self.ui_frame_interface_admin.tableDominantes.item(rowSelected, 0).text())

        ligne_suppr = DominanteDao().supprimer(id_dominante)

        if ligne_suppr == 1:
            QMessageBox.information(self, "Succès", "Etudiant Supprimé avec succès")
        else:
            QMessageBox.information(self, "Succès", "Suppression impossible")

    def on_click_valider_dominante(self):

        # on détermine la ligne sélectionnée
        rowSelected = self.ui_frame_interface_admin.tableDominantes.currentRow()

        # on sélectionne l'idée correspondant à cette dominante
        idDominante = int(self.ui_frame_interface_admin.tableDominantes.item(rowSelected, 0).text())
        nom = self.ui_frame_interface_admin.tableDominantes.item(rowSelected, 1).text()
        sigle = self.ui_frame_interface_admin.tableDominantes.item(rowSelected, 2).text()
        place_max = int(self.ui_frame_interface_admin.tableDominantes.item(rowSelected, 3).text())
        place_max_apprentis = int(self.ui_frame_interface_admin.tableDominantes.item(rowSelected, 4).text())


        dominante = Dominante(id=idDominante, nom_long = nom, sigle = sigle,
                            place_max =place_max, place_max_apprentis=place_max_apprentis)

        ligneUpdate = DominanteDao().update(dominante)
        if ligneUpdate == 1:
            QMessageBox.information(self, "Succes", "Modifications effectuées avec succès")
        else:
            QMessageBox.information(self, "Echec", "Les modifications n'ont pas pu être effectuées")

    def on_click_voir_dominante(self):
        #on récupère l'id de la dominante dont on veut voir le positionnement des étudiants
        rowSelected = self.ui_frame_interface_admin.tableDominantes.currentRow()
        if rowSelected != -1 :

            idDominante = int(self.ui_frame_interface_admin.tableDominantes.item(rowSelected, 0).text())

            listEtudiant = ChoixDao().getListEtudiant(idDominante)

            self.ui_frame_interface_admin.tableVoirDominante.setRowCount(len(listEtudiant))
            self.ui_frame_interface_admin.tableVoirDominante.setColumnCount(3)
            self.ui_frame_interface_admin.tableVoirDominante.setHorizontalHeaderLabels(["ID", "NOM", "PRENOM"])

            for index, etudiant in enumerate(listEtudiant):
                self.ui_frame_interface_admin.tableVoirDominante.setItem(index, 0, QTableWidgetItem(str(etudiant.id)))
                self.ui_frame_interface_admin.tableVoirDominante.setItem(index, 1, QTableWidgetItem(etudiant.nom))
                self.ui_frame_interface_admin.tableVoirDominante.setItem(index, 2, QTableWidgetItem(etudiant.prenom))

            self.ui_frame_interface_admin.stackedWidget.setCurrentWidget(self.ui_frame_interface_admin.pageVoirChoixDominante)
            self.ui_frame_interface_admin.entete_voir_dominante.setText(f"{DominanteDao().get(idDominante).nom_long}, {len(listEtudiant)} / {DominanteDao().get(idDominante).place_max}")
        else:
            QMessageBox.information(self, "Erreur", "Choisir une dominante pour voir les étudiants positionnnés")

    def on_click_voir_visuels(self):
        self.mon_hist = Visuels(self.ui_frame_interface_admin.graph_dominante)

        layout = QVBoxLayout(self.ui_frame_interface_admin.graph_dominante)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.mon_hist)

        sigles = list(ChoixDao().dict_dom_place().keys())
        valeurs = list(ChoixDao().dict_dom_place().values())
        self.mon_hist.axes.bar(x = sigles, height = valeurs)
        self.mon_hist.draw()

        self.ui_frame_interface_admin.stackedWidget.setCurrentWidget(self.ui_frame_interface_admin.pageHistogrammeDominante)

    def on_click_forcer_inscription(self):
        self.ui_frame_interface_admin.stackedWidget.setCurrentWidget(self.ui_frame_interface_admin.pageForcerEtudiant)

        # on affiche les différentes dominantes

        listDominantes = DominanteDao().getAll()


        self.ui_frame_interface_admin.tableForcerDominante.setRowCount(len(listDominantes))
        self.ui_frame_interface_admin.tableForcerDominante.setColumnCount(3)
        self.ui_frame_interface_admin.tableForcerDominante.setHorizontalHeaderLabels(
            ["id", "sigle", "place Restantes"])
        self.ui_frame_interface_admin.tableForcerDominante.setFont(self.font)
        self.ui_frame_interface_admin.tableForcerDominante.verticalHeader().setVisible(False)


        for index, dom in enumerate(listDominantes):
            idItem = QTableWidgetItem(str(dom.id))
            sigleItem = QTableWidgetItem(dom.sigle)
            # on y va chercher le nombre de place restante dans la dominante
            place_restante = EtudiantDao().get_place_restante_id(dom.id)[0]
            placeRestItem = QTableWidgetItem(str(place_restante))


            self.ui_frame_interface_admin.tableForcerDominante.setItem(index, 0, idItem)
            self.ui_frame_interface_admin.tableForcerDominante.setItem(index, 1, sigleItem)
            self.ui_frame_interface_admin.tableForcerDominante.setItem(index, 2, placeRestItem)

        # on récupère la filiere pour lequel on souhaite afficher les étudiants
        str_filiere = self.ui_frame_interface_admin.case_forcer_dominante_filiere.currentText()

        id_filiere = 0

        if str_filiere == "FISA":
            id_filiere = 2
        else:
            id_filiere = 1

        listEtudiant = EtudiantDao().getEtudiantSansDominante(id_filiere)

        self.ui_frame_interface_admin.tableForcerEtudiant.setRowCount(len(listEtudiant))
        self.ui_frame_interface_admin.tableForcerEtudiant.setColumnCount(3)
        self.ui_frame_interface_admin.tableForcerEtudiant.setHorizontalHeaderLabels(["ID", "NOM", "PRENOM"])
        self.ui_frame_interface_admin.tableForcerEtudiant.setFont(self.font)

        for index, etudiant in enumerate(listEtudiant):
            self.ui_frame_interface_admin.tableForcerEtudiant.setItem(index, 0, QTableWidgetItem(str(etudiant.id)))
            self.ui_frame_interface_admin.tableForcerEtudiant.setItem(index, 1, QTableWidgetItem(etudiant.nom))
            self.ui_frame_interface_admin.tableForcerEtudiant.setItem(index, 2, QTableWidgetItem(etudiant.prenom))



    def on_click_suppr_etudiant(self):

        # on détermine la ligne sélectionnée
        rowSelected = self.ui_frame_interface_admin.tableEtudiant.currentRow()

        # on sélectionne l'idée correspondant à cet étudiant
        idEtudiant = int(self.ui_frame_interface_admin.tableEtudiant.item(rowSelected, 0).text())

        ligneSuppr = EtudiantDao().supprimer(idEtudiant)

        if ligneSuppr == 1:
            QMessageBox.information(self, "Succès", "Etudiant Supprimé avec succès")
        else:
            QMessageBox.information(self, "Succès", "Suppression impossible")

    def on_click_valider_etudiant(self):

        # on détermine la ligne sélectionnée
        rowSelected = self.ui_frame_interface_admin.tableEtudiant.currentRow()

        # on sélectionne l'idée correspondant à cet étudiant
        idEtudiant = int(self.ui_frame_interface_admin.tableEtudiant.item(rowSelected, 0).text())
        nom = self.ui_frame_interface_admin.tableEtudiant.item(rowSelected, 1).text()
        prenom = self.ui_frame_interface_admin.tableEtudiant.item(rowSelected, 2).text()
        classement = int(self.ui_frame_interface_admin.tableEtudiant.item(rowSelected, 3).text())
        filiere = int(self.ui_frame_interface_admin.tableEtudiant.item(rowSelected, 4).text())
        promotion = int(self.ui_frame_interface_admin.tableEtudiant.item(rowSelected, 5).text())
        dominante = self.ui_frame_interface_admin.tableEtudiant.item(rowSelected, 6).text()
        if dominante == "Inconnu":
            dominante_finale = None
        else :
            dominante_finale = DominanteDao.get_by_sigle(dominante)

        etudiant = Etudiant(id = idEtudiant, nom = nom, prenom= prenom,
                            classement = classement, filiere= FiliereDao().get(filiere),
                            promotion = promotion, dominante_finale= dominante_finale)

        ligneUpdate = EtudiantDao().update(etudiant)
        if ligneUpdate == 1 :
            QMessageBox.information(self, "Succes", "Modifications effectuées avec succès")
        else :
            QMessageBox.information(self, "Echec", "Les modifications n'ont pas pu être effectuées")

    def on_click_valider_etape(self):
        #on récupère les nouvelles dates

        idEtape = int(self.ui_frame_interface_admin.tableEtape.item(self.ui_frame_interface_admin.tableEtape.currentRow(), 0).text())

        rowSelected = self.ui_frame_interface_admin.tableEtape.currentRow()
        nouvelledate = self.ui_frame_interface_admin.tableEtape.item(rowSelected, 1).text()
        ligneUpdate = TraitementDao().update(nouvelledate, idEtape)

        if ligneUpdate == 1:
            QMessageBox.information(self, "Succes", "Modifications effectuées avec succès")
        else:
            QMessageBox.information(self, "Echec", "Les modifications n'ont pas pu être effectuées")


    def on_click_lancer_etape(self):
        # on récupère la date de l'étape pour voir si elle correspond à la date courante

        idEtape = int(self.ui_frame_interface_admin.tableEtape.item(self.ui_frame_interface_admin.tableEtape.currentRow(), 0).text())

        rowSelected = self.ui_frame_interface_admin.tableEtape.currentRow()
        dateStr = self.ui_frame_interface_admin.tableEtape.item(rowSelected, 1).text()

        # vérification

        madate = datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S")

        if madate.date == datetime.today() and (idEtape == 4 or idEtape == 7):
            if idEtape == 4 :
                TraitementDao().lancerTraitement(2)
                QMessageBox.information(self, "Message", "Fin du traitement Fisa", QMessageBox.Ok)
            elif idEtape == 7:
                TraitementDao().lancerTraitement(1)
                QMessageBox.information(self, "Message", "Fin du traitement Fise", QMessageBox.Ok)


    def on_click_ajouter_etudiant(self):


        #on récupère les informations du nouveau étudiant
        id_etudiant = int(self.ui_frame_interface_admin.case_etudiant_id.text())
        nom = self.ui_frame_interface_admin.case_etudiant_nom.text()
        prenom = self.ui_frame_interface_admin.case_etudiant_prenom.text()
        filiere = self.ui_frame_interface_admin.case_etudiant_filiere.currentText()
        promotion = int(self.ui_frame_interface_admin.case_etudiant_promotion.currentText())
        classement = int(self.ui_frame_interface_admin.case_etudiant_classement.text())
        datedenaissance = self.ui_frame_interface_admin.case_etudiant_ddn.date().toPyDate()

        # on crée un étudiant
        ma_filiere = Filiere()

        if filiere == "FISA":
            ma_filiere = FiliereDao().get(1)
        else :
            ma_filiere = FiliereDao().get(2)

        nouveau_etudiant = Etudiant( id = id_etudiant, nom = nom, prenom = prenom,
                                     filiere = ma_filiere, promotion= promotion,
                                     classement= classement, mot_de_passe= "motdepasse",
                                     date_de_naissance= datedenaissance)

        etudiantDao = EtudiantDao()
        ligneInsere = etudiantDao.add(nouveau_etudiant)

        if ligneInsere == 1 :
            QMessageBox.information(self, "Succes", "L'étudiant a été ajouter avec succès", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Echec", "L'étudiant n'a pas pu être ajouter", QMessageBox.Ok)


    def on_click_ajouter_dominante(self):

        # on récupère les informations du nouveau étudiant
        id_dominante = int(self.ui_frame_interface_admin.case_dominante_id.text())
        nom = self.ui_frame_interface_admin.case_dominante_nom.text()
        sigle = self.ui_frame_interface_admin.case_dominante_sigle.text()
        place_max = int(self.ui_frame_interface_admin.case_dominante_place_max.text())
        place_max_apprentis = int(self.ui_frame_interface_admin.case_dominante_place_max_appr.text())

        nouveau_dominante = Dominante(id=id_dominante, nom_long= nom, sigle = sigle,
                                      place_max= place_max, place_max_apprentis= place_max_apprentis)

        ligneInsere = DominanteDao().add(nouveau_dominante)

        if ligneInsere == 1:
            QMessageBox.information(self, "Succes", "La dominante a été ajouter avec succès", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Echec", "La dominante  n'a pas pu être ajouter", QMessageBox.Ok)
