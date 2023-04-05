from qtmvvmtoolkit.observables.objects import ObservableObject
from qtmvvmtoolkit.observables.properties import ObservableStrProperty


class HomeViewModel(ObservableObject):
    def __init__(self):
        super().__init__()

        self.username = ObservableStrProperty("named")
    pass