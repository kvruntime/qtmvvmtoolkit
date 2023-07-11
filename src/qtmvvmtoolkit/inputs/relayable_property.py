# this new feature allow viewmodel to be notified when called
# and call a function in viewmodel (eg: to update application state, for example

import typing

from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal


class RelayableProperty(QtCore.QObject):
    """Property that call a method when called.
    this signal will be sent ; as response, a function will be called
    """

    relayed = pyqtSignal(name="relayed")

    def __init__(self) -> None:
        super().__init__()
        return

    def call(self) -> None:
        self.relayed.emit()
        return None

    def binding(self, method: typing.Callable[[], None]) -> None:
        self.relayed.connect(method)
        return None
