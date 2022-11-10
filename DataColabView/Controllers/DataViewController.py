from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow, QFileDialog, QDialog
import pyqtgraph as pg
from Views import DataView, UsersDialog, TerminalDialog, UrlDialog, ChartSettingsDialog

class Window(QMainWindow):
    """
    Displays the main data view Window along with the dialog triggers attached.
    Extends the QMainWindow Class.

    Run using the show() method
    """
    def __init__(self, usersession, datasession, app, dataevents):
        super(Window, self).__init__()
        self.ui = DataView.Ui_DataViewWindow()
        self.ui.setupUi(self)
        self.datasession = datasession
        self.usersession = usersession
        self.app = app
        self.DataEvents = dataevents

        self.UiInit()
        self.Graphinit()


    def UiInit(self):
        """
        Adds functionality to the markup

        Returns:
            None
        """
        self.chatListViewModel = QtGui.QStandardItemModel()
        self.ui.chatListView.setModel(self.chatListViewModel)

        self.ui.chatSendButton.clicked.connect(self.SendMessage)
        self.ui.usersButton.clicked.connect(self.Users)
        self.ui.closeButton.clicked.connect(lambda: self.close())
        self.ui.duplicateButton.clicked.connect(self.Duplicate)
        self.ui.actionTerminal.triggered.connect(self.Terminal)
        self.ui.actionUrl.triggered.connect(self.Url)
        self.ui.actionUpload.triggered.connect(self.Upload)
        self.ui.actionMerge.triggered.connect(self.Merge)
        self.ui.actionChart_Settings.triggered.connect(self.ChartSettings)
        self.ui.actionExport.triggered.connect(self.Export)
        self.ui.labelUsername.setText(self.usersession.current_user)
        self.ui.chartTypeCombo.currentIndexChanged.connect(self.GraphUpdate)

        self.DataEvents.GraphUpdateEvent.connect(self.GraphUpdate)

    def Graphinit(self):
        """
        Initializes and sets up the graph and calls graphupdate

        Returns:
            None
        """
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.graphWidget = pg.PlotWidget(self.ui.centralwidget)
        self.ui.graphLayout.addWidget(self.graphWidget)
        self.plot = self.graphWidget.plot()

        self.GraphUpdate()

    def GraphUpdate(self):
        """
        Updates the graph using data from the session data helper

        Returns:
            None
        """
        self.graphWidget.clear()
        self.plot = self.graphWidget.plot()
        x = self.datasession.datahandler.dataframe.iloc[:, 0].to_numpy()
        y = self.datasession.datahandler.dataframe.iloc[:, 1].to_numpy()

        if self.ui.chartTypeCombo.currentText() == "Line":

            self.plot.setData(x=x,
                              y=y)
        elif self.ui.chartTypeCombo.currentText() == "Bar":
            bg1 = pg.BarGraphItem(x=x,
                                  height=y, width=0.3, brush='r')
            self.graphWidget.addItem(bg1)
        elif self.ui.chartTypeCombo.currentText() == "Dot":
            sp1 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(0, 0, 0, 120))
            sp1.addPoints(x, y)
            self.graphWidget.addItem(sp1)

    def SendMessage(self):
        """
        Triggered upon send chat button press. Adds the message from the text input to the chat box.

        Returns:
            None
        """
        message = self.ui.chatInput.text()
        if message.strip():
            item = QtGui.QStandardItem(self.usersession.current_user + ":  " + message)
            self.chatListViewModel.appendRow(item)
            self.ui.chatListView.scrollToBottom()
            self.ui.chatInput.setText('')

    def Users(self):
        """
        Triggered on Users button press. Displays users dialog.

        Returns:
            None
        """
        dialog = QDialog(self)
        dialog.ui = UsersDialog.Ui_UsersDialog()
        dialog.ui.setupUi(dialog)
        dialog.exec()

    def Terminal(self):
        """
        Triggered on Terminal action press. Displays terminal dialog.

        Returns:
            None
        """
        dialog = QDialog(self)
        dialog.ui = TerminalDialog.Ui_TerminalDialog()
        dialog.ui.setupUi(dialog)
        dialog.exec()

    def Url(self):
        """
        Triggered on URL action press. Displays enter url dialog.

        Returns:
            None
        """
        dialog = QDialog(self)
        dialog.ui = UrlDialog.Ui_UrlDialog()
        dialog.ui.setupUi(dialog)
        dialog.exec()

    def ChartSettings(self):
        """
        Triggered on ChartSettings action press. Displays chart stettings dialog.

        Returns:
            None
        """
        dialog = QDialog(self)
        dialog.ui = ChartSettingsDialog.Ui_ChartSettingsDialog()
        dialog.ui.setupUi(dialog)
        dialog.exec()

    def Duplicate(self):
        dataViewWindow = type(self)(self.usersession, self.datasession, self.app, self.DataEvents)
        dataViewWindow.show()

    def Upload(self):
        """
        Triggered on upload action press. Displays open file dialog,
        calls the session datahandler and triggers the graph update event


        Returns:
            None
        """
        filename, filter = QFileDialog.getOpenFileName(parent=self,
                                                       caption='Open file',
                                                       dir='./data',
                                                       filter='Comma Separated Values (*.csv)')
        if filename:
            self.datasession.datahandler.Open(filename)
            self.DataEvents.GraphUpdateEvent.emit()
            self.ui.actionMerge.setEnabled(True)

    def Merge(self):
        """
        Triggered on merge action press. Displays open file dialog,
        calls the session datahandler and triggers the graph update event


        Returns:
            None
        """
        filename, filter = QFileDialog.getOpenFileName(parent=self,
                                                       caption='Open file to merge',
                                                       dir='./data',
                                                       filter='Comma Separated Values (*.csv)')
        if filename:
            self.datasession.datahandler.Merge(filename)
            self.DataEvents.GraphUpdateEvent.emit()

    def Export(self):
        """
                Triggered on export action press. Displays save file dialog,
                calls the session datahandler and save the file to the path


                Returns:
                    None
        """
        filename, filter = QFileDialog.getSaveFileName(parent=self,
                                                       caption='Save table',
                                                       dir='./data',
                                                       filter='Comma Separated Values (*.csv)')
        if filename:
            self.datasession.datahandler.Save(filename)
