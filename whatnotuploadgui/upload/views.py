from ctypes import create_string_buffer
import sys
import time
from tkinter import W
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QLayout,
    QWidget,
)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from database import createConnection

class MainWindow(QMainWindow):
    def createWindow(self):
        window = QtWidgets.QWidget()
        window.resize(1100,885)
        window.move(100,100)
        window.setWindowTitle('Upload')

        #font 
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)

        #LABELS

        #categorylabel
        catlabel = QtWidgets.QLabel(window)
        catlabel.setText('Category')
        catlabel.setObjectName('catlabel')
        catlabel.setAlignment(QtCore.Qt.AlignCenter)
        catlabel.setGeometry(QtCore.QRect(130, 40, 271, 51))
        catlabel.setFont(font)
 
        #subcategorylabel left, top, width, height
        sublabel = QtWidgets.QLabel(window)
        sublabel.setText('Sub category')
        sublabel.setObjectName('sublabel')
        sublabel.setAlignment(QtCore.Qt.AlignCenter)
        sublabel.setGeometry(QtCore.QRect(130, 110, 271, 51))
        sublabel.setFont(font)

        #titlelabel
        titlabel = QtWidgets.QLabel(window)
        titlabel.setText('Title')
        titlabel.setObjectName('titlabel')
        titlabel.setAlignment(QtCore.Qt.AlignCenter)
        titlabel.setGeometry(QtCore.QRect(130, 170, 271, 51))
        titlabel.setFont(font)

        #descriptionlabel
        deslabel = QtWidgets.QLabel(window)
        deslabel.setText('Description')
        deslabel.setObjectName('deslabel')
        deslabel.setAlignment(QtCore.Qt.AlignCenter)
        deslabel.setGeometry(QtCore.QRect(130, 250, 271, 51))
        deslabel.setFont(font)

        #quantitylabel
        quanlabel = QtWidgets.QLabel(window)
        quanlabel.setText('Quantity')
        quanlabel.setObjectName("quanlabel")
        quanlabel.setAlignment(QtCore.Qt.AlignCenter)
        quanlabel.setGeometry(QtCore.QRect(130, 370, 271, 51))
        quanlabel.setFont(font)

        #typelabel
        typelabel = QtWidgets.QLabel(window)
        typelabel.setText('Type')
        typelabel.setObjectName("typelabel")
        typelabel.setAlignment(QtCore.Qt.AlignCenter)
        typelabel.setGeometry(QtCore.QRect(130, 420, 271, 51))
        typelabel.setFont(font)

        #pricelabel
        prilabel = QtWidgets.QLabel(window)
        prilabel.setText('Price (If BIN)')
        prilabel.setObjectName("prilabel")
        prilabel.setAlignment(QtCore.Qt.AlignCenter)
        prilabel.setGeometry(QtCore.QRect(140, 490, 271, 51))
        prilabel.setFont(font)

        #shiplabel
        shiplabel = QtWidgets.QLabel(window)
        shiplabel.setText('Shipping Profile')
        shiplabel.setObjectName("shiplabel")
        shiplabel.setAlignment(QtCore.Qt.AlignCenter)
        shiplabel.setGeometry(QtCore.QRect(140, 550, 271, 51))
        shiplabel.setFont(font)

        #COMBOBOXES

        font.setPointSize(14)
        font.setBold(False)
        font.setFamilies(['MS Shell Dlg 2'])

        #categorycombobox
        catcombobox = QtWidgets.QComboBox(window)
        catcombobox.setEnabled(True)
        catcombobox.setGeometry(QtCore.QRect(440, 40, 631, 51))
        catcombobox.setObjectName("catcombobox")
        catcombobox.addItem("Vintage & Thrift Clothing")
        catcombobox.addItem("Sneakers & Streetwear")
        catcombobox.addItem("Bags, Jewelry & Accessories")
        catcombobox.addItem("Watches")
        catcombobox.addItem("Toys")
        catcombobox.addItem("Electronics")
        catcombobox.addItem("Arts & Crafts")
        catcombobox.setFont(font)

        #subcategorycombobox
        subcombobox = QtWidgets.QComboBox(window)
        subcombobox.setGeometry(QtCore.QRect(440, 110, 631, 51))
        subcombobox.setObjectName("subcombobox")
        subcombobox.addItem("Crafts")
        subcombobox.addItem("Streetwear")
        subcombobox.addItem("Sneakers")
        subcombobox.addItem("Vintage Clothing")
        subcombobox.addItem("Women\'s Modern & Thrift")
        subcombobox.addItem("Men\'s Modern & Thrift")
        subcombobox.addItem("Kids\' Clothing")
        subcombobox.addItem("Other Fashion")
        subcombobox.addItem("Luxury Bags & Accessories")
        subcombobox.addItem("Fashion & Thrift Bags")
        subcombobox.addItem("Watches")
        subcombobox.addItem("Jewelry")
        subcombobox.addItem("Other Accessories")
        subcombobox.addItem("Vintage Decor")
        subcombobox.setFont(font)

        #typecombobox
        titlecombobox = QtWidgets.QComboBox(window)
        titlecombobox.setGeometry(QtCore.QRect(660, 440, 411, 41))
        titlecombobox.setObjectName("titlecombobox")
        titlecombobox.addItem("Auction")
        titlecombobox.addItem("Buy it Now")
        titlecombobox.setFont(font)

        #shipcombobox
        shipcombobox = QtWidgets.QComboBox(window)
        shipcombobox.setGeometry(QtCore.QRect(440, 560, 631, 41))
        shipcombobox.setObjectName("shipcombobox")
        shipcombobox.addItem("4-7 oz (Comic, Fat Pack, T-Shirt)")
        shipcombobox.addItem("8-11 oz (Funko Pop)")
        shipcombobox.addItem("12-15 oz")
        shipcombobox.addItem("1lb (2/3 Pack Funko Pop)")
        shipcombobox.addItem("1-2 lbs (e.g., BearBrick, Hoodie)")
        shipcombobox.setFont(font)

        #TEXTBOXES

        #tittextbox
        titedit = QtWidgets.QTextEdit(window)
        titedit.setGeometry(QtCore.QRect(440, 180, 631, 51))
        titedit.setObjectName("titedit")

        #desctextbox
        descedit = QtWidgets.QTextEdit(window)
        descedit.setGeometry(QtCore.QRect(440, 250, 631, 101))
        descedit.setObjectName("descedit")


        #pritextbox
        priedit = QtWidgets.QTextEdit(window)
        priedit.setEnabled(True)
        priedit.setGeometry(QtCore.QRect(940, 500, 131, 41))
        priedit.setObjectName("priedit")
        priedit.setFont(font)

        #dollartextbox
        font.setWeight(400)
        font.setBold(False)
        dollaredit = QtWidgets.QTextEdit(window)
        dollaredit.setGeometry(QtCore.QRect(910, 500, 31, 41))
        dollaredit.setObjectName("dollaredit")
        dollaredit.setText("$")
        dollaredit.setFont(font)

        #SPINBOXES

        #quantityspinbox
        quanspinbox = QtWidgets.QSpinBox(window)
        quanspinbox.setGeometry(QtCore.QRect(950, 370, 121, 51))
        quanspinbox.setObjectName("quanspinbox")

        #BUTTONS

        #viewbutton
        viewbutton = QtWidgets.QPushButton(window)
        viewbutton.setEnabled(True)
        viewbutton.setGeometry(QtCore.QRect(130, 650, 241, 81))
        viewbutton.setObjectName("viewbutton")
        viewbutton.setText("View List")
        viewbutton.setFont(font)

        #newbutton
        newbutton = QtWidgets.QPushButton(window)
        newbutton.setEnabled(True)
        newbutton.setGeometry(QtCore.QRect(470, 650, 241, 81))
        newbutton.setObjectName("newbtton")
        newbutton.setText("New List")
        newbutton.setFont(font)
        newbutton.clicked.connect(self.openNewList)

        #savebutton
        savebutton = QtWidgets.QPushButton(window)
        savebutton.setEnabled(True)
        savebutton.setGeometry(QtCore.QRect(830, 650, 241, 81))
        savebutton.setObjectName("savebutton")
        savebutton.setText("Save List")
        savebutton.setFont(font)

        window.show()
        sys.exit(app.exec_())

    def openNewList(self):
        newlist = CreateList(self)
        newlist.show()

class CreateList(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        #SETUP WINDOW
        window = self
        window.setWindowTitle("Create List")
        window.resize(550, 150)

        #BUTTONS
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setFamilies(['MS Shell Dlg 2'])

        #addbutton
        addbutton = QtWidgets.QPushButton(window)
        addbutton.setEnabled(True)
        addbutton.setGeometry(QtCore.QRect(400, 88, 125, 51))  
        addbutton.setObjectName("addbutton")
        addbutton.setText("Add")
        addbutton.setFont(font)
        addbutton.clicked.connect(self.addItem)

        #cancelbutton
        cancelbutton = QtWidgets.QPushButton(window)
        cancelbutton.setEnabled(True)
        cancelbutton.setGeometry(QtCore.QRect(250, 88, 125, 51))
        cancelbutton.setObjectName("cancelbutton")
        cancelbutton.setText("Cancel")
        cancelbutton.setFont(font)
        cancelbutton.clicked.connect(self.close)

        #TEXTBOXES
        #nameTEXTBOX
        self.nametextbox = QtWidgets.QTextEdit(window)
        self.nametextbox.setGeometry(QtCore.QRect(300, 27, 200, 51))
        self.nametextbox.setObjectName("nametextbox")
        self.nametextbox.setFont(font)
        
        #LABELS
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)

        #namelabel
        self.namelabel = QtWidgets.QLabel(window)
        self.namelabel.setText('Name:')
        self.namelabel.setObjectName('namelabel')
        self.namelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.namelabel.setGeometry(QtCore.QRect(20, 20, 150, 51))
        self.namelabel.setFont(font)

        #errorlabel
        self.errorlabel = QtWidgets.QLabel(window)
        self.errorlabel.setText('Error: List name already exists')
        self.errorlabel.setObjectName('errorlabel')
        self.errorlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorlabel.setGeometry(QtCore.QRect(10, 155, 525, 51))
        self.setFont(font)
        self.errorlabel.setVisible(False)

        #successlabel
        self.successlabel = QtWidgets.QLabel(window)
        self.successlabel.setText('Success: List created')
        self.successlabel.setObjectName('successlabel')
        self.successlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.successlabel.setGeometry(QtCore.QRect(10, 155, 525, 51))
        self.setFont(font)
        self.successlabel.setVisible(False)


    def addItem(self):
        list = self.nametextbox.toPlainText()
        createTableQuery = QSqlQuery()
        tables = createTableQuery.exec('SELECT name from sqlite_master where type="table"')
        createTableQuery.record()
        print(createTableQuery.record().value(0))
        while createTableQuery.next():
            print(createTableQuery.value(0))
            if list == createTableQuery.value(0):
                print("List already exists")
                self.errorlabel.setVisible(True)
                CreateList.resize(self, 550, 225)
                self.nametextbox.clear()
                return
        createTableQuery.exec('CREATE TABLE ' + list + ' (name TEXT, description TEXT, quantity INTEGER, price REAL)')
        self.successlabel.setVisible(True)
        CreateList.resize(self, 550, 225)
        time.sleep(1)
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    window = MainWindow()
    window.createWindow()




            