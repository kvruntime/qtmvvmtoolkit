from qtmvvmkit.observables.properties.observableproperty import ObservableProperty


class ObservaleStrProperty(ObservableProperty):
    def __init__(self, prop: str) -> None:
        super().__init__(prop)
        pass

    def set(self, value: str):
        return super().set(str(value))
    pass
