import sys
from PySide6.QtWidgets import QDialog, QMessageBox
from Controllers import HomeDialogController
from Views import LoginDialog
from Models.DataViewEventHandler import DataEvents
class Window(QDialog):
    """
        Displays the home window along with the dialog triggers attached.
        Extends the QDialog Class.

        Run using the show() method
        """
    def __init__(self, app, usersession):
        self.app = app
        self.usersession = usersession
        super(Window, self).__init__()
        self.dlg = QMessageBox(self)
        self.ui = LoginDialog.Ui_LoginDialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.loginHandler)
        self.ui.buttonBox.rejected.connect(lambda: sys.exit(app.exec()))
        self.ui.registerButton.clicked.connect(self.registerHandler)

    def registerHandler(self):

        username = self.ui.usernameTextbox.text()
        password = self.ui.passwordTextbox.text()
        if username.strip() and password.strip():
            status = self.usersession.register(username, password)
            print(f"LOGIN STATUS: {status}")
            self.dlg.setText(status)
            self.dlg.exec()
        else:
            self.dlg.setText("Invalid input")
            self.dlg.exec()

    def loginHandler(self):
        username = self.ui.usernameTextbox.text()
        password = self.ui.passwordTextbox.text()
        if username.strip() and password.strip():
            status = self.usersession.login(username, password)
            print(f"LOGIN STATUS: {status}")
            self.dlg.setText(status)
            self.dlg.exec()
            if status == "Login Success":
                homeDialogWindow = HomeDialogController.Window(self.app, self.usersession)
                homeDialogWindow.exec()

        else:
            self.dlg.setText("Invalid input")
            self.dlg.exec()
