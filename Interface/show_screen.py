from PyQt5 import QtWidgets
from PyQt5 import QtGui
from Database import database
from Interface import transition_screen
from Interface import editing_screen
from Interface import initial_screen

class ShowScreen(QtWidgets.QWidget):
    def __init__(self,table):
        self.current_table = table
        super().__init__()
        self.setGeometry(100,100,500,500)
        self.init_ui()
    def init_ui(self):

        database_ = database.Database()
        data = database_.get_data(self.current_table)

        self.show_sc_back_button = QtWidgets.QPushButton("Geri")
        self.edit_button = QtWidgets.QPushButton("Düzenle")
        self.tableWidget = QtWidgets.QTableWidget()
        self.breakeven_label = QtWidgets.QLabel()
        self.breakeven_num_label = QtWidgets.QLabel()
        self.total_cost_label = QtWidgets.QLabel()
        self.total_cost_num_label = QtWidgets.QLabel()
        self.desc_label3 = QtWidgets.QLabel()
        self.breakeven_label.setText("Başabaş noktası:")
        self.breakeven_num_label.setText(str(database_.averager(self.current_table)))
        self.total_cost_label.setText("Toplam maliyet:")
        self.total_cost_label.setFont(QtGui.QFont("",15))
        self.breakeven_label.setFont(QtGui.QFont("", 15))
        self.total_cost_num_label.setText(str(database_.quantity_retriever(self.current_table)))
        self.total_cost_num_label.setFont(QtGui.QFont("", 15))
        self.breakeven_num_label.setFont(QtGui.QFont("", 15))



        self.tableWidget_column_count = 3

        self.tableWidget_Row_count = database_.rows_count(self.current_table)
        self.tableWidget.setColumnCount(self.tableWidget_column_count)
        self.tableWidget.setRowCount(self.tableWidget_Row_count)

        for i in range(0,self.tableWidget_Row_count):
            for j in range(0,self.tableWidget_column_count):
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(data[i][j+1]))
                    self.tableWidget.item(i,j).setFont(QtGui.QFont("Arial",19))



        self.tableWidget.setHorizontalHeaderLabels(["TARİH", "FİYAT", "ALIM MİKTARI"])
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1, 121)
        self.tableWidget.setColumnWidth(2, 121)



        show_sc_vbox = QtWidgets.QVBoxLayout()
        show_sc_hbox = QtWidgets.QHBoxLayout()
        show_sc_hbox2 = QtWidgets.QHBoxLayout()

        show_sc_hbox.addStretch()
        show_sc_hbox.addWidget(self.show_sc_back_button)
        show_sc_vbox.addWidget(self.tableWidget)
        show_sc_vbox.addWidget(self.edit_button)
        show_sc_vbox.addStretch()
        show_sc_hbox2.addWidget(self.total_cost_label)
        show_sc_hbox2.addWidget(self.total_cost_num_label)
        show_sc_hbox2.addWidget(self.breakeven_label)
        show_sc_hbox2.addWidget(self.breakeven_num_label)
        show_sc_vbox.addLayout(show_sc_hbox2)
        show_sc_vbox.addStretch()
        show_sc_vbox.addLayout(show_sc_hbox)
        self.setLayout(show_sc_vbox)
        self.show_sc_back_button.clicked.connect(self.back_button_is_clicked)
        self.edit_button.clicked.connect(self.edit_button_is_clicked)

    def edit_button_is_clicked(self):
        self.editing_sc = editing_screen.editing_screen(self.tableWidget.currentItem().row(),self.current_table)
        print(self.tableWidget.currentItem().row())
        self.editing_sc.init_ui()
        self.editing_sc.show()

        self.hide()
    def back_button_is_clicked(self):
        self.transition_sc = transition_screen.TransitionScreen()
        self.transition_sc.init_ui()
        self.transition_sc.show()
        self.hide()



