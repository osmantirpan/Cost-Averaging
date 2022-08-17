from PyQt5 import QtWidgets
from Interface import initial_screen
from Interface import show_screen
from Database import database
from Interface import editing_screen
from PyQt5 import QtGui
#########################
class TransitionScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.list_widget = QtWidgets.QListWidget()
        self.database_ = database.Database()
        self.lister()


    def init_ui(self):

        self.setGeometry(100,100,500,500)
        trans_sc_vbox = QtWidgets.QVBoxLayout()
        trans_sc_hbox = QtWidgets.QHBoxLayout()
        trans_sc_hbox2 = QtWidgets.QHBoxLayout()

        self.select_button = QtWidgets.QPushButton("Göster")
        self.delete_button = QtWidgets.QPushButton("Sil")
        self.back_button = QtWidgets.QPushButton("Geri")
        trans_sc_vbox.addWidget(self.list_widget)
        trans_sc_hbox.addStretch()
        trans_sc_hbox.addWidget(self.select_button)
        trans_sc_hbox.addWidget(self.delete_button)
        trans_sc_hbox2.addWidget(self.back_button)

        trans_sc_vbox.addLayout(trans_sc_hbox)
        trans_sc_vbox.addStretch(2)
        trans_sc_hbox2.addStretch()
        trans_sc_vbox.addLayout(trans_sc_hbox2)
        self.setLayout(trans_sc_vbox)
        self.back_button.clicked.connect(self.back_button_is_clicked)
        self.delete_button.clicked.connect(self.delete_button_is_clicked)
        self.select_button.clicked.connect(self.show_screen_initializer)









    def lister(self):
        table_data = self.database_.get_data("tableListExecutionInfo01")
        for item in table_data:
            self.list_widget.addItem(item[0])

    def show_screen_initializer(self):

        selected_value = self.list_widget.currentItem()
        if selected_value == None:
            pass
        else:
            self.show_sc = show_screen.ShowScreen(selected_value.text())
            self.show_sc.show()
            self.hide()




    def back_button_is_clicked(self):
        self.init_sc = initial_screen.initial_screen()
        self.hide()

    def delete_button_is_clicked(self):
        if self.list_widget.currentItem() == None:
            pass

        else:
            self.database_.delete_data(self.list_widget.currentItem().text())
            self.database_.delete_table(self.list_widget.currentItem().text())
            self.list_widget.takeItem(self.list_widget.currentRow())












