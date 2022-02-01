import os
import sys
import sqlite3

from autorisation_file import AutorisationWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, AutorisationWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_warning = False
        self.log_btn.clicked.connect(self.sign_in)
        self.reg_btn.clicked.connect(self.reg_window)

    def reg_window(self):
        self.close()
        os.system('python registration.py')

    def sign_in(self):
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
                    self.warning.setText("Неверный логин")
                    self.warning.setVisible(True)
                    self.is_warning = True
                elif str(data[2]) != pas:
                    self.warning.setText("Неверный пароль")
                    self.warning.setVisible(True)
                    self.is_warning = True
                else:
                    self.close()
                    con.commit()
                    cur.close()
                    req = 'None'
                    os.system(
                        f'python search.py --user_name {log} --name_color {data[3]} --request {req}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
