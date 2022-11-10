# -*- coding: utf-8 -*-
"""
main.py

Author: Mitchell Trow
Email: REMOVED
Last Edited: 27 Aug 21 2:00pm

Important:
    Run `pip install -r requirements.txt` first!

Note:
    Python form files have no comments due to them being auto generated and rewritten regularly.
"""
import sys
from PySide6.QtWidgets import QApplication
from Controllers import LoginDialogController, HomeDialogController
from Models import DataViewUserManager



if __name__ == "__main__":
    usersession = DataViewUserManager.UserManager()
    app = QApplication(sys.argv)
    loginDialogWindow = LoginDialogController.Window(app, usersession);
    loginDialogWindow.show()

    #homeDialogWindow = HomeDialogController.Window(Username, app, sessions)
    #homeDialogWindow.show()

    sys.exit(app.exec())
