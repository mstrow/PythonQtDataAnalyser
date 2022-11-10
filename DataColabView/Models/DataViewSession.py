from Models.DataViewDataHandler import DataHandler

class Session:
    """
    Holds the session info and the data being used.

    TODO:
    Complete this for multi-user support

    """


    def __init__(self, name):
        self.datahandler = DataHandler()
        self.name = name
        self.chat = None
        self.users = []