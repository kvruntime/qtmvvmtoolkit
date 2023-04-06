# this new feature allow viewmodel to be notified when called
# and call a function in viewmodel (eg: to update application state, for example

from PyQt6 import QtCore


class RelayableProperty(QtCore.QObject):
    relayed = QtCore.pyqtSignal(name="relayed")

    # this signal will be sent ; as response, a function will be called

    def __init__(self) -> None:
        super().__init__()
        pass

    def call(self) -> None:
        self.relayed.emit()
        return None
