from .router import Router
from typing import Dict
from PyQt6.QtWidgets import QWidget, QStackedWidget
from PyQt6.QtCore import QObject


class StackWidgetRouter(Router):
    def __init__(self, target: QStackedWidget) -> None:
        super().__init__(target)
        self.target = target
        self.routes: Dict[str, QWidget] = {}
        pass

    def register_route(self, path: str, element: QObject):
        self.routes[path] = element  # type: ignore
        return None

    def navigate_to(self, path: str):
        _page = self.routes.get(path)
        if _page:
            self.target.setCurrentWidget(_page)
        return None
    
    def next(self):
        return None
    
    def previous(self):
        return None
