import argparse
import os
import sys
import sqlite3

from history_file import HistoryWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, HistoryWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_user_name()
        self.dishes = [self.dish1, self.dish2, self.dish3, self.dish4, self.dish5, self.dish6, self.dish7, self.dish8,
                       self.dish9, self.dish10]
        self.buttons = [self.search1, self.search2, self.search3, self.search4, self.search5, self.search6,
                        self.search7, self.search8,
                        self.search9, self.search10]
        for i in self.buttons:
            i.clicked.connect(self.search)
        self.history()
        self.search_btn.clicked.connect(self.search_window)
        self.logout_btn.clicked.connect(self.logout)
        self.clean_btn.clicked.connect(self.clean)

    def get_user_name(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--user_name', type=str)
        parser.add_argument('--name_color', type=str)
        args = parser.parse_args()
        self.user_name = args.user_name
        self.name_color = args.name_color
        self.user.setText(self.user_name)
        self.user.setStyleSheet(f'color: rgb({self.name_color});')

    def history(self):
        with sqlite3.connect("db.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Profiles WHERE user_name=?;", (self.user_name,))
            data = cur.fetchone()
            id1 = data[0]
            cur.execute("SELECT * FROM History WHERE id=?;", (id1,))
            data = cur.fetchone()
            data1 = data[1].split('*')
            for i in range(len(data1) - 1, -1, -1):
                self.dishes[len(data1) - i - 1].setText(data1[i])

            con.commit()
            cur.close()

    def search(self):
        self.close()
        req = self.dishes[self.buttons.index(self.sender())].text()
        if req == '_':
            req = "None"
        os.system(
            f'python search.py --user_name {self.user_name} --name_color {self.name_color} --req {req}')

    def search_window(self):
        self.close()
        req = "None"
        os.system(
            f'python search.py --user_name {self.user_name} --name_color {self.name_color} --req {req}')

    def logout(self):
        self.close()
        os.system('python autorisation.py')

    def clean(self):
        with sqlite3.connect("db.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Profiles WHERE user_name=?;", (self.user_name,))
            data = cur.fetchone()
            id1 = data[0]
            cur.execute(f"UPDATE History SET dishes = ? WHERE id = ?;", ('', id1,))
            self.history()
            con.commit()
            cur.close()
        for i in self.dishes:
            i.setText('_')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
