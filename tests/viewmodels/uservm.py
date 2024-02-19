# coding:utf-8
import random
import string
from pathlib import Path

# from qtmvvmtoolkit.objects import ObservableObject
from qtmvvmtoolkit.inputs import (
    ComputedObservableProperty,
    ObservableCollection,
    ObservableObject,
    ObservableProperty,
    RelayableProperty,
)


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        return


class UserViewModel:
    def __init__(self):
        super().__init__()
        self.u = User("victor", 20)
        self.ou = ObservableObject(self.u)
        return

    def command_display_user(self) -> None:
        print(self.ou.display_object())
        print(self.u.__dict__)
        return None
