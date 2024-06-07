import context

context.__file__

from qtmvvmtoolkit.inputs import ObservableObjectDev


class User:
    def __init__(self) -> None:
        self.username: str = ""
        self.age: int = 0
        self.account: float = 0
        return


o_user = ObservableObjectDev[User](User())
print(o_user)
print(o_user.__dir__())
print(o_user.binding_port
