# coding:utf-8
import typing

from pydantic import BaseModel
from loguru import logger
from context import register_package
from qtpy.QtCore import QCoreApplication

register_package()
from qtmvvmtoolkit.inputs import ObservableObject


def handle_changes(name: str, value: typing.Any) -> None:
    print(f"name:{name} & value:{value}")
    return


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        return


class User2(BaseModel):
    name: str = "default"
    age: int = 0


app = QCoreApplication([])

user_val = User2(name="jean", age=20)
u = ObservableObject(user_val)
u.valueChanged.connect(handle_changes)

u.set("name", "victor")
u.set("age", 78)
u.display_object()
print(user_val)

app.exec()
