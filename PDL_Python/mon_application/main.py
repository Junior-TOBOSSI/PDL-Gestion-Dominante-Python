import os
import sys
import ctypes

from PyQt5.QtGui import QIcon

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gui_ui.type_user import Ui_Frame
from mon_application.EtudiantConfig import EtudiantConfig
from mon_application.AdminConfig import AdminConfig


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(QtCore.Qt.AA_Use96Dpi, True)
myappid = 'mon.application.unique.nom.1.0'  # doit être unique
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



class Authentification(QMainWindow):

    def __init__(self):
        super().__init__()


        self.frame = QFrame()
        self.ui_frame = Ui_Frame()
        self.ui_frame.setupUi(self.frame)
        self.setWindowTitle("Gestion dominantes")
        self.setWindowIcon(QIcon("../data/iconeBarre.ico"))
        self.setMinimumSize(461, 328)
        self.setCentralWidget(self.frame)
        self.ui_frame.btn_admin.clicked.connect(self.on_connection_admin)
        self.ui_frame.btn_etudiant.clicked.connect(self.on_connection_etudiant)


    def on_connection_etudiant(self):

        self.connection_user = EtudiantConfig()
        self.connection_user.show()
        self.close()

    def on_connection_admin(self):

        self.connection_user = AdminConfig()
        self.connection_user.show()
        self.close()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("../data/IconeDelete.png"))

    app.setStyleSheet("""
        * {
            font-family : "Arial";
            font-size : 10pt;
            }
    """)

    window = Authentification()
    window.show()


    sys.exit(app.exec_())
