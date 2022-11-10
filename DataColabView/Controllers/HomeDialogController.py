import sys
from PySide6.QtWidgets import QDialog, QMainWindow
from Controllers import DataViewController
from Views import HomeDialog
from Models.DataViewSession import Session
from Models.DataViewEventHandler import DataEvents
class Window(QDialog):
    """
        Displays the home window along with the dialog triggers attached.
        Extends the QDialog Class.

        Run using the show() method
        """
    def __init__(self, app, usersession):
        self.usersession = usersession
        self.app = app
        self.datasessions = [Session("new session by " + self.usersession.current_user)]
        self.dataevents = DataEvents()
        super(Window, self).__init__()
        self.ui = HomeDialog.Ui_HomeDialog()
        self.ui.setupUi(self)

        self.ui.newButton.clicked.connect(self.handleNewWindow)
        self.ui.logoutButton.clicked.connect(lambda: sys.exit(app.exec()))

        self.ui.usernameLabel.setText(self.usersession.current_user)

    def handleNewWindow(self):
        dataViewWindow = DataViewController.Window(self.usersession, self.datasessions[0], self.app, self.dataevents)
        dataViewWindow.show()
        self.hide()