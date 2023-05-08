import typing

from PyQt6.QtWidgets import QStackedWidget, QWidget


class NavigationManager:
    def __init__(
        self,
        outlet: typing.Optional[QStackedWidget] = None,
        routes: typing.Optional[typing.Dict[typing.Any, typing.Any]] = None,
    ) -> None:
        self._outlet = outlet or QStackedWidget()
        self._routes = routes or {}
        pass

    def goto(self, path: str):
        if element := self._routes.get(path):
            self._outlet.setCurrentWidget(element)
        return None

    def register_route(self, *, path: str, element: QWidget):
        if not path or not element:
            return None
        self._routes[path] = element
        return None

    def set_outlet(self, outlet: QStackedWidget):
        self._outlet = outlet
        return None

    pass
