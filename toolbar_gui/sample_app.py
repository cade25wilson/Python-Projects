import sys
import qrc_resources

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QToolBar, QAction, QSpinBox

newIcon = QIcon(":file-new.svg")
separator = QAction()
separator.setSeparator(True)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Menu")
        self.resize(400, 200)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createActions()
        self._createMenuBar()
        self._createToolBars()
       # self._createContextMenu()
    
    def _createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        editMenu.addSeparator()
        findMenu = editMenu.addMenu("Find and replace")
        findMenu.addAction("Find...")
        findMenu.addAction("Replace")
        helpMenu = menuBar.addMenu(QIcon(":help-content.svg"), "&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def _createToolBars(self):
        fileToolBar = self.addToolBar("File")
        fileToolBar.setMovable(False)
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        editToolbar = QToolBar("Edit", self)
        self.addToolBar(editToolbar)
        editToolbar.addAction(self.copyAction)
        editToolbar.addAction(self.pasteAction)
        editToolbar.addAction(self.cutAction)
        helpToolbar = QToolBar("Help", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolbar)
        self.fontSizeSpinBox = QSpinBox()
        self.fontSizeSpinBox.setFocusPolicy(Qt.NoFocus)
        editToolbar.addWidget(self.fontSizeSpinBox)

    def _createActions(self):
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.newAction.setIcon(QIcon(":file-new.svg"))
        self.openAction = QAction(QIcon(":file-open.svg"),"&Open", self)
        self.saveAction = QAction(QIcon(":file-save.svg"),"&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction(QIcon(":edit-copy.svg"),"&Copy", self)
        self.pasteAction = QAction(QIcon(":edit-paste.svg"),"&Paste", self)
        self.cutAction = QAction(QIcon(":edit-cut.svg"), "C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)

    def contextMenuEvent(self, event):
        menu = QMenu(self.centralWidget)
        menu.addAction(self.newAction)
        menu.addAction(self.openAction)
        menu.addAction(self.saveAction)
        separator = QAction(self)
        separator.setSeparator(True)
        menu.addAction(separator)
        menu.addAction(self.copyAction)
        menu.addAction(self.pasteAction)
        menu.addAction(self.cutAction)
        menu.exec(event.globalPos())
        
"""    def _createContextMenu(self):
        self.centralWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.centralWidget.addAction(self.newAction)
        self.centralWidget.addAction(self.openAction)
        self.centralWidget.addAction(self.saveAction)
        self.centralWidget.addAction(self.copyAction)
        self.centralWidget.addAction(self.pasteAction)
        self.centralWidget.addAction(self.cutAction)"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())