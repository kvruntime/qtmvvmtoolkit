from PyQt6.QtWidgets import QPushButton, QWidget
from typing import Optional
from .router import Router


class NavButton(QPushButton):
    def __init__(self, parent: Optional[QWidget] = None,*,  text: str = "", router: Router | None = None, path: str = ""):
        super().__init__()
        self.setText(text)
        self.router = router
        self.path = path

        self._binds()
        pass

    def _changePage(self):
        if self.router:
            self.router.goTo(self.path)
        return None

    def _binds(self):
        self.clicked.connect(self._changePage)
        return None

    def addRouter(self, router: Router):
        self.router = router
        return

    def setPath(self, path: str):
        self.path = path
        return None

    # def setText(self, text: str):
    #     # FIXME: class already implement setText function (possible bug)
    #     self.setText(text)
    #     return None
