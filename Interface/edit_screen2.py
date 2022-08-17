from PyQt5 import QtWidgets
import Interface.edit_screen
from Interface import edit_screen
from Interface import initial_screen
from Database import database
class edit_screen2(QtWidgets.QWidget):

    def __init__(self,tableNameData):
        super().__init__()
        self.tableNameData = tableNameData






    def init_ui(self):
        self.setGeometry(100, 100, 500, 500)

        self.database = database.Database()
        self.edit_sc_back_button = QtWidgets.QPushButton("Back")
        self.edit_sc_inital_sc_button = QtWidgets.QPushButton("Main Menu")
        self.qtoolbar = QtWidgets.QDateEdit()
        self.edit_sc_success_label = QtWidgets.QLabel()
        self.edit_sc_warn_label = QtWidgets.QLabel()
        self.edit_sc_warn_label2 = QtWidgets.QLabel()
        self.edit_sc_success_label.setText("Asset added successfully..")
        self.edit_sc_warn_label.setText("Please fill all fields..")
        self.edit_sc_warn_label2.setText("Enter only numeric values")
        self.edit_sc_warn_label2.setStyleSheet("background-color:red")
        self.edit_sc_warn_label.setStyleSheet("background-color:red")
        self.edit_sc_success_label.setStyleSheet("background-color:green")
        edit_sc_vbox = QtWidgets.QVBoxLayout()
        edit_sc_hbox = QtWidgets.QHBoxLayout()
        edit_sc_hbox2 = QtWidgets.QHBoxLayout()
        self.qline_edit1_label1 = QtWidgets.QLabel()
        self.qline_edit2_label2 = QtWidgets.QLabel()
        self.qline_edit3_label3 = QtWidgets.QLabel()
        self.qline_edit2 = QtWidgets.QLineEdit()
        self.qline_edit3 = QtWidgets.QLineEdit()
        self.qline_edit1_label1.setText("Enter date")
        self.qline_edit2_label2.setText("Enter price")
        self.qline_edit3_label3.setText("Enter quantity")
        self.qline_edit1_clear_button = QtWidgets.QPushButton("Clear")
        self.qline_edit1_add_button = QtWidgets.QPushButton("Add")

        edit_sc_vbox.addWidget(self.qline_edit1_label1)
        edit_sc_vbox.addWidget(self.qtoolbar)
        edit_sc_hbox.addStretch()

        #########
        edit_sc_vbox.addWidget(self.qline_edit2_label2)
        edit_sc_vbox.addWidget(self.qline_edit2)
        edit_sc_hbox.addStretch()

        #########
        edit_sc_vbox.addWidget(self.qline_edit3_label3)
        edit_sc_vbox.addWidget(self.qline_edit3)
        edit_sc_hbox.addStretch()

        edit_sc_vbox.addWidget(self.edit_sc_warn_label)
        self.edit_sc_warn_label.hide()
        edit_sc_vbox.addWidget(self.edit_sc_success_label)
        self.edit_sc_success_label.hide()
        edit_sc_vbox.addWidget(self.edit_sc_warn_label2)
        self.edit_sc_warn_label2.hide()
        edit_sc_vbox.addLayout(edit_sc_hbox)
        edit_sc_vbox.addStretch()

        edit_sc_hbox.addWidget(self.qline_edit1_add_button)
        edit_sc_hbox.addWidget(self.qline_edit1_clear_button)


        edit_sc_hbox2.addWidget(self.edit_sc_back_button)
        edit_sc_hbox2.addWidget(self.edit_sc_inital_sc_button)
        self.edit_sc_inital_sc_button.hide()


        edit_sc_vbox.addLayout(edit_sc_hbox)
        edit_sc_vbox.addStretch(2)
        edit_sc_hbox2.addStretch()
        edit_sc_vbox.addLayout(edit_sc_hbox2)
        self.edit_sc_obj = edit_screen.edit_screen()








        self.setLayout(edit_sc_vbox)
        self.edit_sc_back_button.clicked.connect(self.back_button_is_clicked)
        self.qline_edit1_add_button.clicked.connect(self.add_button_is_clicked)
        self.qline_edit1_clear_button.clicked.connect(self.clear_button_is_clicked)
        self.edit_sc_inital_sc_button.clicked.connect(self.initial_sc_button_clicked)

    def back_button_is_clicked(self):
        self.edit_screen1 = Interface.edit_screen.edit_screen()
        self.edit_screen1.init_ui()
        self.edit_screen1.show()
        self.hide()
    def add_button_is_clicked(self):
        if self.qtoolbar.text() == "":
            self.edit_sc_warn_label.show()
        elif self.qline_edit2.text() == "":
            self.edit_sc_warn_label.show()
        elif self.qline_edit3.text() == "":
            self.edit_sc_warn_label.show()

        elif self.qline_edit2.text().isnumeric() == False:
            self.edit_sc_warn_label2.show()
            self.edit_sc_warn_label.hide()
        elif self.qline_edit3.text().isnumeric() == False:
            self.edit_sc_warn_label2.show()
            self.edit_sc_warn_label.hide()
        else:
            self.database.add_table_name(self.tableNameData.upper())
            self.database.new_table(self.tableNameData)
            self.tableNameData = self.tableNameData.upper()
            self.database.add_data((self.tableNameData), self.qtoolbar.text(), self.qline_edit2.text(),self.qline_edit3.text())
            self.edit_sc_warn_label.hide()
            self.edit_sc_warn_label2.hide()
            self.edit_sc_success_label.show()
            self.qline_edit1_add_button.hide()
            self.qline_edit1_clear_button.hide()
            self.edit_sc_inital_sc_button.show()



    def initial_sc_button_clicked(self):
        self.initial_sc = initial_screen.initial_screen()
        self.hide()


    def clear_button_is_clicked(self):
        self.qtoolbar.clear()
        self.qline_edit2.clear()
        self.qline_edit3.clear()


