import typing
from typing import Generic, TypeVar

from PyQt6 import QtCore
from PyQt6.QtCore import *

from qtmvvmtoolkit.inputs.observableproperty import ObservableProperty

T = TypeVar("T", int, str, float, object, bool)
Types = [[object], [int], [float], [str], [bool]]


class ComputedObservableProperty(QtCore.QObject, Generic[T]):
    valueChanged = QtCore.pyqtSignal(*Types, name="valueChanged")

    def __init__(
        self,
        value: T,
        observable_props: typing.List[ObservableProperty[typing.Any]],
        update_function: typing.Callable[[], T],
        item: T,
    ) -> None:
        super().__init__()
        self.value: T = value
        self.item: T = item
        self.update_function = update_function
        self.observable_props = observable_props

        for observable_prop in self.observable_props:
            observable_prop.valueChanged.connect(self.update)
        return

    def get(self) -> T:
        return self.value

    def set(self, value: T):
        # assert isinstance(value, self.item)
        self.value = value
        self.valueChanged.emit(self.value)
        return None

    def update(self) -> None:
        _result = self.update_function()
        self.set(_result)
        return None

    def binding(self, method: typing.Callable[[], None]) -> None:
        """One way binding"""
        self.valueChanged.connect(method)
        self.valueChanged.emit(self.get())
        return None


# FIXME: resolve type hint for remain computed properties
class ComputedObservableBoolProperty(ComputedObservableProperty[bool]):
    def __init__(
        self,
        value: bool,
        observable_props: typing.List[ObservableProperty[typing.Any]],
        update_function: typing.Callable[[], bool],
    ) -> None:
        super().__init__(value, observable_props, update_function, item=bool)
        return


class ComputedObservableFloatProperty(ComputedObservableProperty[float]):
    def __init__(
        self,
        value: float,
        observable_props: typing.List[ObservableProperty[typing.Any]],
        update_function: typing.Callable[..., float],
    ) -> None:
        super().__init__(value, observable_props, update_function, item=float)
        return


class ComputedObservableIntProperty(ComputedObservableProperty[int]):
    def __init__(
        self,
        value: int,
        observable_props: typing.Sequence[ObservableProperty[typing.Any]],
        update_function: typing.Callable[..., int],
    ) -> None:
        super().__init__(value, observable_props, update_function, item=int)
        pass


class ComputedObservableStrProperty(ComputedObservableProperty[str]):
    def __init__(
        self,
        value: str,
        observable_props: typing.List[ObservableProperty],
        update_function: typing.Callable[..., str],
    ) -> None:
        super().__init__(value, observable_props, update_function, item=str)
        return
