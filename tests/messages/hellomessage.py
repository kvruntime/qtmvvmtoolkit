from qtmvvmtoolkit.messenger import Message


class HelloMessage(Message[str]):
    def __init__(self, value: str) -> None:
        super().__init__(value)
        return


class StateChangedMessage(Message[bool]):
    def __init__(self, value: bool) -> None:
        super().__init__(value)
        return
