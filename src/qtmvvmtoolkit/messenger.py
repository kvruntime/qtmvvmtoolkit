import typing
from typing import Any, Callable, Generic, TypeVar

# from PyQt6.QtCore import *
from qtpy.QtCore import QObject, Signal, QCoreApplication

FuncT = typing.TypeVar("FuncT", bound=typing.Callable)


T = TypeVar("T")


class SigInst(Generic[T]):
    @staticmethod
    def connect(slot: Callable[[T], typing.Any], type: type | None = None) -> None:
        ...

    @staticmethod
    def disconnect(slot: Callable[[T], typing.Any] = typing.Any) -> None:
        ...

    @staticmethod
    def emit(*args: T) -> None:
        ...


class WorkerBaseSignals(QObject):
    message = Signal(object)  # emitted when the work is started


class Message(QObject, Generic[T]):
    message: SigInst[T]

    def __init__(self, value: T) -> None:
        super().__init__(None)
        self._value = value
        self.signals = WorkerBaseSignals()
        return

    def __getattr__(self, name: str) -> SigInst:
        attr = getattr(self.signals.__class__, name, None)
        if isinstance(attr, Signal):
            return getattr(self.signals, name)
        raise AttributeError(
            f"{self.__class__.__name__!r} object has no attribute {name!r}"
        )

    @property
    def value(self) -> T:
        return self._value

    @classmethod
    def name(cls) -> str:
        return cls.__name__

    def send(self) -> None:
        self.message.emit(self._value)
        return None

    def register(self, func: Callable[[T], Any]) -> None:
        self.message.connect(func)
        return None

    def unregister(self, func: Callable[[T], Any]) -> None:
        try:
            self.message.disconnect(func)
        except TypeError as ex:
            print("this function is not connected")
            raise ex
        return None


class Messenger:
    _Default: typing.Any

    def __init__(self) -> None:
        self._messages: typing.Dict[
            str, typing.List[typing.Callable[[], typing.Any]]
        ] = dict()
        return

    @classmethod
    @property
    def Default(cls):
        try:
            if Messenger._Default:
                return Messenger._Default
        except AttributeError:
            Messenger._Default = Messenger()
            return Messenger._Default

    def register(self, message: typing.Type[Message[Any]]) -> None:
        if not message.__name__ in self._messages.keys():
            self._messages.update({message.__name__: []})
        return None

    def use(self, message: typing.Type[Message[Any]], func: Callable[[T], Any]):
        if not message.__name__ in self._messages.keys():
            raise Exception(f"Message:{message.__name__}  doesn't exists")

        value: typing.List[typing.Any] = self._messages.get(message.__name__)
        if func in value:
            return None
        value.append(func)
        self._messages.update({message.__name__: value})
        return None

    def unuse(self, message: typing.Type[Message[Any]], func: Callable[[T], Any]):
        if message.__name__ in self._messages.keys():
            _funcs = self._messages.get(message.__name__)
            if func in _funcs:
                _funcs.remove(func)
            self._messages.update({message.__name__: _funcs})
        else:
            print("Message dont exists")
        return None

    def send(self, message: Message[Any]) -> None:
        _exists = message.__class__.__name__ in self._messages
        if _exists:
            _funcs = self._messages.get(message.__class__.__name__)
            for func in _funcs:
                message.register(func)
                message.send()
                message.unregister(func)
        return None


class IntMessage(Message[int]):
    pass


class StrMessage(Message[str]):
    pass


def operation(value: Any):
    print(f"value->{value}")
    return None


def s_operation(value: Any):
    print(f"()value()->{value}()")
    return None


def main() -> None:
    app = QCoreApplication([])

    Messenger.Default.register(IntMessage)
    Messenger.Default.register(StrMessage)

    Messenger.Default.use(IntMessage, operation)
    Messenger.Default.use(IntMessage, s_operation)
    Messenger.Default.use(StrMessage, operation)
    Messenger.Default.use(StrMessage, s_operation)

    Messenger.Default.send(IntMessage(6))
    Messenger.Default.send(StrMessage("sdfdsfdsf===>"))
    app.exec()
    return None


if __name__ == "__main__":
    main()
