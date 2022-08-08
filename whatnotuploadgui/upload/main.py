import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets, QtGui, QtCore

from database import createConnection
from views import MainWindow, Lists, CreateList, EditList, CreateItem, EditItem

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    window = MainWindow()
    window.createWindow()
