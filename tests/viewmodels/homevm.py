import typing

from qtmvvmtoolkit.inputs import (
    ComputedObservableIntProperty,
    ObservableBoolProperty,
    ObservableIntProperty,
    ObservableObject,
    ObservableStrProperty,
    RelayableProperty,
)


class HomeViewModel(ObservableObject):
    def __init__(self):
        super().__init__()

        self.username = ObservableStrProperty("named")
        self.voltage = ObservableIntProperty(2)
        self.capacity = ObservableIntProperty(100)
        self.energy = ComputedObservableIntProperty(
            10, [self.voltage, self.capacity], self.compute_energy
        )
        self.hide = ObservableBoolProperty(False)
        self.changed = RelayableProperty()
        pass

    def compute_energy(self) -> typing.Type[int]:
        return self.voltage.get() * self.capacity.get()

    def command_call_relay(self):
        self.changed.call()
        # self.hide.set(not self.hide.get())
        return None
