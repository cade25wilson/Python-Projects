from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

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

    

    