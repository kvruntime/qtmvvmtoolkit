from PyQt6 import QtCore


class Navigator(QtCore.QObject):
    pushed = QtCore.pyqtSignal(bool)
    poped = QtCore.pyqtSignal(bool)
    popedToRoot = QtCore.pyqtSignal(bool)

    def __init__(self) -> None:
        pass
    
    def push(self):
        return None
    
    def pop(self):
        return None
    
    pass
