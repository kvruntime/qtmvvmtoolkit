# coding:utf-8
import typing
from typing import Any, Callable, Generic, TypeVar

from qtpy.QtCore import QObject, Signal
from qtpy.QtWidgets import QComboBox

# from qtpy.QtCore import pyqtBoundSignal
# from qtpy.QtCore import Signal


_T = TypeVar("_T")


class SigInst(Generic[_T]):
    @staticmethod
    def connect(slot: Callable[[_T], Any], type: type | None = ...) -> None: ...

    @staticmethod
    def disconnect(slot: Callable[[_T], Any] = ...) -> None: ...

    @staticmethod
    def emit(*args: _T) -> None: ...


class ObservableSignals(QObject):
    valueChanged = Signal(object)  # emitted when the work is started


# class ObservableSignals(QObject):
#     valueChanged = Signal(object)


# class SigInst(Generic[_T]):
#     @staticmethod
#     def connect(slot: Callable[[_T], Any], type: type | None = ...) -> None:
#         ...

#     @staticmethod
#     def disconnect(slot: Callable[[_T], Any] = ...) -> None:
#         ...

#     @staticmethod
#     def emit(*args: _T) -> None:
#         ...


# class IObservableProperty(QObject, Generic[_T]):
#     #  = Signal(name="valueChanged")
#     valueChanged: SigInst[_T]

#     def get(self) -> typing.Any:
#         ...

#     def set(self, value: typing.Any):
#         ...

#     def binding(self, method: typing.Callable[..., None]) -> None:
#         """One way binding"""
#         ...

#     def rbinding(self, signal: Signal) -> None:
#         """Reverse binding method"""
#         ...

#     def getattr(self, name: str) -> SigInst:
#         attr = getattr(self.signals.__class__, name, None)
#         if isinstance(attr, Signal):
#             return getattr(self.signals, name)
#         raise AttributeError(
#             f"{self.__class__.name!r} object has no attribute {name!r}"
#         )


class ObservableProperty(QObject, Generic[_T]):
    valueChanged: SigInst[_T]

    def __init__(self, value: _T):
        super().__init__(None)
        self.value: _T = value
        self.set(value)
        self.signals = ObservableSignals()
        return

    # def cast_data(self) -> None:
    #     self.valueChanged.emit(self.get())
    #     return None

    def get(self) -> _T:
        return self.value

    def set(self, value: _T):
        if value != self.value:
            self.value = value
            self.valueChanged.emit(self.value)
        return

    def binding(self, method: typing.Callable[..., None]) -> None:
        """One way binding"""
        self.valueChanged.connect(method)
        self.valueChanged.emit(self.get())
        return None

    def rbinding(self, signal: Signal) -> None:
        """Reverse binding method"""
        signal.connect(self.set)
        self.valueChanged.emit(self.get())
        return None

    def __getattr__(self, name: str) -> SigInst:
        attr = getattr(self.signals.__class__, name, None)
        if isinstance(attr, Signal):
            return getattr(self.signals, name)
        raise AttributeError(
            f"{self.__class__.name!r} object has no attribute {name!r}"
        )


class ComputedObservableProperty(QObject, Generic[_T]):
    valueChanged: SigInst[_T]

    def __init__(
        self,
        value: _T,
        observable_props: typing.List[ObservableProperty[typing.Any]],
        update_function: typing.Callable[..., _T],
    ) -> None:
        super().__init__()
        self.value: _T = value
        self.signals = ObservableSignals()
        self.update_function = update_function
        self.observable_props = observable_props

        for observable_prop in self.observable_props:
            observable_prop.valueChanged.connect(self.update)
        return

    def get(self) -> _T:
        return self.value

    def set(self, value: _T):
        self.value = value
        self.valueChanged.emit(self.value)
        return None

    def update(self) -> None:
        _result = self.update_function()
        self.set(_result)
        return None

    def binding(self, method: typing.Callable[..., None]) -> None:
        """One way binding"""
        self.valueChanged.connect(method)
        self.valueChanged.emit(self.get())
        return None

    def __getattr__(self, name: str) -> SigInst:
        attr = getattr(self.signals.__class__, name, None)
        if isinstance(attr, Signal):
            return getattr(self.signals, name)
        raise AttributeError(
            f"{self.__class__.name!r} object has no attribute {name!r}"
        )


class ObservableCollection(QObject, typing.Generic[_T]):
    valueChanged: SigInst[_T]

    def __init__(self, value: list[_T]) -> None:
        super().__init__()
        self.value = value
        self.signals = ObservableSignals()
        return None

    def get(self) -> list[_T]:
        return self.value

    def set(self, value: list[_T]) -> None:
        self.value = value
        self.valueChanged.emit(value)
        return None

    def clear(self) -> None:
        self.value.clear()
        self.valueChanged.emit(self.value)
        return None

    def append(self, value: _T) -> None:
        self.value.append(value)
        self.valueChanged.emit(self.value)
        return None

    def remove(self) -> None:
        self.valueChanged.emit(self.value)
        return None

    def extend(self, values: list[_T]) -> None:
        self.value.extend(values)
        self.valueChanged.emit(self.value)
        return None

    def binding(self, method: typing.Callable[[typing.Any], None]) -> None:
        """One way binding"""
        self.valueChanged.connect(method)
        self.valueChanged.emit(self.get())
        return None

    def bind_combobox(self, widget: QComboBox):
        widget.clear()
        self.valueChanged.connect(widget.addItems)
        self.valueChanged.emit(self.value)
        return None

    def __getattr__(self, name: str) -> SigInst:
        attr = getattr(self.signals.__class__, name, None)
        if isinstance(attr, Signal):
            return getattr(self.signals, name)
        raise AttributeError(
            f"{self.__class__.name!r} object has no attribute {name!r}"
        )

    # pop
    # __getitem__
    # index
    # __len__
    # __contains__
    # __iter__


class RelayableProperty(QObject):
    """Property that call a method when called.
    this signal will be sent ; as response, a function will be called
    """

    relayed = Signal(name="relayed")

    def __init__(self) -> None:
        super().__init__()
        return

    def call(self) -> None:
        self.relayed.emit()
        return None

    def binding(self, method: typing.Callable[[], None]) -> None:
        self.relayed.connect(method)
        return None
