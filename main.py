import sys
import sqlite3

from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt6 import uic

class Add(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.new_or_change.clicked.connect(self.run)

    def run(self):
        try:
            id = self.line_id.text()
            sort = self.line_sort.text()
            l1 = self.line_obzar.text()
            l2 = self.line_vibor.text()
            l3 = self.line_descr.text()
            l4 = self.line_price.text()
            l5 = self.line_volume.text()
            if l4 == '':
                l4 = 0
            self.con = sqlite3.connect("coffee.sqlite")
            self.cur = self.con.cursor()
            id_tab = self.cur.execute(f"SELECT * FROM coffee WHERE ID = {id}").fetchone()
            if id_tab is None:
                print(f"INSERT INTO coffee(ID, sort, roasting, ground_in_grains, description, price, volume) "
                      f"VALUES({id}, '{sort}', '{l1}', '{l2}', '{l3}', {l4}, '{l5}')")
                self.cur.execute(
                    f"INSERT INTO coffee(ID, sort, roasting, ground_in_grains, description, price, volume) "
                    f"VALUES({id}, '{sort}', '{l1}', '{l2}', '{l3}', {l4}, '{l5}')")
            else:
                print(f"UPDATE coffee "
                      f"set ID = {id}, sort = '{sort}', roasting = '{l1}', ground_in_grains = '{l2}', "
                      f"description = '{l3}', price = {l4}, volume = '{l5}' "
                      f"WHERE ID = {id}")
                self.cur.execute(f"UPDATE coffee "
                                 f"SET ID = {id}, sort = '{sort}', roasting = '{l1}', ground_in_grains = '{l2}', "
                                 f"description = '{l3}', price = {l4}, volume = '{l5}' "
                                 f"WHERE ID = {id}")
            self.con.close()
        except Exception as e:
            print('%s' % e)

class Caputino(QMainWindow):
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
    ex = Caputino()
    es = Add()
    ex.show()
    es.show()
    sys.exit(app.exec())