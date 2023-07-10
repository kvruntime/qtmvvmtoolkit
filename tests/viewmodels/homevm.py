import typing

from qtmvvmtoolkit.inputs.computedproperty import ComputedObservableIntProperty, ComputedObservableBoolProperty
from qtmvvmtoolkit.objects.observable_object import ObservableObject
from qtmvvmtoolkit.inputs.observableproperty import (
    ObservableBoolProperty,
    ObservableIntProperty,
    ObservableStrProperty,
    ObservableFloatProperty
)
from qtmvvmtoolkit.inputs.relayableproperty import RelayableProperty
from qtmvvmtoolkit.inputs.observable_collection import ObservableCollection


class HomeViewModel(ObservableObject):
    def __init__(self):
        super().__init__()
        self.numbers = ObservableCollection(list(range(10)))
        self.valid_numbers = ComputedObservableBoolProperty(
            False,
            [self.numbers],
            self.update_valid_numbers
        )

        self.username = ObservableStrProperty("named")
        self.voltage = ObservableIntProperty(2)
        self.capacity = ObservableFloatProperty(100)
        self.energy = ComputedObservableIntProperty(
            10, [self.voltage, self.capacity], self.compute_energy
        )
        self.hide = ObservableBoolProperty(False)
        self.infos = ObservableCollection[str](["user"])
        self.infos.valueChanged.connect(lambda value: print(value))

        self.changed = RelayableProperty()
        return

    def update_valid_numbers(self) -> bool:
        _validation = len(self.numbers.get()) != 0
        print(self, _validation)
        return _validation

    def compute_energy(self) -> typing.Type[int]:
        return self.voltage.get() * self.capacity.get()

    def command_call_relay(self):
        self.changed.call()
        # self.hide.set(not self.hide.get())
        return None

    def fill_numbers(self) -> None:
        print(self.numbers.get())
        print("is valid", self.valid_numbers.get())
        if len(self.numbers.get()) != 0:
            print("emptying")
            self.numbers.set([])
            return None
        if len(self.numbers.get()) == 0:
            print("filling")
            self.numbers.set(list(range(10)))
            return None
        return None
