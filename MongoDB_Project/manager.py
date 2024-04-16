# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class ManagerProfileUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(751, 581)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 751, 581))
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(2, 84, 218))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(2, 84, 218))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(2, 84, 218))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(2, 84, 218))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(2, 84, 218))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(2, 84, 218))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(2, 84, 218))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(2, 84, 218))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(2, 84, 218))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.bgwidget.setPalette(palette)
        self.bgwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(2, 84, 218, 255));")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(190, 70, 431, 71))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 160, 171, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";color:rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QPushButton(self.bgwidget)
        self.login.setGeometry(QtCore.QRect(230, 210, 341, 41))
        self.login.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.login.setObjectName("login")
        self.login_2 = QtWidgets.QPushButton(self.bgwidget)
        self.login_2.setGeometry(QtCore.QRect(230, 260, 341, 41))
        self.login_2.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.login_2.setObjectName("login_2")
        self.login_3 = QtWidgets.QPushButton(self.bgwidget)
        self.login_3.setGeometry(QtCore.QRect(230, 310, 341, 41))
        self.login_3.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.login_3.setObjectName("login_3")
        self.login_4 = QtWidgets.QPushButton(self.bgwidget)
        self.login_4.setGeometry(QtCore.QRect(230, 360, 341, 41))
        self.login_4.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.login_4.setObjectName("login_4")
        self.login_5 = QtWidgets.QPushButton(self.bgwidget)
        self.login_5.setGeometry(QtCore.QRect(230, 480, 341, 41))
        self.login_5.setStyleSheet("border-radius:20px;\n"
"background-color:rgb(166, 166, 166);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.Dialog = Dialog
        self.login_5.setObjectName("login_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.login_5.clicked.connect(self.redirect_to_login)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Bienvenue Manager"))
        self.label_2.setText(_translate("Dialog", "Choisie un service"))
        self.login.setText(_translate("Dialog", "Gestion des voitures"))
        self.login_2.setText(_translate("Dialog", "Gestion des clients"))
        self.login_3.setText(_translate("Dialog", "Faire une réservation"))
        self.login_4.setText(_translate("Dialog", "Gestion des réservations"))
        self.login_5.setText(_translate("Dialog", "Déconnexion"))

    def redirect_to_login(self):
        from login import Ui_Dialog
        # Fermer la fenêtre du profil manager
        self.Dialog.close()
    # Afficher la fenêtre de connexion
        login_dialog = QtWidgets.QDialog()
        login_ui = Ui_Dialog()
        login_ui.setupUi(login_dialog)  # Passer la référence à la fenêtre du manager
        login_dialog.exec_()


