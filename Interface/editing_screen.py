from PyQt5 import QtWidgets
from Database import database
from Interface import edit_screen
from Interface import show_screen
class editing_screen(QtWidgets.QWidget):

    def __init__(self,id_num,table_name_data):
        super().__init__()
        self.id_num = id_num
        self.table_name_data = table_name_data


    def init_ui(self):

        self.setGeometry(100, 100, 500, 500)

        self.database = database.Database()
        data = self.database.get_data(self.table_name_data)
        print(data)
        self.edit_sc_back_button = QtWidgets.QPushButton("Back")
        self.edit_sc_inital_sc_button = QtWidgets.QPushButton("Main Menu")
        self.qtoolbar = QtWidgets.QDateEdit()
        self.edit_sc_success_label = QtWidgets.QLabel()
        self.edit_sc_warn_label = QtWidgets.QLabel()
        self.edit_sc_warn_label2 = QtWidgets.QLabel()
        self.edit_sc_warn_label2.setText("Enter only numeric values")
        self.edit_sc_warn_label2.setStyleSheet("background-color:red")
        self.edit_sc_success_label.setText("Asset added successfully..")
        self.edit_sc_warn_label.setText("Please fill all fields..")
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
        self.qline_edit1_label1.setText("Enter date..")
        self.qline_edit2_label2.setText("Enter price..")
        self.qline_edit3_label3.setText("Enter quantity..")
        self.qline_edit1_clear_button = QtWidgets.QPushButton("Clear")
        self.edit_button = QtWidgets.QPushButton("Edit")

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
        edit_sc_vbox.addWidget(self.edit_sc_warn_label2)
        self.edit_sc_warn_label2.hide()
        edit_sc_vbox.addWidget(self.edit_sc_success_label)
        self.edit_sc_success_label.hide()
        edit_sc_vbox.addLayout(edit_sc_hbox)
        edit_sc_vbox.addStretch()

        edit_sc_hbox.addWidget(self.edit_button)
        edit_sc_hbox.addWidget(self.qline_edit1_clear_button)

        edit_sc_hbox2.addWidget(self.edit_sc_back_button)
        edit_sc_hbox2.addWidget(self.edit_sc_inital_sc_button)
        self.edit_sc_inital_sc_button.hide()

        edit_sc_vbox.addLayout(edit_sc_hbox)
        edit_sc_vbox.addStretch(2)
        edit_sc_hbox2.addStretch()
        edit_sc_vbox.addLayout(edit_sc_hbox2)

        self.setLayout(edit_sc_vbox)
        self.edit_sc_back_button.clicked.connect(self.back_button_is_clicked)
        self.edit_button.clicked.connect(self.edit_button_is_clicked)



    def back_button_is_clicked(self):
        self.show_sc = show_screen.ShowScreen(self.table_name_data)
        self.show_sc.show()
        self.hide()
    def edit_button_is_clicked(self):

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
            self.database.update_data(self.table_name_data,(self.qtoolbar.text(),self.qline_edit2.text(),self.qline_edit3.text(),self.id_num+1))
            self.show_sc1 = show_screen.ShowScreen(self.table_name_data)
            self.show_sc1.show()
            self.hide()

