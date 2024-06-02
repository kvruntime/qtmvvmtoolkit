# coding:utf-8
import random
import string

from messages.hellomessage import HelloMessage

from qtmvvmtoolkit.inputs import (
    ComputedObservableProperty,
    ObservableCollection,
    ObservableProperty,
    RelayableProperty,
)
from qtmvvmtoolkit.messenger import Messenger


from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str

    @property
    def infos(self):
        return f"{self.name}->({self.email})"


class HomeViewModel:
    def __init__(self):
        super().__init__()
        self.numbers = ObservableCollection[list[str]](list(range(10)))
        self.valid_numbers = ComputedObservableProperty[bool](
            self.update_valid_numbers(), [self.numbers], self.update_valid_numbers
        )
        self.state = ObservableProperty[bool](False)

        self.username = ObservableProperty[str]("named")
        self.counter = ObservableProperty[int](0)
        self.user = ObservableProperty[User](User(name="", email=""))
        self.voltage = ObservableProperty[int](48)
        self.capacity = ObservableProperty[float](100)
        self.energy = ComputedObservableProperty[float](
            self.compute_energy(), [self.voltage, self.capacity], self.compute_energy
        )
        self.hide = ObservableProperty[bool](False)
        self.infos = ObservableCollection[str]([f"user-{index}" for index in range(10)])
        self.user_infos = ObservableCollection[str](
            [User(name=f"user-{index}", email=f"email-{index}") for index in range(10)]
        )

        self.changed = RelayableProperty()

        Messenger.Default.register(HelloMessage)
        return

    def update_valid_numbers(self) -> bool:
        _validation = len(self.numbers.get()) != 0
        return _validation

    def compute_energy(self) -> float:
        return self.voltage.get() * self.capacity.get()

    def command_call_relay(self):
        self.changed.call()
        # self.hide.set(not self.hide.get())
        return None

    def fill_numbers(self) -> None:
        Messenger.Default.send(HelloMessage("new message sent"))
        new_name = "".join(random.choices(list(string.ascii_letters), k=10))
        self.infos.append(new_name)
        if len(self.numbers.get()) != 0:
            return self.numbers.set([])
        if len(self.numbers.get()) == 0:
            return self.numbers.set(list(range(10)))
