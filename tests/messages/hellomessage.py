from qtmvvmtoolkit.messenger import Message


class HelloMessage(Message[str]):
    def __init__(self, value: str) -> None:
        super().__init__(value)
        return
