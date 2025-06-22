from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QFrame, QMessageBox, QLineEdit,QApplication




class AdminConfig(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Gestion dominantes")
        self.setWindowIcon(QIcon("../data/iconeBarre.ico"))
        from gui_ui.connection_user import Ui_Frame_User
        self.frame_user = QFrame()
        self.ui_frame_user = Ui_Frame_User()
        self.setMinimumSize(461, 328)
        self.ui_frame_user.setupUi(self.frame_user)
        self.setCentralWidget(self.frame_user)

        self.ui_frame_user.case_mdp.setEchoMode(QLineEdit.Password)
        self.ui_frame_user.btn_se_connecter.clicked.connect(self.on_interface_admin)

    def on_interface_admin(self):

        from dao import AdminDao
        admin_dao = AdminDao()
        id = int(self.ui_frame_user.case_id.text())
        mdp = self.ui_frame_user.case_mdp.text()

        from model import Admin

        admin_entrer = Admin(id = id, mot_de_passe = mdp)
        self._base_admin = admin_dao.isAdmin(admin_entrer)

        if self._base_admin.id != 0 :

            from mon_application.Interface_Admin import Interface_Admin

            self.interface_admin = Interface_Admin(self._base_admin)
            self.interface_admin.show()
            self.close()

        else:
            QMessageBox.information(self, "Identification..", "L'authentification n'a pas abouti !")





