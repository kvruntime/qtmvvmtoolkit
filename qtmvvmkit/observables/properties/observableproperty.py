import typing

from PyQt6.QtCore import QObject
from PyQt6.QtCore import pyqtSignal
import typing


class ObservableProperty(QObject):
    valueChanged = pyqtSignal(str, name="valueChanged")

    def __init__(self, prop) -> None:
        super().__init__()
        self.prop: typing.Any = None
        self.set(prop)
        pass

    def get(self):
        return self.prop

    def set(self, value):
        if value != self.prop:
            self.prop = value
            self.valueChanged.emit(self.prop)
        return


# T = typing.TypeVar("T", bound=[int, str, float])

# class ObservableProperty(typing.Generic[typing.Type], QObject):
#     valueChanged = pyqtSignal((T), name="valueChanged")

#     def __init__(self, prop:T) -> None:
#         super().__init__()
#         self._prop:typing.Optional[T]=None
#         pass

#     def get(self)->typing.Optional[T]:
#         if self._prop:
#             return self._prop
#         return None

#     def set(self, value:T)->None:
#         if value != self._prop:
#             self._prop=value
#             self.valueChanged.emit(self._prop)
#         return
