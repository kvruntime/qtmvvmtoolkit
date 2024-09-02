# coding:utf-8


from pydantic import BaseModel
from qtmvvmtoolkit.inputs import observable_object


@observable_object
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        return


@observable_object
class UserInfo(BaseModel):
    name: str = "vik"
    age: int = 25


class UserViewModel:
    def __init__(self):
        super().__init__()
        # self.user = User("victor", 20)
        self.user = UserInfo()
        # Messenger.Default.use(HelloMessage, self.command_handle_message)
        return

    def command_display_user(self) -> None:
        print(self.user.get_attribute())
        return None

    # def command_handle_message(self, message: str) -> None:
    #     print(f"handle message==>{message}")
    #     return
