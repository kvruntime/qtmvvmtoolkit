# coding:utf-8
import typing
from typing import Generic, TypeVar, Callable, Any

from PyQt6.QtCore import pyqtBoundSignal
from qtpy.QtCore import QObject, Signal


T = TypeVar("T")


_T = TypeVar("_T")


class SigInst(Generic[_T]):
    @staticmethod
    def connect(slot: Callable[[_T], Any], type: type | None = ...) -> None:
        ...

    @staticmethod
    def disconnect(slot: Callable[[_T], Any] = ...) -> None:
        ...

    @staticmethod
    def emit(*args: _T) -> None:
        ...


class ObservableSignals(QObject):
    valueChanged = Signal(object)  # emitted when the work is started


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

#     def rbinding(self, signal: pyqtBoundSignal) -> None:
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
    # valueChanged = Signal(*base_types.types, name="valueChanged")
    valueChanged: SigInst[_T]

    def __init__(self, value: _T):
        super().__init__(None)
        self.value: _T = value
        self.set(value)
        self.signals = ObservableSignals()
        return

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

    def rbinding(self, signal: pyqtBoundSignal) -> None:
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
        observable_props: typing.List[ObservableProperty[object]],
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
