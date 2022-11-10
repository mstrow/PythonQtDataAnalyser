# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UrlDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_UrlDialog(object):
    def setupUi(self, UrlDialog):
        if not UrlDialog.objectName():
            UrlDialog.setObjectName(u"UrlDialog")
        UrlDialog.resize(400, 70)
        self.formLayout = QFormLayout(UrlDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(UrlDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(UrlDialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.buttonBox = QDialogButtonBox(UrlDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.buttonBox)


        self.retranslateUi(UrlDialog)
        self.buttonBox.accepted.connect(UrlDialog.accept)
        self.buttonBox.rejected.connect(UrlDialog.reject)

        QMetaObject.connectSlotsByName(UrlDialog)
    # setupUi

    def retranslateUi(self, UrlDialog):
        UrlDialog.setWindowTitle(QCoreApplication.translate("UrlDialog", u"Enter URL", None))
        self.label.setText(QCoreApplication.translate("UrlDialog", u"URL: ", None))
    # retranslateUi

