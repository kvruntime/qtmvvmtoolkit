import typing


from qtmvvmtoolkit.observables import (
     ObservableIntProperty, ObservableStrProperty, ComputedObservableIntProperty,ObservableObject
)
from qtmvvmtoolkit.observables.relayableproperty import RelayableProperty


class HomeViewModel(ObservableObject):
    def __init__(self):
        super().__init__()

        self.username = ObservableStrProperty("named")
        self.voltage = ObservableIntProperty(2)
        self.capacity = ObservableIntProperty(100)
        self.energy = ComputedObservableIntProperty(10, [self.voltage, self.capacity], self.compute_energy)

        self.changed = RelayableProperty()
        pass

    def compute_energy(self) -> typing.Type[int]:
        _energy = self.voltage.get() * self.capacity.get()
        return _energy

    def command_call_relay(self):
        self.changed.call()
        return None
