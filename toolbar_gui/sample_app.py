import sys
import qrc_resources

from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QToolBar, QAction, QSpinBox
from functools import partial

newIcon = QIcon(":file-new.svg")
class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.setWindowTitle("Python Menu")
        self.resize(400, 200)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createActions()
        self._createMenuBar()
        self._createToolBars()
        self._connectActions()
        self._createStatusBar()
    
    def _createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        self.openRecentMenu = fileMenu.addMenu("Open Recent")
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
        self.fontSizeSpinBox = QSpinBox()
        self.fontSizeSpinBox.setFocusPolicy(Qt.NoFocus)
        editToolbar.addWidget(self.fontSizeSpinBox)

    def _createActions(self):
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.newAction.setIcon(QIcon(":file-new.svg"))
        self.openAction = QAction(QIcon(":file-open.svg"),"&Open", self)
        self.saveAction = QAction(QIcon(":file-save.svg"),"&Save", self)
        self.newAction.setShortcut("Ctrl+N")
        self.openAction.setShortcut("Ctrl+O")
        self.saveAction.setShortcut("Ctrl+S")
        newTip = "Create a new file"
        self.newAction.setStatusTip(newTip)
        self.newAction.setToolTip(newTip)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction(QIcon(":edit-copy.svg"),"&Copy", self)
        self.pasteAction = QAction(QIcon(":edit-paste.svg"),"&Paste", self)
        self.cutAction = QAction(QIcon(":edit-cut.svg"), "C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)
        self.copyAction.setShortcut(QKeySequence.Copy)
        self.pasteAction.setShortcut(QKeySequence.Paste)
        self.cutAction.setShortcut(QKeySequence.Cut)

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

    def newFile(self):
        self.centralWidget.setText("<b>File > New</b> clicked")

    def openFile(self):
        self.centralWidget.setText("<b>File > Open...</b> clicked")

    def saveFile(self):
        self.centralWidget.setText("<b>File > Save</b> clicked")
        
    def copyContent(self):
        self.centralWidget.setText("<b>Edit > Copy</b> clicked")

    def pasteContent(self):
        self.centralWidget.setText("<b>Edit > Paste</b> clicked")

    def cutContent(self):
        self.centralWidget.setText("<b>Edit > Cut</b> clicked")

    def helpContent(self):
        self.centralWidget.setText("<b>Help > Help Content...</b> clicked")

    def about(self):
        self.centralWidget.setText("<b>Help > About...</b> clicked")

    def _connectActions(self):
        self.newAction.triggered.connect(self.newFile)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.close)
        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)
        self.helpContentAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)
        self.openRecentMenu.aboutToShow.connect(self.populateOpenRecent)

    def populateOpenRecent(self):
        self.openRecentMenu.clear()
        actions = []
        filenames = [f"File-{n}" for n in range(5)]
        for filename in filenames:
            action = QAction(filename, self)
            action.triggered.connect(partial(self.openRecentFile, filename))
            actions.append(action)
        self.openRecentMenu.addActions(actions)

    def openRecentFile(self, filename):
        self.centralWidget.setText(f"<b>{filename}</b> opened")

    def _createStatusBar(self):
        self.statusBar = self.statusBar()
        self.statusBar.showMessage("Ready", 3000)
        self.wcLabel = QLabel(f"{self.getWordCount()} Words")
        self.statusBar.addPermanentWidget(self.wcLabel)
        self.ccLabel = QLabel(f"{self.getCharCount()} Chars")
        self.statusBar.addPermanentWidget(self.ccLabel)

    def getWordCount(self):
        return 42

    def getCharCount(self):
        return 4853

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())