# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_RegisterDialog(object):
    def setupUi(self, RegisterDialog):
        if not RegisterDialog.objectName():
            RegisterDialog.setObjectName(u"RegisterDialog")
        RegisterDialog.resize(270, 157)
        self.formLayout = QFormLayout(RegisterDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.buttonBox = QDialogButtonBox(RegisterDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.buttonBox)

        self.label = QLabel(RegisterDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.usernameTextbox = QLineEdit(RegisterDialog)
        self.usernameTextbox.setObjectName(u"usernameTextbox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.usernameTextbox)

        self.passwordTextbox = QLineEdit(RegisterDialog)
        self.passwordTextbox.setObjectName(u"passwordTextbox")
        self.passwordTextbox.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.passwordTextbox)

        self.label_2 = QLabel(RegisterDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(RegisterDialog)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)


        self.retranslateUi(RegisterDialog)
        self.buttonBox.accepted.connect(RegisterDialog.accept)
        self.buttonBox.rejected.connect(RegisterDialog.reject)

        QMetaObject.connectSlotsByName(RegisterDialog)
    # setupUi

    def retranslateUi(self, RegisterDialog):
        RegisterDialog.setWindowTitle(QCoreApplication.translate("RegisterDialog", u"Register", None))
        self.label.setText(QCoreApplication.translate("RegisterDialog", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("RegisterDialog", u"Password:", None))
        self.label_3.setText(QCoreApplication.translate("RegisterDialog", u"Register", None))
    # retranslateUi

