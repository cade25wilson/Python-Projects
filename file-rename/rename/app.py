import sys

from PyQt5.QtWidgets import QApplication

from .views import Window

def main():
    # Creating application
    app = QApplication(sys.argv)
    # Creating and showing main window
    win = Window()
    win.show()
    # Run even loop
    sys.exit(app.exec())