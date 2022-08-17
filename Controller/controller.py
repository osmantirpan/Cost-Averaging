import Database.database
from Interface import initial_screen
from Interface import edit_screen
from Database import database
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
interface_object = initial_screen.initial_screen()
sys.exit(app.exec_())

