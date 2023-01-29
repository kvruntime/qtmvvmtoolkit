from qtmvvmkit.observables.properties.observableproperty import ObservableProperty


class ObservaleIntProperty(ObservableProperty):
    def __init__(self, prop: int) -> None:
        super().__init__(prop)
        pass

    def set(self, value: int):
        return super().set(int(value))
    pass
