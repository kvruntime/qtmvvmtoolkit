import random
import string
import typing
from pathlib import Path
from typing import Generic, List, Type, TypeVar

import pandas as pd
from pydantic import BaseModel, Field
from PyQt6.QtCore import QCoreApplication, pyqtBoundSignal
from qtpy.QtCore import QObject, Signal

T = TypeVar("T")


class BaseTypes:
    def __init__(self) -> None:
        self.types_list: List[type] = [
            object,
            int,
            float,
            str,
            bool,
            pd.DataFrame,
            Path,
        ]
        self.types: List[list[type]] = [[t] for t in self.types_list]
        return

    def add_newtype(self, typ: type) -> None:
        self.types_list.append(typ)
        self.types.append([typ])
        return


class User(BaseModel):
    name: str = Field(
        default_factory=lambda: "".join(random.choices(list(string.ascii_letters), k=9))
    )
    age: int = 18


base_types = BaseTypes()
base_types.add_newtype(User)


class IObservableProperty(QObject):
    valueChanged = Signal(name="valueChanged")

    def get(self) -> typing.Any:
        ...

    def set(self, value: typing.Any):
        ...

    def binding(self, method: typing.Callable[..., None]) -> None:
        """One way binding"""
        ...

    def rbinding(self, signal: pyqtBoundSignal) -> None:
        """Reverse binding method"""
        ...


class ObservableProperty(IObservableProperty, Generic[T]):
    valueChanged = Signal(*base_types.types, name="valueChanged")

    def __init__(self, value: T):
        super().__init__()
        self.value: T = value
        self.set(value)
        return

    def get(self) -> T:
        return self.value

    def set(self, value: T):
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


class ComputedObservableProperty(QObject, Generic[T]):
    valueChanged = Signal(*base_types.types, name="valueChanged")

    def __init__(
        self,
        value: T,
        observable_props: typing.List[IObservableProperty],
        update_function: typing.Callable[..., T],
    ) -> None:
        super().__init__()
        self.value: T = value
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

    def binding(self, method: typing.Callable[..., None]) -> None:
        """One way binding"""
        self.valueChanged.connect(method)
        self.valueChanged.emit(self.get())
        return None


def connection(arg: int) -> None:
    print(arg)
    return None


def user_info(arg: User) -> None:
    return print(arg)


app = QCoreApplication([])
one = ObservableProperty(19)
user_data = ObservableProperty(User())
user_role = ComputedObservableProperty(User(), [user_data], lambda: User())
user_data.set(User(name="viktor"))
one.binding(connection)
user_data.binding(user_info)
user_role.binding(user_info)


app.exec()
