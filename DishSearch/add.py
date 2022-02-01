import argparse
import os
import sys
import sqlite3

from PyQt5.QtGui import QPixmap

from add_file import AddWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MyWidget(QMainWindow, AddWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fname = r'.\images\default.jpg'
        self.get_user_name()
        self.search_btn.clicked.connect(self.search_window)
        self.logout_btn.clicked.connect(self.logout)
        self.choose_btn.clicked.connect(self.choose_img)
        self.add_btn.clicked.connect(self.add)

    def get_user_name(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--user_name', type=str)
        parser.add_argument('--name_color', type=str)
        args = parser.parse_args()
        self.user_name = args.user_name
        self.name_color = args.name_color
        self.user.setText(self.user_name)
        self.user.setStyleSheet(f'color: rgb({self.name_color});')

    def logout(self):
        self.close()
        os.system('python autorisation.py')

    def search_window(self):
        self.close()
        req = "None"
        os.system(
            f'python search.py --user_name {self.user_name} --name_color {self.name_color} --req {req}')

    def choose_img(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать изображение', '')[0]
        pixmap = QPixmap(self.fname)
        self.img.setPixmap(pixmap)
        self.img.setScaledContents(True)

    def add(self):
        self.name_war.setVisible(False)
        self.kcal_war.setVisible(False)
        self.mass_war.setVisible(False)
        f = 1
        if self.name.text() == '':
            self.name_war.setVisible(True)
            f = 0

        if (not self.kcal.text().isdigit()) and self.kcal.text() != '':
            self.kcal_war.setVisible(True)
            f = 0
        if len(self.products.text().split('  ')) != len(self.mass.text().split('  ')):
            self.mass_war.setVisible(True)
            f = 0

        if f == 1:
            print('add')
            self.name_war.setVisible(False)
            self.kcal_war.setVisible(False)
            self.mass_war.setVisible(False)
            with sqlite3.connect("db.db") as con:
                cur = con.cursor()
                if self.kcal.text() == '':
                    kcal = -1
                else:
                    kcal = int(self.kcal.text())

                products = '*'.join(self.products.text().split('  '))
                mass = '*'.join(self.mass.text().split('  '))
                cur.execute("INSERT INTO Recipes VALUES(?, ?, ?, ?, ?, ?, ?);",
                            (None, self.name.text(), self.recipe.text(), products,
                             mass, kcal, str(self.fname)))
                con.commit()
                cur.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
