from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Interface import edit_screen
from Interface import show_screen
from Interface import transition_screen

class initial_screen(QtWidgets.QWidget):

    def __init__(self):
            super().__init__()
            self.init_ui()
            self.setWindowTitle("Portfolio Manager")
            self.setWindowIcon(QtGui.QIcon("bbicon.png"))



    def init_ui(self):

        self.edit_button = QtWidgets.QPushButton("Düzenle(Ekle/Çıkar)")
        self.show_button = QtWidgets.QPushButton("Portföyümü Göster")
        self.welcome_label = QtWidgets.QLabel()
        self.welcome_label.setText("Welcome to the Portfolio Manager v0.0.1")

        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setFont(QtGui.QFont("",20))
        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()
        h_box.addStretch()
        v_box.addWidget(self.welcome_label)

        v_box.addStretch()
        h_box.addWidget(self.edit_button)
        h_box.addWidget(self.show_button)
        h_box.addStretch()
        v_box.addLayout(h_box)



        self.setGeometry(100,100,500,500)
        self.setLayout(v_box)
        self.edit_button.clicked.connect(self.edit_button_is_clicked)
        self.show_button.clicked.connect(self.portfolio_button_is_clicked)
        self.show()


    def edit_button_is_clicked(self):
        self.edit_sc = edit_screen.edit_screen()
        self.edit_sc.init_ui()
        self.edit_sc.show()
        self.hide()

    def portfolio_button_is_clicked(self):
        self.trans_screen = transition_screen.TransitionScreen()
        self.trans_screen.init_ui()
        self.trans_screen.show()
        self.hide()












