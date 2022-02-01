import os
import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog
from registration_file import RegistrationWindow


class MyWidget(QMainWindow, RegistrationWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.reg_btn.clicked.connect(self.create_profile)
        self.log_btn.clicked.connect(self.login_window)
        self.color_select.clicked.connect(self.color_picker)
        self.is_warning = False
        self.red = 172
        self.green = 222
        self.blue = 255

    def login_window(self):
        self.close()
        os.system('python autorisation.py')

    def color_picker(self):
        color = QColorDialog.getColor()
        self.red = color.red()
        self.green = color.green()
        self.blue = color.blue()
        self.color.setStyleSheet(f"background-color: rgb({self.red}, {self.green}, {self.blue}); border-radius: 5px;")

    def create_profile(self):
        log = self.login.text()
        pas = self.password.text()
        if pas == "" or log == "":
            self.warning.setText("Логин и пароль не могут быть пустыми")
            self.warning.setVisible(True)
            self.is_warning = True
        else:
            with sqlite3.connect("db.db") as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Profiles WHERE user_name=?", (log,))
                data = cur.fetchone()
                if not data:
                    cur.execute("INSERT INTO Profiles VALUES(?, ?, ?, ?);",
                                (None, log, pas, f"{self.red},{self.green},{self.blue}"))
                    cur.execute("SELECT * FROM Profiles WHERE user_name=?", (log,))
                    data = cur.fetchone()
                    # print(data[0])
                    cur.execute("INSERT INTO History VALUES(?, ?);",
                                (data[0], ''))
                    con.commit()
                    cur.close()
                    self.close()
                    req = "None"
                    os.system(
                        f'python search.py --user_name {log} --name_color {f"{self.red},{self.green},{self.blue}"} --req {req}')
                else:
                    self.warning.setText("Этот логин уже занят")
                    self.warning.setVisible(True)
                    self.is_warning = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
