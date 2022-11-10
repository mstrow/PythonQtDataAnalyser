# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_HomeDialog(object):
    def setupUi(self, HomeDialog):
        if not HomeDialog.objectName():
            HomeDialog.setObjectName(u"HomeDialog")
        HomeDialog.resize(400, 441)
        self.verticalLayout = QVBoxLayout(HomeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(HomeDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.dataTableWidget = QTableWidget(HomeDialog)
        if (self.dataTableWidget.columnCount() < 2):
            self.dataTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.dataTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dataTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.dataTableWidget.rowCount() < 10):
            self.dataTableWidget.setRowCount(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dataTableWidget.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dataTableWidget.setItem(0, 1, __qtablewidgetitem3)
        self.dataTableWidget.setObjectName(u"dataTableWidget")
        self.dataTableWidget.setFrameShape(QFrame.NoFrame)
        self.dataTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.dataTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dataTableWidget.setTabKeyNavigation(False)
        self.dataTableWidget.setProperty("showDropIndicator", False)
        self.dataTableWidget.setAlternatingRowColors(True)
        self.dataTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.dataTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dataTableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataTableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataTableWidget.setShowGrid(True)
        self.dataTableWidget.setCornerButtonEnabled(False)
        self.dataTableWidget.setRowCount(10)
        self.dataTableWidget.setColumnCount(2)
        self.dataTableWidget.horizontalHeader().setStretchLastSection(True)
        self.dataTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.dataTableWidget)

        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.logoutButton = QPushButton(HomeDialog)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setAutoDefault(False)

        self.bottomLayout.addWidget(self.logoutButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomLayout.addItem(self.horizontalSpacer_2)

        self.usernameLabel = QLabel(HomeDialog)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.bottomLayout.addWidget(self.usernameLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomLayout.addItem(self.horizontalSpacer)

        self.newButton = QPushButton(HomeDialog)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setAutoDefault(False)

        self.bottomLayout.addWidget(self.newButton)


        self.verticalLayout.addLayout(self.bottomLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.retranslateUi(HomeDialog)

        self.newButton.setDefault(True)


        QMetaObject.connectSlotsByName(HomeDialog)
    # setupUi

    def retranslateUi(self, HomeDialog):
        HomeDialog.setWindowTitle(QCoreApplication.translate("HomeDialog", u"Home", None))
        self.label.setText(QCoreApplication.translate("HomeDialog", u"Data Collab View", None))
        ___qtablewidgetitem = self.dataTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("HomeDialog", u"Filename", None));
        ___qtablewidgetitem1 = self.dataTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("HomeDialog", u"Users", None));

        __sortingEnabled = self.dataTableWidget.isSortingEnabled()
        self.dataTableWidget.setSortingEnabled(False)
        self.dataTableWidget.setSortingEnabled(__sortingEnabled)

        self.logoutButton.setText(QCoreApplication.translate("HomeDialog", u"Logout", None))
        self.usernameLabel.setText(QCoreApplication.translate("HomeDialog", u"Username", None))
        self.newButton.setText(QCoreApplication.translate("HomeDialog", u"New Session", None))
    # retranslateUi

