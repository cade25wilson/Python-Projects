import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QToolBar

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Python Menu")
        self.resize(400, 200)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createMenuBar()
        self._createToolBars()
    
    def _createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")
    
    def _createToolBars(self):
        fileToolBar = self.addToolBar("File")
        editToolbar = QToolBar("Edit", self)
        self.addToolBar(editToolbar)
        helpToolbar = QToolBar("Help", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolbar)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())