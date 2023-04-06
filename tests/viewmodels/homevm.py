import typing

from qtmvvmtoolkit.observables.objects import ObservableObject
from qtmvvmtoolkit.observables.properties import ComputedObservableIntProperty
from qtmvvmtoolkit.observables.properties import ObservableIntProperty, ObservableStrProperty


class HomeViewModel(ObservableObject):
    def __init__(self):
        super().__init__()

        self.username = ObservableStrProperty("named")
        self.voltage = ObservableIntProperty(2)
        self.capacity = ObservableIntProperty(100)
        self.energy = ComputedObservableIntProperty(10, [self.voltage, self.capacity], self.compute_energy)
        pass

    def compute_energy(self) -> typing.Type[int]:
        _energy = self.voltage.get() * self.capacity.get()
        print(_energy)
        # self.energy.set(_energy)
        return _energy

