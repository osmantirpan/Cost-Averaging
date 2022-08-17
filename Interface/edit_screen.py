from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import Interface.edit_screen2
from Interface import initial_screen
from Database import database
from Interface import transition_screen
###########################################
class edit_screen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


    def init_ui(self):
        self.trans_screen = transition_screen.TransitionScreen()
        self.setGeometry(100, 100, 500, 500)
        self.database_ = database.Database()
        self.edit_sc_back_button = QtWidgets.QPushButton("Geri")
        edit_sc_vbox = QtWidgets.QVBoxLayout()
        edit_sc_hbox = QtWidgets.QHBoxLayout()
        edit_sc_hbox2 = QtWidgets.QHBoxLayout()
        self.qline_edit1_label = QtWidgets.QLabel()
        self.qline_edit_warn_label = QtWidgets.QLabel()
        self.qline_edit_warn_label2 = QtWidgets.QLabel()
        self.qline_edit_warn_label.setText("Bu alan boş bırakılamaz..")
        self.qline_edit_warn_label.setStyleSheet("background-color:red")
        self.qline_edit_warn_label2.setText("Yalnızca alfabetik karakter giriniz..")
        self.qline_edit_warn_label2.setStyleSheet("background-color:red")
        self.qline_edit1_label.setText("Girmek istediğiniz ürünü yazınız..")
        self.qline_edit1 = QtWidgets.QLineEdit()
        self.qline_edit1_clear_button = QtWidgets.QPushButton("Temizle")
        self.qline_edit1_add_button = QtWidgets.QPushButton("Ekle")

        edit_sc_vbox.addWidget(self.qline_edit1_label)
        edit_sc_vbox.addWidget(self.qline_edit1)
        edit_sc_hbox.addStretch()
        edit_sc_hbox.addWidget(self.qline_edit1_add_button)
        edit_sc_hbox.addWidget(self.qline_edit1_clear_button)
        edit_sc_hbox2.addWidget(self.edit_sc_back_button)
        edit_sc_vbox.addWidget(self.qline_edit_warn_label)
        edit_sc_vbox.addWidget(self.qline_edit_warn_label2)
        self.qline_edit_warn_label2.hide()
        self.qline_edit_warn_label.hide()





        edit_sc_vbox.addLayout(edit_sc_hbox)
        edit_sc_vbox.addStretch(2)
        edit_sc_hbox2.addStretch()
        edit_sc_vbox.addLayout(edit_sc_hbox2)


        edit_sc_vbox.addStretch()


        self.setLayout(edit_sc_vbox)
        self.edit_sc_back_button.clicked.connect(self.back_button_is_clicked)
        self.qline_edit1_clear_button.clicked.connect(self.clear_button_is_clicked)


        self.qline_edit1_add_button.clicked.connect(self.add_button_is_clicked)
    def alpha_test(self,word):
        statement = True
        for letter in word:
            if not letter.isalpha():
                statement = False
        return statement
    def add_button_is_clicked(self):

        if self.qline_edit1.text() == "":
            self.qline_edit_warn_label.show()

        else:
            if not self.alpha_test(self.qline_edit1.text()):
                self.qline_edit_warn_label2.show()
                self.qline_edit_warn_label.hide()
            else:

                self.edit_sc2 = Interface.edit_screen2.edit_screen2(str(self.qline_edit1.text()).upper())
                self.edit_sc2.init_ui()
                self.edit_sc2.show()
                self.hide()











    def clear_button_is_clicked(self):
        if self.sender() == self.qline_edit1_clear_button:
            self.qline_edit1.clear()


    def back_button_is_clicked(self):
        self.init_sc = initial_screen.initial_screen()
        self.hide()




