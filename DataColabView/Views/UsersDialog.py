# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UsersDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_UsersDialog(object):
    def setupUi(self, UsersDialog):
        if not UsersDialog.objectName():
            UsersDialog.setObjectName(u"UsersDialog")
        UsersDialog.resize(357, 373)
        self.horizontalLayout = QHBoxLayout(UsersDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.usersTableWidget = QTableWidget(UsersDialog)
        if (self.usersTableWidget.columnCount() < 2):
            self.usersTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.usersTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.usersTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.usersTableWidget.rowCount() < 10):
            self.usersTableWidget.setRowCount(10)
        self.usersTableWidget.setObjectName(u"usersTableWidget")
        self.usersTableWidget.setFrameShape(QFrame.NoFrame)
        self.usersTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.usersTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.usersTableWidget.setTabKeyNavigation(False)
        self.usersTableWidget.setProperty("showDropIndicator", False)
        self.usersTableWidget.setAlternatingRowColors(True)
        self.usersTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.usersTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.usersTableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.usersTableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.usersTableWidget.setShowGrid(False)
        self.usersTableWidget.setCornerButtonEnabled(False)
        self.usersTableWidget.setRowCount(10)
        self.usersTableWidget.setColumnCount(2)
        self.usersTableWidget.horizontalHeader().setStretchLastSection(True)
        self.usersTableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.usersTableWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(UsersDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(UsersDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalLayout.setStretch(1, 100)
        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(UsersDialog)
        self.buttonBox.accepted.connect(UsersDialog.accept)
        self.buttonBox.rejected.connect(UsersDialog.reject)

        QMetaObject.connectSlotsByName(UsersDialog)
    # setupUi

    def retranslateUi(self, UsersDialog):
        UsersDialog.setWindowTitle(QCoreApplication.translate("UsersDialog", u"Users", None))
        ___qtablewidgetitem = self.usersTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UsersDialog", u"Name", None));
        ___qtablewidgetitem1 = self.usersTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UsersDialog", u"Role", None));
        self.label.setText(QCoreApplication.translate("UsersDialog", u"Users Online: 0", None))
    # retranslateUi

