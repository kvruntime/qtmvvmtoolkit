# coding:utf-8
import typing
from typing import Any, Callable, Generic, TypeVar

# from qtpy.QtCore import pyqtBoundSignal
# from qtpy.QtCore import Signal
# from pydantic import BaseModel
# from PyQt6.QtCore import QCoreApplication, QObject, pyqtSignal
from loguru import logger
from qtpy.QtCore import QObject, Signal
from qtpy.QtWidgets import QComboBox

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

    def pop(self, index: int) -> _T:
        _poped = self.value.pop(index)
        return _poped

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

    def __getitem__(self, index: int) -> _T:
        return self.value[index]

    def __len__(self) -> int:
        return len(self.value)

    def __contains__(self, item: _T) -> bool:
        return item in self.value

    def __iter__(self) -> typing.Iterator[_T]:
        return iter(self.value)


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


class ObservableObject(QObject):
    valueChanged = Signal(str, object)

    def __init__(self, obj: object) -> None:
        super().__init__(None)
        self._observed = obj
        return

    def set(self, attr: str, value: typing.Any) -> None:
        if hasattr(self._observed, attr):
            if type(value) == type(getattr(self._observed, attr)):
                self.valueChanged.emit(attr, value)
                setattr(self._observed, attr, value)
                return None
            logger.warning(f"{attr} not found in {self._observed}")
        return None

    def get(self, attr: str) -> typing.Any:
        if hasattr(self._observed, attr):
            return getattr(self._observed, attr)
        logger.warning(f"{attr} not found in {self._observed}")
        return None

    def has_attr(self, attr: str) -> bool:
        return hasattr(self._observed, attr)

    def rbinding(self, attr: str, value: typing.Any) -> None:
        if hasattr(self._observed, attr):
            if type(value) == type(getattr(self._observed, attr)):
                # apply modification only when type is value
                pass
            self.valueChanged.emit(attr, value)
            setattr(self._observed, attr, value)
        return None

    def display_object(self) -> None:
        print(self._observed)
        print(self._observed.__dict__)
        return None

    def export_dict(self) -> typing.Dict[str, typing.Any]:
        return {
            k: v for k, v in self._observed.__dict__.items() if not k.startswith("__")
        }


def handle_changes(name: str, value: typing.Any) -> None:
    print(f"name:{name} & value:{value}")
    return


class ObservableObjectDev(typing.Generic[_T]):
    def __init__(self, obj: _T) -> None:
        super().__init__()
        self.obj = obj

        self.obj_type = type(self.obj)
        self.__initialize_observables()
        return

    def __initialize_observables(self) -> None:
        attributes = [
            attr
            for attr in self.obj.__dir__()
            if not attr.startswith("__")
            if not callable(getattr(self.obj, attr))
        ]
        for attr_name in attributes:
            attr_type = type(getattr(self, attr_name, None))
            setattr(self, attr_name, ObservableProperty[attr_type](attr_type()))
        return None

    def set(self, value: typing.Any) -> None:
        return None

    def get(self) -> None:
        return None

    def binding_port(self) -> type[_T]:
        return self.obj_type
