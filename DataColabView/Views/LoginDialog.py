# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(284, 149)
        self.formLayout = QFormLayout(LoginDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(LoginDialog)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label = QLabel(LoginDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.usernameTextbox = QLineEdit(LoginDialog)
        self.usernameTextbox.setObjectName(u"usernameTextbox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.usernameTextbox)

        self.label_2 = QLabel(LoginDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.passwordTextbox = QLineEdit(LoginDialog)
        self.passwordTextbox.setObjectName(u"passwordTextbox")
        self.passwordTextbox.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.passwordTextbox)

        self.buttonBox = QDialogButtonBox(LoginDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.buttonBox)

        self.registerButton = QPushButton(LoginDialog)
        self.registerButton.setObjectName(u"registerButton")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.registerButton)


        self.retranslateUi(LoginDialog)
        self.buttonBox.accepted.connect(LoginDialog.accept)
        self.buttonBox.rejected.connect(LoginDialog.reject)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("LoginDialog", u"Login", None))
        self.label.setText(QCoreApplication.translate("LoginDialog", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("LoginDialog", u"Password:", None))
        self.registerButton.setText(QCoreApplication.translate("LoginDialog", u"Register", None))
    # retranslateUi

