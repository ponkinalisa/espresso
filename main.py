import sys
import sqlite3

from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt6 import uic


class Car(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.get.clicked.connect(self.run)

    def run(self):
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        result = self.cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Car()
    ex.show()
    sys.exit(app.exec())