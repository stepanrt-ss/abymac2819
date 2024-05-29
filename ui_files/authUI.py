# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth_buyer.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(500, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 600))
        self.frame.setStyleSheet("background:qlineargradient(spread:reflect, x1:0.962682, y1:0, x2:0, y2:1, stop:0 rgba(201, 85, 19, 255), stop:1 rgba(67, 28, 6, 255))")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.input_login = QtWidgets.QLineEdit(self.frame)
        self.input_login.setGeometry(QtCore.QRect(130, 190, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_login.setFont(font)
        self.input_login.setStyleSheet("QLineEdit {\n"
"    background: rgb(224, 131, 61);\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    border-radius: 5px;\n"
"    font-size: 14;\n"
"    padding: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(219, 123, 53);\n"
"}")
        self.input_login.setObjectName("input_login")
        self.input_password = QtWidgets.QLineEdit(self.frame)
        self.input_password.setGeometry(QtCore.QRect(130, 240, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_password.setFont(font)
        self.input_password.setStyleSheet("QLineEdit {\n"
"    background: rgb(224, 131, 61);\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    border-radius: 5px;\n"
"    font-size: 14;\n"
"    padding: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(219, 123, 53);\n"
"}")
        self.input_password.setObjectName("input_password")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: none;\n"
"color: white")
        self.label_2.setObjectName("label_2")
        self.accept_btn = QtWidgets.QPushButton(self.frame)
        self.accept_btn.setGeometry(QtCore.QRect(130, 290, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.accept_btn.setFont(font)
        self.accept_btn.setStyleSheet("QPushButton {\n"
"    background: rgb(224, 131, 61);\n"
"    border: 30px;\n"
"    border-radius: 15px;\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(255, 180, 94);\n"
"    border: 30px;\n"
"    border-radius: 15px;\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: rgb(152, 65, 14);\n"
"    border: 30px;\n"
"    border-radius: 15px;\n"
"    color: white\n"
"}")
        self.accept_btn.setObjectName("accept_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация | abuzer_abuzer"))
        self.input_login.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.input_password.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.label_2.setText(_translate("MainWindow", "Авторизация"))
        self.accept_btn.setText(_translate("MainWindow", "Войти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())