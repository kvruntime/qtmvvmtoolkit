# coding:utf-8

from messages.hellomessage import HelloMessage

from qtmvvmtoolkit.inputs import ObservableObject
from qtmvvmtoolkit.messenger import Messenger


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
        Messenger.Default.use(HelloMessage, self.command_handle_message)
        return

    def command_display_user(self) -> None:
        print(self.ou.display_object())
        print(self.u.__dict__)
        return None

    def command_handle_message(self, message: str) -> None:
        print(f"handle message==>{message}")
        return
