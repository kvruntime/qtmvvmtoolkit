import random

from qtmvvmtoolkit.objects import ObservableObject
from qtmvvmtoolkit.inputs import (
    ObservableBoolProperty,
    ObservableIntProperty,
    ObservableStrProperty,
    ObservableFloatProperty,
    ObservableCollection,
    ComputedObservableBoolProperty,
    RelayableProperty,
    ComputedObservableFloatProperty
)
import string


class HomeViewModel(ObservableObject):
    def __init__(self):
        super().__init__()
        self.numbers = ObservableCollection(list(range(10)))
        self.valid_numbers = ComputedObservableBoolProperty(
            self.update_valid_numbers(),
            [self.numbers],
            self.update_valid_numbers
        )

        self.username = ObservableStrProperty("named")
        self.voltage = ObservableIntProperty(48)
        self.capacity = ObservableFloatProperty(100)
        self.energy = ComputedObservableFloatProperty(
            self.compute_energy(),
            [self.voltage, self.capacity],
            self.compute_energy
        )
        self.hide = ObservableBoolProperty(False)
        self.infos = ObservableCollection[str](["user"])

        self.changed = RelayableProperty()
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
        new_name = "".join(random.choices(list(string.ascii_letters), k=10))
        self.infos.append(new_name)
        if len(self.numbers.get()) != 0:
            return self.numbers.set([])
        if len(self.numbers.get()) == 0:
            return self.numbers.set(list(range(10)))
