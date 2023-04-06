import typing
from PyQt6.QtWidgets import QWidget, QStackedWidget


class NavigationManager:

    def __init__(
        self,
        outlet: typing.Optional[QStackedWidget]=None,
        routes: typing.Optional[typing.Dict] = None
    ) -> None:
        self._outlet = outlet or QStackedWidget()
        self._routes: typing.Dict = routes or {} 
        pass

    def goto(self, path:str):
        element = self._routes.get(path)
        if element:
            self._outlet.setCurrentWidget(element)
        return None

    def register_route(self, *, path: str, element: QWidget):
        if not path or not element:
            return None
        self._routes[path]=element
        return None
    
    def set_outlet(self, outlet:QStackedWidget):
        self._outlet=outlet
        return None
    pass
