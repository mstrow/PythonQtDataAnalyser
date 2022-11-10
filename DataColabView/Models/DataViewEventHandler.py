from PySide6 import QtCore

class DataEvents(QtCore.QObject):
    """
    Trigger event to be sent between form objects

    """
    GraphUpdateEvent = QtCore.Signal()
