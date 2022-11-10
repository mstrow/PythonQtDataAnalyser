# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChartSettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_ChartSettingsDialog(object):
    def setupUi(self, ChartSettingsDialog):
        if not ChartSettingsDialog.objectName():
            ChartSettingsDialog.setObjectName(u"ChartSettingsDialog")
        ChartSettingsDialog.resize(279, 174)
        self.formLayout = QFormLayout(ChartSettingsDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(ChartSettingsDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.backgroundButton = QPushButton(ChartSettingsDialog)
        self.backgroundButton.setObjectName(u"backgroundButton")
        self.backgroundButton.setMaximumSize(QSize(30, 16777215))
        self.backgroundButton.setFlat(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.backgroundButton)

        self.label_3 = QLabel(ChartSettingsDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.foregroundButton = QPushButton(ChartSettingsDialog)
        self.foregroundButton.setObjectName(u"foregroundButton")
        self.foregroundButton.setMaximumSize(QSize(30, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.foregroundButton)

        self.label_4 = QLabel(ChartSettingsDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelsXBox = QCheckBox(ChartSettingsDialog)
        self.labelsXBox.setObjectName(u"labelsXBox")

        self.horizontalLayout.addWidget(self.labelsXBox)

        self.labelsYBox = QCheckBox(ChartSettingsDialog)
        self.labelsYBox.setObjectName(u"labelsYBox")

        self.horizontalLayout.addWidget(self.labelsYBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(3, QFormLayout.FieldRole, self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ChartSettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.buttonBox)


        self.retranslateUi(ChartSettingsDialog)
        self.buttonBox.accepted.connect(ChartSettingsDialog.accept)
        self.buttonBox.rejected.connect(ChartSettingsDialog.reject)

        QMetaObject.connectSlotsByName(ChartSettingsDialog)
    # setupUi

    def retranslateUi(self, ChartSettingsDialog):
        ChartSettingsDialog.setWindowTitle(QCoreApplication.translate("ChartSettingsDialog", u"Chart Settings", None))
        self.label_2.setText(QCoreApplication.translate("ChartSettingsDialog", u"Background Color:", None))
        self.backgroundButton.setText("")
        self.label_3.setText(QCoreApplication.translate("ChartSettingsDialog", u"Foreground Color:", None))
        self.foregroundButton.setText("")
        self.label_4.setText(QCoreApplication.translate("ChartSettingsDialog", u"Axis Labels:", None))
        self.labelsXBox.setText(QCoreApplication.translate("ChartSettingsDialog", u"X", None))
        self.labelsYBox.setText(QCoreApplication.translate("ChartSettingsDialog", u"Y", None))
    # retranslateUi

