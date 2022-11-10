# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TerminalDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_TerminalDialog(object):
    def setupUi(self, TerminalDialog):
        if not TerminalDialog.objectName():
            TerminalDialog.setObjectName(u"TerminalDialog")
        TerminalDialog.resize(545, 376)
        self.verticalLayout = QVBoxLayout(TerminalDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.terminalTableWidget = QTableWidget(TerminalDialog)
        if (self.terminalTableWidget.columnCount() < 1):
            self.terminalTableWidget.setColumnCount(1)
        if (self.terminalTableWidget.rowCount() < 15):
            self.terminalTableWidget.setRowCount(15)
        self.terminalTableWidget.setObjectName(u"terminalTableWidget")
        self.terminalTableWidget.setFrameShape(QFrame.NoFrame)
        self.terminalTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.terminalTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.terminalTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.terminalTableWidget.setTabKeyNavigation(False)
        self.terminalTableWidget.setProperty("showDropIndicator", False)
        self.terminalTableWidget.setDragDropOverwriteMode(False)
        self.terminalTableWidget.setAlternatingRowColors(True)
        self.terminalTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.terminalTableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.terminalTableWidget.setShowGrid(False)
        self.terminalTableWidget.setSortingEnabled(False)
        self.terminalTableWidget.setCornerButtonEnabled(False)
        self.terminalTableWidget.setRowCount(15)
        self.terminalTableWidget.setColumnCount(1)
        self.terminalTableWidget.horizontalHeader().setVisible(False)
        self.terminalTableWidget.horizontalHeader().setStretchLastSection(True)
        self.terminalTableWidget.verticalHeader().setVisible(False)
        self.terminalTableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.terminalTableWidget)

        self.chatInputLayout = QHBoxLayout()
        self.chatInputLayout.setSpacing(1)
        self.chatInputLayout.setObjectName(u"chatInputLayout")
        self.chatInputLayout.setContentsMargins(-1, 2, -1, -1)
        self.chatInput = QLineEdit(TerminalDialog)
        self.chatInput.setObjectName(u"chatInput")

        self.chatInputLayout.addWidget(self.chatInput)

        self.c = QPushButton(TerminalDialog)
        self.c.setObjectName(u"c")

        self.chatInputLayout.addWidget(self.c)

        self.chatInputLayout.setStretch(0, 5)
        self.chatInputLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.chatInputLayout)

        self.buttonBox = QDialogButtonBox(TerminalDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(TerminalDialog)
        self.buttonBox.accepted.connect(TerminalDialog.accept)
        self.buttonBox.rejected.connect(TerminalDialog.reject)

        QMetaObject.connectSlotsByName(TerminalDialog)
    # setupUi

    def retranslateUi(self, TerminalDialog):
        TerminalDialog.setWindowTitle(QCoreApplication.translate("TerminalDialog", u"Terminal", None))
        self.c.setText(QCoreApplication.translate("TerminalDialog", u"Go", None))
    # retranslateUi

