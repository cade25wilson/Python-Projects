import csv
from ctypes import create_string_buffer
from operator import contains
from socket import create_connection
import sqlite3
import sys
import time
from tkinter import W
from unicodedata import category
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

        #ListLabel
        self.listlabel = QtWidgets.QLabel(window)
        self.listlabel.setText('Select List:')
        self.listlabel.setObjectName('listlabel')
        self.listlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.listlabel.setGeometry(QtCore.QRect(130, 30, 271, 51))
        self.listlabel.setFont(font)

        #categorylabel
        self.catlabel = QtWidgets.QLabel(window)
        self.catlabel.setText('Category')
        self.catlabel.setObjectName('catlabel')
        self.catlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.catlabel.setGeometry(QtCore.QRect(130, 100, 271, 51))
        self.catlabel.setFont(font)
 
        #subcategorylabel left, top, width, height
        self.sublabel = QtWidgets.QLabel(window)
        self.sublabel.setText('Sub category')
        self.sublabel.setObjectName('sublabel')
        self.sublabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sublabel.setGeometry(QtCore.QRect(130, 170, 271, 51))
        self.sublabel.setFont(font)

        #titlelabel
        self.titlabel = QtWidgets.QLabel(window)
        self.titlabel.setText('Title')
        self.titlabel.setObjectName('titlabel')
        self.titlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titlabel.setGeometry(QtCore.QRect(130, 230, 271, 51))
        self.titlabel.setFont(font)

        #descriptionlabel
        self.deslabel = QtWidgets.QLabel(window)
        self.deslabel.setText('Description')
        self.deslabel.setObjectName('deslabel')
        self.deslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.deslabel.setGeometry(QtCore.QRect(130, 310, 271, 51))
        self.deslabel.setFont(font)

        #quantitylabel
        self.quanlabel = QtWidgets.QLabel(window)
        self.quanlabel.setText('Quantity')
        self.quanlabel.setObjectName("quanlabel")
        self.quanlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.quanlabel.setGeometry(QtCore.QRect(130, 420, 271, 51))
        self.quanlabel.setFont(font)

        #typelabel
        self.typelabel = QtWidgets.QLabel(window)
        self.typelabel.setText('Type')
        self.typelabel.setObjectName("typelabel")
        self.typelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.typelabel.setGeometry(QtCore.QRect(130, 480, 271, 51))
        self.typelabel.setFont(font)

        #pricelabel
        self.prilabel = QtWidgets.QLabel(window)
        self.prilabel.setText('Price (If BIN)')
        self.prilabel.setObjectName("prilabel")
        self.prilabel.setAlignment(QtCore.Qt.AlignCenter)
        self.prilabel.setGeometry(QtCore.QRect(140, 550, 271, 51))
        self.prilabel.setFont(font)

        #shiplabel
        self.shiplabel = QtWidgets.QLabel(window)
        self.shiplabel.setText('Shipping Profile')
        self.shiplabel.setObjectName("shiplabel")
        self.shiplabel.setAlignment(QtCore.Qt.AlignCenter)
        self.shiplabel.setGeometry(QtCore.QRect(140, 610, 271, 51))
        self.shiplabel.setFont(font)

        #COMBOBOXES

        font.setPointSize(14)
        font.setBold(False)
        font.setFamilies(['MS Shell Dlg 2'])

        #listcombobox
        self.listcombobox = QtWidgets.QComboBox(window)
        self.listcombobox.setEnabled(True)
        self.listcombobox.setGeometry(QtCore.QRect(440, 30, 631, 51))
        self.listcombobox.setObjectName("listcombobox")

        createTableQuery = QSqlQuery()
        createTableQuery.exec('SELECT name from sqlite_master where type="table"')
        while createTableQuery.next():
            self.listcombobox.addItem(createTableQuery.value(0))
        self.listcombobox.setFont(font)

        #categorycombobox
        self.catcombobox = QtWidgets.QComboBox(window)
        self.catcombobox.setEnabled(True)
        self.catcombobox.setGeometry(QtCore.QRect(440, 100, 631, 51))
        self.catcombobox.setObjectName("catcombobox")
        self.catcombobox.addItem("Vintage & Thrift Clothing")
        self.catcombobox.addItem("Sneakers & Streetwear")
        self.catcombobox.addItem("Bags, Jewelry & Accessories")
        self.catcombobox.addItem("Watches")
        self.catcombobox.addItem("Toys")
        self.catcombobox.addItem("Electronics")
        self.catcombobox.addItem("Arts & Crafts")
        self.catcombobox.setFont(font)

        #subcategorycombobox
        self.subcombobox = QtWidgets.QComboBox(window)
        self.subcombobox.setGeometry(QtCore.QRect(440, 170, 631, 51))
        self.subcombobox.setObjectName("subcombobox")
        self.subcombobox.addItem("Crafts")
        self.subcombobox.addItem("Streetwear")
        self.subcombobox.addItem("Sneakers")
        self.subcombobox.addItem("Vintage Clothing")
        self.subcombobox.addItem("Women\'s Modern & Thrift")
        self.subcombobox.addItem("Men\'s Modern & Thrift")
        self.subcombobox.addItem("Kids\' Clothing")
        self.subcombobox.addItem("Other Fashion")
        self.subcombobox.addItem("Luxury Bags & Accessories")
        self.subcombobox.addItem("Fashion & Thrift Bags")
        self.subcombobox.addItem("Watches")
        self.subcombobox.addItem("Jewelry")
        self.subcombobox.addItem("Other Accessories")
        self.subcombobox.addItem("Vintage Decor")
        self.subcombobox.setFont(font)

        #typecombobox
        self.titlecombobox = QtWidgets.QComboBox(window)
        self.titlecombobox.setGeometry(QtCore.QRect(660, 500, 411, 41))
        self.titlecombobox.setObjectName("titlecombobox")
        self.titlecombobox.addItem("Auction")
        self.titlecombobox.addItem("Buy it Now")
        self.titlecombobox.setFont(font)

        #shipcombobox
        self.shipcombobox = QtWidgets.QComboBox(window)
        self.shipcombobox.setGeometry(QtCore.QRect(440, 620, 631, 41))
        self.shipcombobox.setObjectName("shipcombobox")
        self.shipcombobox.addItem("4-7 oz (Comic, Fat Pack, T-Shirt)")
        self.shipcombobox.addItem("8-11 oz (Funko Pop)")
        self.shipcombobox.addItem("12-15 oz")
        self.shipcombobox.addItem("1lb (2/3 Pack Funko Pop)")
        self.shipcombobox.addItem("1-2 lbs (e.g., BearBrick, Hoodie)")
        self.shipcombobox.setFont(font)

        #TEXTBOXES

        #tittextbox
        self.titedit = QtWidgets.QTextEdit(window)
        self.titedit.setGeometry(QtCore.QRect(440, 240, 631, 51))
        self.titedit.setObjectName("titedit")

        #desctextbox
        self.descedit = QtWidgets.QTextEdit(window)
        self.descedit.setGeometry(QtCore.QRect(440, 310, 631, 101))
        self.descedit.setObjectName("descedit")


        #pritextbox
        self.priedit = QtWidgets.QTextEdit(window)
        self.priedit.setEnabled(True)
        self.priedit.setGeometry(QtCore.QRect(940, 560, 131, 41))
        self.priedit.setObjectName("priedit")
        self.priedit.setFont(font)

        #dollartextbox
        font.setWeight(400)
        font.setBold(False)
        self.dollaredit = QtWidgets.QTextEdit(window)
        self.dollaredit.setGeometry(QtCore.QRect(910, 560, 31, 41))
        self.dollaredit.setObjectName("dollaredit")
        self.dollaredit.setText("$")
        self.dollaredit.setFont(font)

        #SPINBOXES

        #quantityspinbox
        self.quanspinbox = QtWidgets.QSpinBox(window)
        self.quanspinbox.setGeometry(QtCore.QRect(950, 430, 121, 51))
        self.quanspinbox.setObjectName("quanspinbox")
        self.quanspinbox.setMinimum(1)
        self.quanspinbox.setValue(1)
        #BUTTONS

        #viewbutton
        self.viewbutton = QtWidgets.QPushButton(window)
        self.viewbutton.setEnabled(True)
        self.viewbutton.setGeometry(QtCore.QRect(130, 710, 241, 81))
        self.viewbutton.setObjectName("viewbutton")
        self.viewbutton.setText("View Lists")
        self.viewbutton.setFont(font)
        self.viewbutton.clicked.connect(self.chooseList)

        #newbutton
        self.newbutton = QtWidgets.QPushButton(window)
        self.newbutton.setEnabled(True)
        self.newbutton.setGeometry(QtCore.QRect(470, 710, 241, 81))
        self.newbutton.setObjectName("newbtton")
        self.newbutton.setText("New List")
        self.newbutton.setFont(font)
        self.newbutton.clicked.connect(self.openNewList)

        #savebutton
        self.savebutton = QtWidgets.QPushButton(window)
        self.savebutton.setEnabled(True)
        self.savebutton.setGeometry(QtCore.QRect(830, 710, 241, 81))
        self.savebutton.setObjectName("savebutton")
        self.savebutton.setText("Save To List")
        self.savebutton.setFont(font)
        self.savebutton.clicked.connect(self.saveToList)

        window.show()
        sys.exit(app.exec_())

    def openNewList(self):
        newlist = CreateList(self)
        newlist.show()

    def chooseList(self):
        chooselist = Lists(self)
        chooselist.show()

    def saveToList(self):
        list = self.listcombobox.currentText()
        category = self.catcombobox.currentText()
        subcategory = self.subcombobox.currentText()
        title = self.titedit.toPlainText()
        desc = self.descedit.toPlainText()
        price = self.priedit.toPlainText()
        quantity = self.quanspinbox.value()
        type = self.titlecombobox.currentText()
        ship = self.shipcombobox.currentText()
        print(list, category, subcategory, title, desc, price, quantity, type, ship)
        #insert into contacts database
        if list and category and subcategory and title and desc and price and quantity and type and ship:
            conn = sqlite3.connect('contacts.sqlite')
            cur = conn.cursor()
            cur.execute("INSERT INTO " + list +  " VALUES (?,?,?,?,?,?,?,?)", (category, subcategory, title, desc, price, quantity, type, ship))
            conn.commit()
            self.titedit.clear()
            self.descedit.clear()
            self.quanspinbox.setValue(1)
            self.priedit.clear()
        else: 
            print("Please fill out all fields")
            self.error = QtWidgets.QMessageBox()
            self.error.setText("Please fill out all fields")
            self.error.exec_()
        

class Lists(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        window = self
        window.setWindowTitle("View Lists")
        window.resize(550, 150)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setFamilies(['MS Shell Dlg 2'])

        #LIST COMBOBOX
        self.listcombobox = QtWidgets.QComboBox(window)
        self.listcombobox.setGeometry(QtCore.QRect(10, 10, 531, 51))
        self.listcombobox.setObjectName("listcombobox")
        self.listcombobox.setFont(font)
        createTableQuery = QSqlQuery()
        createTableQuery.exec('SELECT name from sqlite_master where type="table"')
        while createTableQuery.next():
            self.listcombobox.addItem(createTableQuery.value(0))
        self.listcombobox.setFont(font)

        #BUTTONS
        self.viewbutton = QtWidgets.QPushButton(window)
        self.viewbutton.setEnabled(True)
        self.viewbutton.setGeometry(QtCore.QRect(342, 80, 200, 51))
        self.viewbutton.setObjectName("csvbutton")
        self.viewbutton.setText("Export To CSV")
        self.viewbutton.setFont(font)
        self.viewbutton.clicked.connect(self.exportToCsv)

        self.listbutton = QtWidgets.QPushButton(window)
        self.listbutton.setEnabled(True)
        self.listbutton.setGeometry(QtCore.QRect(10, 80, 200, 51))
        self.listbutton.setObjectName("Listbutton")
        self.listbutton.setText("Edit List")
        self.listbutton.setFont(font)
        self.listbutton.clicked.connect(self.clearui)

    def exportToCsv(self):
        list = self.listcombobox.currentText()
        conn = sqlite3.connect('contacts.sqlite')
        cur = conn.cursor()
        cur.execute("SELECT * FROM " + list)
        with open('csv/' + list + ".csv", 'w') as f:
            writer = csv.writer(f)
            writer.writerow([i[0] for i in cur.description])
            writer.writerows(cur.fetchall())
        conn.close()
        self.error = QtWidgets.QMessageBox()
        self.error.setText("Exported to " + list + ".csv")
        self.error.exec_()

    #resize the windows to fit the master window
    def clearui(self, event):
        self.resize(1000, 1000)
        self.setFixedSize(self.size())





class CreateList(QMainWindow, QSqlDatabase):
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
        combo = window.listcombobox
        list = self.nametextbox.toPlainText()
        createTableQuery = QSqlQuery()
        tables = createTableQuery.exec('SELECT name from sqlite_master where type="table"')
        createTableQuery.record()
        print(createTableQuery.record().value(0))
        while createTableQuery.next():
            print(createTableQuery.value(0))
            if list == createTableQuery.value(0):
                print("List already exists")
                self.error = QtWidgets.QMessageBox()
                self.error.setText("List already exists")
                self.error.exec_()
                self.nametextbox.clear()
                return
        conn = sqlite3.connect('contacts.sqlite')
        cur = conn.cursor()
        if list.__contains__('"'):
            cur.execute("CREATE TABLE " + list  + " ('Category' Text, 'Sub Category' TEXT, 'Title' Text, 'Description' Text, 'Quantity' Text, 'Type' Text, 'Price (If BIN)' Text, 'Shipping Profile' Text)")
            conn.commit()   
            print("List created")
            combo.addItem(list) 
        else:
            cur.execute("CREATE TABLE " + '"' + list + '"' + " ('Category' Text, 'Sub Category' TEXT, 'Title' Text, 'Description' Text, 'Quantity' Text, 'Type' Text, 'Price (If BIN)' Text, 'Shipping Profile' Text)")
            conn.commit()   
            print("List created")
            combo.addItem(list)
        self.close()

class database(QMainWindow, QSqlDatabase):
    def createConnection():
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("contacts.sqlite")
        con.open()
        createtable = QSqlQuery()
        createtable.exec_("CREATE TABLE IF NOT EXISTS contacts"
        """(
        "Category"	TEXT,
            "Sub Category"	TEXT,
            "Title"	TEXT,
            "Description"	TEXT,
            "Quantity"	TEXT,
            "Type"	TEXT,
            "Price (If BIN)"	TEXT,
            "Shipping Profile"	TEXT
        )"""
        )
        if not con.open():
            QMessageBox.critical(
                None,
                "QTableView Example - Error!",
                "Database Error: %s" % con.lastError().databaseText(),
            )
            return False
        return True


if __name__ == "__main__":
    import sys
    create_connection = database.createConnection()
    app = QtWidgets.QApplication(sys.argv)
    if not create_connection:
        sys.exit(1)
    window = MainWindow()
    window.createWindow()




            