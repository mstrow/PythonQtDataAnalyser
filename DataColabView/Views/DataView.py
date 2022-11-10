# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataView.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_DataViewWindow(object):
    def setupUi(self, DataViewWindow):
        if not DataViewWindow.objectName():
            DataViewWindow.setObjectName(u"DataViewWindow")
        DataViewWindow.resize(866, 623)
        self.actionUpload_Data_Source = QAction(DataViewWindow)
        self.actionUpload_Data_Source.setObjectName(u"actionUpload_Data_Source")
        self.actionTerminal = QAction(DataViewWindow)
        self.actionTerminal.setObjectName(u"actionTerminal")
        self.actionExport = QAction(DataViewWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionQuit = QAction(DataViewWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionChart_Settings = QAction(DataViewWindow)
        self.actionChart_Settings.setObjectName(u"actionChart_Settings")
        self.actionUpload = QAction(DataViewWindow)
        self.actionUpload.setObjectName(u"actionUpload")
        self.actionUrl = QAction(DataViewWindow)
        self.actionUrl.setObjectName(u"actionUrl")
        self.actionReset_View = QAction(DataViewWindow)
        self.actionReset_View.setObjectName(u"actionReset_View")
        self.actionManual = QAction(DataViewWindow)
        self.actionManual.setObjectName(u"actionManual")
        self.actionAbout = QAction(DataViewWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionMerge = QAction(DataViewWindow)
        self.actionMerge.setObjectName(u"actionMerge")
        self.actionMerge.setEnabled(False)
        self.centralwidget = QWidget(DataViewWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topLayout = QHBoxLayout()
        self.topLayout.setObjectName(u"topLayout")
        self.topLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setCheckable(False)

        self.topLayout.addWidget(self.closeButton)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.topLayout.addWidget(self.label_5)

        self.labelUsername = QLabel(self.centralwidget)
        self.labelUsername.setObjectName(u"labelUsername")
        font = QFont()
        font.setItalic(True)
        self.labelUsername.setFont(font)
        self.labelUsername.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelUsername.setMargin(5)

        self.topLayout.addWidget(self.labelUsername)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topLayout.addItem(self.horizontalSpacer_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.RightToLeft)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.topLayout.addWidget(self.label_6)

        self.chartTypeCombo = QComboBox(self.centralwidget)
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.setObjectName(u"chartTypeCombo")
        self.chartTypeCombo.setLayoutDirection(Qt.LeftToRight)

        self.topLayout.addWidget(self.chartTypeCombo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topLayout.addItem(self.horizontalSpacer)

        self.duplicateButton = QPushButton(self.centralwidget)
        self.duplicateButton.setObjectName(u"duplicateButton")

        self.topLayout.addWidget(self.duplicateButton)


        self.verticalLayout.addLayout(self.topLayout)

        self.middleLayout = QHBoxLayout()
        self.middleLayout.setObjectName(u"middleLayout")
        self.graphGroupBox = QGroupBox(self.centralwidget)
        self.graphGroupBox.setObjectName(u"graphGroupBox")
        self.graphGroupBox.setFlat(False)
        self.graphLayout = QHBoxLayout(self.graphGroupBox)
        self.graphLayout.setObjectName(u"graphLayout")
        self.graphLayout.setContentsMargins(4, 4, 4, 4)

        self.middleLayout.addWidget(self.graphGroupBox)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.setObjectName(u"rightLayout")
        self.informationGroupBox = QGroupBox(self.centralwidget)
        self.informationGroupBox.setObjectName(u"informationGroupBox")
        self.informationGroupBox.setFlat(False)
        self.informationGroupBox.setCheckable(False)
        self.formLayout = QFormLayout(self.informationGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_3 = QLabel(self.informationGroupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.informationGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_4)

        self.label = QLabel(self.informationGroupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.informationGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)


        self.rightLayout.addWidget(self.informationGroupBox)

        self.chatGroupBox = QGroupBox(self.centralwidget)
        self.chatGroupBox.setObjectName(u"chatGroupBox")
        self.chatGroupBox.setFlat(False)
        self.chatGroupBox.setCheckable(False)
        self.chatLayout = QVBoxLayout(self.chatGroupBox)
        self.chatLayout.setSpacing(1)
        self.chatLayout.setObjectName(u"chatLayout")
        self.chatLayout.setContentsMargins(4, 6, 4, 4)
        self.usersButton = QPushButton(self.chatGroupBox)
        self.usersButton.setObjectName(u"usersButton")

        self.chatLayout.addWidget(self.usersButton)

        self.chatListView = QListView(self.chatGroupBox)
        self.chatListView.setObjectName(u"chatListView")
        self.chatListView.setFrameShape(QFrame.NoFrame)
        self.chatListView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.chatListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.chatListView.setProperty("showDropIndicator", False)
        self.chatListView.setDragDropMode(QAbstractItemView.DragOnly)
        self.chatListView.setAlternatingRowColors(True)
        self.chatListView.setSelectionMode(QAbstractItemView.NoSelection)
        self.chatListView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.chatListView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chatListView.setMovement(QListView.Snap)

        self.chatLayout.addWidget(self.chatListView)

        self.chatInputLayout = QHBoxLayout()
        self.chatInputLayout.setSpacing(1)
        self.chatInputLayout.setObjectName(u"chatInputLayout")
        self.chatInputLayout.setContentsMargins(-1, 2, -1, -1)
        self.chatInput = QLineEdit(self.chatGroupBox)
        self.chatInput.setObjectName(u"chatInput")

        self.chatInputLayout.addWidget(self.chatInput)

        self.chatSendButton = QPushButton(self.chatGroupBox)
        self.chatSendButton.setObjectName(u"chatSendButton")

        self.chatInputLayout.addWidget(self.chatSendButton)

        self.chatInputLayout.setStretch(0, 3)
        self.chatInputLayout.setStretch(1, 1)

        self.chatLayout.addLayout(self.chatInputLayout)


        self.rightLayout.addWidget(self.chatGroupBox)

        self.rightLayout.setStretch(0, 1)
        self.rightLayout.setStretch(1, 2)

        self.middleLayout.addLayout(self.rightLayout)

        self.middleLayout.setStretch(0, 10)
        self.middleLayout.setStretch(1, 5)

        self.verticalLayout.addLayout(self.middleLayout)

        self.verticalLayout.setStretch(1, 10)
        DataViewWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DataViewWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 866, 22))
        self.menuData = QMenu(self.menubar)
        self.menuData.setObjectName(u"menuData")
        self.menuChart = QMenu(self.menubar)
        self.menuChart.setObjectName(u"menuChart")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        DataViewWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuChart.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuData.addAction(self.actionUpload)
        self.menuData.addAction(self.actionUrl)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionMerge)
        self.menuChart.addAction(self.actionReset_View)
        self.menuChart.addSeparator()
        self.menuChart.addAction(self.actionTerminal)
        self.menuChart.addAction(self.actionChart_Settings)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(DataViewWindow)

        QMetaObject.connectSlotsByName(DataViewWindow)
    # setupUi

    def retranslateUi(self, DataViewWindow):
        DataViewWindow.setWindowTitle(QCoreApplication.translate("DataViewWindow", u"Data View", None))
        self.actionUpload_Data_Source.setText(QCoreApplication.translate("DataViewWindow", u"Upload Data Source...", None))
        self.actionTerminal.setText(QCoreApplication.translate("DataViewWindow", u"Terminal...", None))
        self.actionExport.setText(QCoreApplication.translate("DataViewWindow", u"Export...", None))
        self.actionQuit.setText(QCoreApplication.translate("DataViewWindow", u"Quit", None))
        self.actionChart_Settings.setText(QCoreApplication.translate("DataViewWindow", u"Chart Settings...", None))
        self.actionUpload.setText(QCoreApplication.translate("DataViewWindow", u"Upload file...", None))
        self.actionUrl.setText(QCoreApplication.translate("DataViewWindow", u"Upload via URL...", None))
        self.actionReset_View.setText(QCoreApplication.translate("DataViewWindow", u"Reset View", None))
        self.actionManual.setText(QCoreApplication.translate("DataViewWindow", u"Manual...", None))
        self.actionAbout.setText(QCoreApplication.translate("DataViewWindow", u"About...", None))
        self.actionMerge.setText(QCoreApplication.translate("DataViewWindow", u"Append (merge) file...", None))
        self.closeButton.setText(QCoreApplication.translate("DataViewWindow", u"Close", None))
        self.label_5.setText(QCoreApplication.translate("DataViewWindow", u"Logged in as:", None))
        self.labelUsername.setText(QCoreApplication.translate("DataViewWindow", u"Username", None))
        self.label_6.setText(QCoreApplication.translate("DataViewWindow", u"Chart Type: ", None))
        self.chartTypeCombo.setItemText(0, QCoreApplication.translate("DataViewWindow", u"Line", None))
        self.chartTypeCombo.setItemText(1, QCoreApplication.translate("DataViewWindow", u"Dot", None))
        self.chartTypeCombo.setItemText(2, QCoreApplication.translate("DataViewWindow", u"Bar", None))

        self.duplicateButton.setText(QCoreApplication.translate("DataViewWindow", u"New Window in Session", None))
        self.graphGroupBox.setTitle(QCoreApplication.translate("DataViewWindow", u"Graph", None))
        self.informationGroupBox.setTitle(QCoreApplication.translate("DataViewWindow", u"Information", None))
        self.label_3.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.chatGroupBox.setTitle(QCoreApplication.translate("DataViewWindow", u"Chat", None))
        self.usersButton.setText(QCoreApplication.translate("DataViewWindow", u"Users", None))
        self.chatSendButton.setText(QCoreApplication.translate("DataViewWindow", u"Send", None))
        self.menuData.setTitle(QCoreApplication.translate("DataViewWindow", u"Data", None))
        self.menuChart.setTitle(QCoreApplication.translate("DataViewWindow", u"Chart", None))
        self.menuFile.setTitle(QCoreApplication.translate("DataViewWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("DataViewWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataView.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_DataViewWindow(object):
    def setupUi(self, DataViewWindow):
        if not DataViewWindow.objectName():
            DataViewWindow.setObjectName(u"DataViewWindow")
        DataViewWindow.resize(866, 623)
        self.actionUpload_Data_Source = QAction(DataViewWindow)
        self.actionUpload_Data_Source.setObjectName(u"actionUpload_Data_Source")
        self.actionTerminal = QAction(DataViewWindow)
        self.actionTerminal.setObjectName(u"actionTerminal")
        self.actionExport = QAction(DataViewWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionQuit = QAction(DataViewWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionChart_Settings = QAction(DataViewWindow)
        self.actionChart_Settings.setObjectName(u"actionChart_Settings")
        self.actionUpload = QAction(DataViewWindow)
        self.actionUpload.setObjectName(u"actionUpload")
        self.actionUrl = QAction(DataViewWindow)
        self.actionUrl.setObjectName(u"actionUrl")
        self.actionReset_View = QAction(DataViewWindow)
        self.actionReset_View.setObjectName(u"actionReset_View")
        self.actionManual = QAction(DataViewWindow)
        self.actionManual.setObjectName(u"actionManual")
        self.actionAbout = QAction(DataViewWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionMerge = QAction(DataViewWindow)
        self.actionMerge.setObjectName(u"actionMerge")
        self.centralwidget = QWidget(DataViewWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topLayout = QHBoxLayout()
        self.topLayout.setObjectName(u"topLayout")
        self.topLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setCheckable(False)

        self.topLayout.addWidget(self.closeButton)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.topLayout.addWidget(self.label_5)

        self.labelUsername = QLabel(self.centralwidget)
        self.labelUsername.setObjectName(u"labelUsername")
        font = QFont()
        font.setItalic(True)
        self.labelUsername.setFont(font)
        self.labelUsername.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelUsername.setMargin(5)

        self.topLayout.addWidget(self.labelUsername)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topLayout.addItem(self.horizontalSpacer_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.RightToLeft)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.topLayout.addWidget(self.label_6)

        self.chartTypeCombo = QComboBox(self.centralwidget)
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.setObjectName(u"chartTypeCombo")
        self.chartTypeCombo.setLayoutDirection(Qt.LeftToRight)

        self.topLayout.addWidget(self.chartTypeCombo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topLayout.addItem(self.horizontalSpacer)

        self.duplicateButton = QPushButton(self.centralwidget)
        self.duplicateButton.setObjectName(u"duplicateButton")

        self.topLayout.addWidget(self.duplicateButton)


        self.verticalLayout.addLayout(self.topLayout)

        self.middleLayout = QHBoxLayout()
        self.middleLayout.setObjectName(u"middleLayout")
        self.graphGroupBox = QGroupBox(self.centralwidget)
        self.graphGroupBox.setObjectName(u"graphGroupBox")
        self.graphGroupBox.setFlat(False)
        self.graphLayout = QHBoxLayout(self.graphGroupBox)
        self.graphLayout.setObjectName(u"graphLayout")
        self.graphLayout.setContentsMargins(4, 4, 4, 4)

        self.middleLayout.addWidget(self.graphGroupBox)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.setObjectName(u"rightLayout")
        self.informationGroupBox = QGroupBox(self.centralwidget)
        self.informationGroupBox.setObjectName(u"informationGroupBox")
        self.informationGroupBox.setFlat(False)
        self.informationGroupBox.setCheckable(False)
        self.formLayout = QFormLayout(self.informationGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_3 = QLabel(self.informationGroupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.informationGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_4)

        self.label = QLabel(self.informationGroupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.informationGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)


        self.rightLayout.addWidget(self.informationGroupBox)

        self.chatGroupBox = QGroupBox(self.centralwidget)
        self.chatGroupBox.setObjectName(u"chatGroupBox")
        self.chatGroupBox.setFlat(False)
        self.chatGroupBox.setCheckable(False)
        self.chatLayout = QVBoxLayout(self.chatGroupBox)
        self.chatLayout.setSpacing(1)
        self.chatLayout.setObjectName(u"chatLayout")
        self.chatLayout.setContentsMargins(4, 6, 4, 4)
        self.usersButton = QPushButton(self.chatGroupBox)
        self.usersButton.setObjectName(u"usersButton")

        self.chatLayout.addWidget(self.usersButton)

        self.chatListView = QListView(self.chatGroupBox)
        self.chatListView.setObjectName(u"chatListView")
        self.chatListView.setFrameShape(QFrame.NoFrame)
        self.chatListView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.chatListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.chatListView.setProperty("showDropIndicator", False)
        self.chatListView.setDragDropMode(QAbstractItemView.DragOnly)
        self.chatListView.setAlternatingRowColors(True)
        self.chatListView.setSelectionMode(QAbstractItemView.NoSelection)
        self.chatListView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.chatListView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chatListView.setMovement(QListView.Snap)

        self.chatLayout.addWidget(self.chatListView)

        self.chatInputLayout = QHBoxLayout()
        self.chatInputLayout.setSpacing(1)
        self.chatInputLayout.setObjectName(u"chatInputLayout")
        self.chatInputLayout.setContentsMargins(-1, 2, -1, -1)
        self.chatInput = QLineEdit(self.chatGroupBox)
        self.chatInput.setObjectName(u"chatInput")

        self.chatInputLayout.addWidget(self.chatInput)

        self.chatSendButton = QPushButton(self.chatGroupBox)
        self.chatSendButton.setObjectName(u"chatSendButton")

        self.chatInputLayout.addWidget(self.chatSendButton)

        self.chatInputLayout.setStretch(0, 3)
        self.chatInputLayout.setStretch(1, 1)

        self.chatLayout.addLayout(self.chatInputLayout)


        self.rightLayout.addWidget(self.chatGroupBox)

        self.rightLayout.setStretch(0, 1)
        self.rightLayout.setStretch(1, 2)

        self.middleLayout.addLayout(self.rightLayout)

        self.middleLayout.setStretch(0, 10)
        self.middleLayout.setStretch(1, 5)

        self.verticalLayout.addLayout(self.middleLayout)

        self.verticalLayout.setStretch(1, 10)
        DataViewWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DataViewWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 866, 24))
        self.menuData = QMenu(self.menubar)
        self.menuData.setObjectName(u"menuData")
        self.menuChart = QMenu(self.menubar)
        self.menuChart.setObjectName(u"menuChart")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        DataViewWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuChart.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuData.addAction(self.actionUpload)
        self.menuData.addAction(self.actionUrl)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionMerge)
        self.menuChart.addAction(self.actionReset_View)
        self.menuChart.addSeparator()
        self.menuChart.addAction(self.actionTerminal)
        self.menuChart.addAction(self.actionChart_Settings)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(DataViewWindow)

        QMetaObject.connectSlotsByName(DataViewWindow)
    # setupUi

    def retranslateUi(self, DataViewWindow):
        DataViewWindow.setWindowTitle(QCoreApplication.translate("DataViewWindow", u"Data View", None))
        self.actionUpload_Data_Source.setText(QCoreApplication.translate("DataViewWindow", u"Upload Data Source...", None))
        self.actionTerminal.setText(QCoreApplication.translate("DataViewWindow", u"Terminal...", None))
        self.actionExport.setText(QCoreApplication.translate("DataViewWindow", u"Export...", None))
        self.actionQuit.setText(QCoreApplication.translate("DataViewWindow", u"Quit", None))
        self.actionChart_Settings.setText(QCoreApplication.translate("DataViewWindow", u"Chart Settings...", None))
        self.actionUpload.setText(QCoreApplication.translate("DataViewWindow", u"Upload file...", None))
        self.actionUrl.setText(QCoreApplication.translate("DataViewWindow", u"Upload via URL...", None))
        self.actionReset_View.setText(QCoreApplication.translate("DataViewWindow", u"Reset View", None))
        self.actionManual.setText(QCoreApplication.translate("DataViewWindow", u"Manual...", None))
        self.actionAbout.setText(QCoreApplication.translate("DataViewWindow", u"About...", None))
        self.actionMerge.setText(QCoreApplication.translate("DataViewWindow", u"Append (merge) file...", None))
        self.closeButton.setText(QCoreApplication.translate("DataViewWindow", u"Close", None))
        self.label_5.setText(QCoreApplication.translate("DataViewWindow", u"Logged in as:", None))
        self.labelUsername.setText(QCoreApplication.translate("DataViewWindow", u"Username", None))
        self.label_6.setText(QCoreApplication.translate("DataViewWindow", u"Chart Type: ", None))
        self.chartTypeCombo.setItemText(0, QCoreApplication.translate("DataViewWindow", u"Line", None))
        self.chartTypeCombo.setItemText(1, QCoreApplication.translate("DataViewWindow", u"Dot", None))
        self.chartTypeCombo.setItemText(2, QCoreApplication.translate("DataViewWindow", u"Bar", None))

        self.duplicateButton.setText(QCoreApplication.translate("DataViewWindow", u"New Window in Session", None))
        self.graphGroupBox.setTitle(QCoreApplication.translate("DataViewWindow", u"Graph", None))
        self.informationGroupBox.setTitle(QCoreApplication.translate("DataViewWindow", u"Information", None))
        self.label_3.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.chatGroupBox.setTitle(QCoreApplication.translate("DataViewWindow", u"Chat", None))
        self.usersButton.setText(QCoreApplication.translate("DataViewWindow", u"Users", None))
        self.chatSendButton.setText(QCoreApplication.translate("DataViewWindow", u"Send", None))
        self.menuData.setTitle(QCoreApplication.translate("DataViewWindow", u"Data", None))
        self.menuChart.setTitle(QCoreApplication.translate("DataViewWindow", u"Chart", None))
        self.menuFile.setTitle(QCoreApplication.translate("DataViewWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("DataViewWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataView.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_DataViewWindow(object):
    def setupUi(self, DataViewWindow):
        if not DataViewWindow.objectName():
            DataViewWindow.setObjectName(u"DataViewWindow")
        DataViewWindow.resize(866, 623)
        self.actionUpload_Data_Source = QAction(DataViewWindow)
        self.actionUpload_Data_Source.setObjectName(u"actionUpload_Data_Source")
        self.actionTerminal = QAction(DataViewWindow)
        self.actionTerminal.setObjectName(u"actionTerminal")
        self.actionExport = QAction(DataViewWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionQuit = QAction(DataViewWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionChart_Settings = QAction(DataViewWindow)
        self.actionChart_Settings.setObjectName(u"actionChart_Settings")
        self.actionUpload = QAction(DataViewWindow)
        self.actionUpload.setObjectName(u"actionUpload")
        self.actionUrl = QAction(DataViewWindow)
        self.actionUrl.setObjectName(u"actionUrl")
        self.actionReset_View = QAction(DataViewWindow)
        self.actionReset_View.setObjectName(u"actionReset_View")
        self.actionManual = QAction(DataViewWindow)
        self.actionManual.setObjectName(u"actionManual")
        self.actionAbout = QAction(DataViewWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionMerge = QAction(DataViewWindow)
        self.actionMerge.setObjectName(u"actionMerge")
        self.centralwidget = QWidget(DataViewWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topLayout = QHBoxLayout()
        self.topLayout.setObjectName(u"topLayout")
        self.topLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setCheckable(False)

        self.topLayout.addWidget(self.closeButton)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.topLayout.addWidget(self.label_5)

        self.labelUsername = QLabel(self.centralwidget)
        self.labelUsername.setObjectName(u"labelUsername")
        font = QFont()
        font.setItalic(True)
        self.labelUsername.setFont(font)
        self.labelUsername.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelUsername.setMargin(5)

        self.topLayout.addWidget(self.labelUsername)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topLayout.addItem(self.horizontalSpacer_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.RightToLeft)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.topLayout.addWidget(self.label_6)

        self.chartTypeCombo = QComboBox(self.centralwidget)
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.addItem("")
        self.chartTypeCombo.setObjectName(u"chartTypeCombo")
        self.chartTypeCombo.setLayoutDirection(Qt.LeftToRight)

        self.topLayout.addWidget(self.chartTypeCombo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topLayout.addItem(self.horizontalSpacer)

        self.duplicateButton = QPushButton(self.centralwidget)
        self.duplicateButton.setObjectName(u"duplicateButton")

        self.topLayout.addWidget(self.duplicateButton)


        self.verticalLayout.addLayout(self.topLayout)

        self.middleLayout = QHBoxLayout()
        self.middleLayout.setObjectName(u"middleLayout")
        self.graphGroupBox = QGroupBox(self.centralwidget)
        self.graphGroupBox.setObjectName(u"graphGroupBox")
        self.graphGroupBox.setFlat(False)
        self.graphLayout = QHBoxLayout(self.graphGroupBox)
        self.graphLayout.setObjectName(u"graphLayout")
        self.graphLayout.setContentsMargins(4, 4, 4, 4)

        self.middleLayout.addWidget(self.graphGroupBox)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.setObjectName(u"rightLayout")
        self.informationGroupBox = QGroupBox(self.centralwidget)
        self.informationGroupBox.setObjectName(u"informationGroupBox")
        self.informationGroupBox.setFlat(False)
        self.informationGroupBox.setCheckable(False)
        self.formLayout = QFormLayout(self.informationGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_3 = QLabel(self.informationGroupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.informationGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_4)

        self.label = QLabel(self.informationGroupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.informationGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)


        self.rightLayout.addWidget(self.informationGroupBox)

        self.chatGroupBox = QGroupBox(self.centralwidget)
        self.chatGroupBox.setObjectName(u"chatGroupBox")
        self.chatGroupBox.setFlat(False)
        self.chatGroupBox.setCheckable(False)
        self.chatLayout = QVBoxLayout(self.chatGroupBox)
        self.chatLayout.setSpacing(0)
        self.chatLayout.setObjectName(u"chatLayout")
        self.chatLayout.setContentsMargins(4, 6, 4, 4)
        self.usersButton = QPushButton(self.chatGroupBox)
        self.usersButton.setObjectName(u"usersButton")

        self.chatLayout.addWidget(self.usersButton)

        self.verticalSpacer = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.chatLayout.addItem(self.verticalSpacer)

        self.chatListView = QListView(self.chatGroupBox)
        self.chatListView.setObjectName(u"chatListView")
        self.chatListView.setFrameShape(QFrame.NoFrame)
        self.chatListView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.chatListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.chatListView.setProperty("showDropIndicator", False)
        self.chatListView.setDragDropMode(QAbstractItemView.DragOnly)
        self.chatListView.setAlternatingRowColors(True)
        self.chatListView.setSelectionMode(QAbstractItemView.NoSelection)
        self.chatListView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.chatListView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chatListView.setMovement(QListView.Snap)

        self.chatLayout.addWidget(self.chatListView)

        self.chatInputLayout = QHBoxLayout()
        self.chatInputLayout.setSpacing(1)
        self.chatInputLayout.setObjectName(u"chatInputLayout")
        self.chatInputLayout.setContentsMargins(-1, 2, -1, -1)
        self.chatInput = QLineEdit(self.chatGroupBox)
        self.chatInput.setObjectName(u"chatInput")

        self.chatInputLayout.addWidget(self.chatInput)

        self.chatSendButton = QPushButton(self.chatGroupBox)
        self.chatSendButton.setObjectName(u"chatSendButton")

        self.chatInputLayout.addWidget(self.chatSendButton)

        self.chatInputLayout.setStretch(0, 3)
        self.chatInputLayout.setStretch(1, 1)

        self.chatLayout.addLayout(self.chatInputLayout)


        self.rightLayout.addWidget(self.chatGroupBox)

        self.rightLayout.setStretch(0, 1)
        self.rightLayout.setStretch(1, 2)

        self.middleLayout.addLayout(self.rightLayout)

        self.middleLayout.setStretch(0, 10)
        self.middleLayout.setStretch(1, 5)

        self.verticalLayout.addLayout(self.middleLayout)

        self.verticalLayout.setStretch(1, 10)
        DataViewWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DataViewWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 866, 24))
        self.menuData = QMenu(self.menubar)
        self.menuData.setObjectName(u"menuData")
        self.menuChart = QMenu(self.menubar)
        self.menuChart.setObjectName(u"menuChart")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        DataViewWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuChart.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuData.addAction(self.actionUpload)
        self.menuData.addAction(self.actionUrl)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionMerge)
        self.menuChart.addAction(self.actionReset_View)
        self.menuChart.addSeparator()
        self.menuChart.addAction(self.actionTerminal)
        self.menuChart.addAction(self.actionChart_Settings)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(DataViewWindow)

        QMetaObject.connectSlotsByName(DataViewWindow)
    # setupUi

    def retranslateUi(self, DataViewWindow):
        DataViewWindow.setWindowTitle(QCoreApplication.translate("DataViewWindow", u"Data View", None))
        self.actionUpload_Data_Source.setText(QCoreApplication.translate("DataViewWindow", u"Upload Data Source...", None))
        self.actionTerminal.setText(QCoreApplication.translate("DataViewWindow", u"Terminal...", None))
        self.actionExport.setText(QCoreApplication.translate("DataViewWindow", u"Export...", None))
        self.actionQuit.setText(QCoreApplication.translate("DataViewWindow", u"Quit", None))
        self.actionChart_Settings.setText(QCoreApplication.translate("DataViewWindow", u"Chart Settings...", None))
        self.actionUpload.setText(QCoreApplication.translate("DataViewWindow", u"Upload file...", None))
        self.actionUrl.setText(QCoreApplication.translate("DataViewWindow", u"Upload via URL...", None))
        self.actionReset_View.setText(QCoreApplication.translate("DataViewWindow", u"Reset View", None))
        self.actionManual.setText(QCoreApplication.translate("DataViewWindow", u"Manual...", None))
        self.actionAbout.setText(QCoreApplication.translate("DataViewWindow", u"About...", None))
        self.actionMerge.setText(QCoreApplication.translate("DataViewWindow", u"Append (merge) file...", None))
        self.closeButton.setText(QCoreApplication.translate("DataViewWindow", u"Close", None))
        self.label_5.setText(QCoreApplication.translate("DataViewWindow", u"Logged in as:", None))
        self.labelUsername.setText(QCoreApplication.translate("DataViewWindow", u"Username", None))
        self.label_6.setText(QCoreApplication.translate("DataViewWindow", u"Chart Type: ", None))
        self.chartTypeCombo.setItemText(0, QCoreApplication.translate("DataViewWindow", u"Line", None))
        self.chartTypeCombo.setItemText(1, QCoreApplication.translate("DataViewWindow", u"Dot", None))
        self.chartTypeCombo.setItemText(2, QCoreApplication.translate("DataViewWindow", u"Bar", None))

        self.duplicateButton.setText(QCoreApplication.translate("DataViewWindow", u"New Window in Session", None))
        self.graphGroupBox.setTitle(QCoreApplication.translate("DataViewWindow", u"Graph", None))
        self.informationGroupBox.setTitle(QCoreApplication.translate("DataViewWindow", u"Information", None))
        self.label_3.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("DataViewWindow", u"TextLabel", None))
        self.chatGroupBox.setTitle(QCoreApplication.translate("DataViewWindow", u"Chat", None))
        self.usersButton.setText(QCoreApplication.translate("DataViewWindow", u"Users", None))
        self.chatSendButton.setText(QCoreApplication.translate("DataViewWindow", u"Send", None))
        self.menuData.setTitle(QCoreApplication.translate("DataViewWindow", u"Data", None))
        self.menuChart.setTitle(QCoreApplication.translate("DataViewWindow", u"Chart", None))
        self.menuFile.setTitle(QCoreApplication.translate("DataViewWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("DataViewWindow", u"Help", None))
    # retranslateUi

