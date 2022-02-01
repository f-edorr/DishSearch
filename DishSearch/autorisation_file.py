# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autorisation.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class AutorisationWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 451)
        MainWindow.setStyleSheet("QPushButton{\n"
"    background-color: rgb(172, 222, 255);\n"
"    border-radius: 5px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.log_btn = QtWidgets.QPushButton(self.centralwidget)
        self.log_btn.setGeometry(QtCore.QRect(220, 230, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.log_btn.setFont(font)
        self.log_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.log_btn.setObjectName("log_btn")
        self.aut = QtWidgets.QLabel(self.centralwidget)
        self.aut.setGeometry(QtCore.QRect(210, 60, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.aut.setFont(font)
        self.aut.setObjectName("aut")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(180, 140, 211, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.login = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.login.setObjectName("login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.login)
        self.log = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.log.setFont(font)
        self.log.setObjectName("log")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.log)
        self.pas = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pas.setFont(font)
        self.pas.setObjectName("pas")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pas)
        self.password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 280, 221, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qst = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.qst.setObjectName("qst")
        self.horizontalLayout.addWidget(self.qst)
        self.reg_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reg_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reg_btn.setObjectName("reg_btn")
        self.horizontalLayout.addWidget(self.reg_btn)
        self.warning = QtWidgets.QLabel(self.centralwidget)
        self.warning.setGeometry(QtCore.QRect(190, 110, 191, 21))
        self.warning.setStyleSheet("color: rgb(255, 0, 0);")
        self.warning.setAlignment(QtCore.Qt.AlignCenter)
        self.warning.setObjectName("warning")
        self.warning.setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.log_btn.setText(_translate("MainWindow", "Войти"))
        self.aut.setText(_translate("MainWindow", "Авторизация"))
        self.log.setText(_translate("MainWindow", "Логин"))
        self.pas.setText(_translate("MainWindow", "Пароль"))
        self.qst.setText(_translate("MainWindow", "Нет аккаунта?"))
        self.reg_btn.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.warning.setText(_translate("MainWindow", "Неверные данные!"))