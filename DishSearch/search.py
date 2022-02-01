import os
import sys
import sqlite3
import argparse

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtCore

from search_file import SearchWindow


class MyWidget(QMainWindow, SearchWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user_name = ''
        self.name_color = ''
        self.page = 0
        self.req = ''

        self.get_user_name()

        self.logout_btn.clicked.connect(self.logout)
        self.history_btn.clicked.connect(self.history_window)
        self.search_btn.clicked.connect(self.searching)
        self.left_btn.clicked.connect(self.change_page)
        self.right_btn.clicked.connect(self.change_page)
        self.save_btn.clicked.connect(self.save_recipe)
        self.add_btn.clicked.connect(self.add_recipe)

    def get_user_name(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--user_name', type=str)
        parser.add_argument('--name_color', type=str)
        parser.add_argument('--request', type=str)
        args = parser.parse_args()
        self.user_name = args.user_name
        self.name_color = args.name_color
        self.req = args.request
        if self.req == 'None':
            self.req = ''
        self.user.setText(self.user_name)
        self.user.setStyleSheet(f'color: rgb({self.name_color});')
        self.search.setText(self.req)
        self.searching()

    def logout(self):
        self.close()
        os.system('python autorisation.py')

    def history_window(self):
        self.close()
        os.system(
            f'python history.py --user_name {self.user_name} --name_color {self.name_color}')

    def add_recipe(self):
        self.close()
        os.system(
            f'python add.py --user_name {self.user_name} --name_color {self.name_color}')

    def change_page(self):
        if not self.not_found.isVisible():
            if self.sender().text() == '->':
                self.page += 1
            elif self.sender().text() == '<-':
                self.page -= 1
            self.show_data()

    def searching(self):
        self.req = self.search.text()
        self.page = 0
        if ''.join(self.req.split()) != '':
            with sqlite3.connect("db.db") as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Profiles WHERE user_name=?;", (self.user_name,))  # запись в историю
                data = cur.fetchone()
                id1 = data[0]
                cur.execute("SELECT * FROM History WHERE id=?;", (id1,))
                data = cur.fetchone()
                # print(len(data[1].split('*')))
                if len(data[1].split('*')) == 10:
                    text = '*'.join(data[1].split('*')[1:]) + '*' + self.req
                    cur.execute(f"UPDATE History SET dishes = ? WHERE id = ?;", (text, id1,))
                else:
                    if data[1] == '':
                        text = self.req
                    else:
                        text = str(data[1]) + '*' + self.req
                    cur.execute(f"UPDATE History SET dishes = ? WHERE id = ?;", (text, id1,))

                con.commit()
                cur.execute("SELECT * FROM Recipes WHERE name like ?;", ('%' + self.req.lower() + '%',))  # поиск
                data = cur.fetchall()
                print(data)
                con.commit()
                cur.close()
                if len(data) == 0:
                    self.not_found.setVisible(True)
                    self.hide_data()
                else:
                    print('ok')
                    self.not_found.setVisible(False)
                    self.show_data()

    def save_recipe(self):
        products = self.products.text().split('\n')
        mass = self.mass.text().split('\n')
        f = open(f"../{self.name.text()}.txt", 'w')
        print(f"{self.name.text()}", file=f)
        print(' ', file=f)
        print(f"{self.kcal.text()}", file=f)
        print(f"{self.recipe.text()}", file=f)
        print(' ', file=f)
        for i in range(len(products)):
           print(f"{products[i]}   {mass[i]}", file=f)
        f.close()
    def show_data(self):
        with sqlite3.connect("db.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Recipes WHERE name like ?;", ('%' + self.req.lower() + '%',))
            data = cur.fetchall()
            if self.page == len(data):
                self.page = 0
            elif self.page == -1:
                self.page = len(data) - 1

            self.save_btn.setVisible(True)
            pixmap = QPixmap(str(data[self.page][6]))
            self.img.setPixmap(pixmap)
            self.img.setScaledContents(True)
            self.img.setVisible(True)
            self.name.setText(str(data[self.page][1]).capitalize())
            self.recipe.setText(str(data[self.page][2]))
            self.kcal.setText(str(data[self.page][5]) + " ккал")
            products = data[self.page][3].split('*')
            mass = data[self.page][4].split('*')
            self.products.setText('')
            self.mass.setText('')
            for i in range(len(products)):
                self.products.setText(self.products.text() + '\n' + str(products[i]))
                self.mass.setText(self.mass.text() + '\n' + str(mass[i]))

            con.commit()
            cur.close()

    def hide_data(self):
        self.save_btn.setVisible(False)
        self.name.setText('')
        self.recipe.setText('')
        self.products.setText('')
        self.mass.setText('')
        self.kcal.setText('')
        self.img.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
