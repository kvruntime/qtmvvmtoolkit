from .router import Router
from typing import Dict
from PyQt6.QtWidgets import QWidget, QStackedWidget
from PyQt6.QtCore import QObject


class StackWidgetRouter(Router):
    def __init__(self, outlet: QStackedWidget) -> None:
        super().__init__(outlet)
        self.outlet = outlet
        self.routes: Dict[str, QWidget] = {}
        pass

    def registerRoute(self, path: str, element: QObject):
        self.routes[path] = element  # type: ignore
        return None

    def goTo(self, path: str):
        _page = self.routes.get(path)
        if _page:
            self.outlet.setCurrentWidget(_page)
        return None
    
    def goToNext(self):
        return None
    
    def goToPrevious(self):
        return None
