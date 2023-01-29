from PyQt6.QtWidgets import QPushButton, QWidget, QToolButton
from typing import Optional
from qtmvvmkit.navigations.router import Router
from pathlib import Path
from PyQt6.QtGui import QIcon


class NavButton(QPushButton):
    def __init__(
        self,
        parent: Optional[QWidget] = None,
        *,
        text: str = "",
        router: Router | None = None,
        path: str = "",
        icon_path: Path = Path()
    ):
        super().__init__()
        self.setParent(parent) if parent else None
        self.setText(text)
        self.router = router
        self.path = path
        self.setIcon(QIcon(icon_path.as_posix()))

        self._binds()
        pass

    def _change_page(self):
        if self.router:
            self.router.goTo(self.path)
        return None

    def _binds(self):
        self.clicked.connect(self._change_page)
        return None

    def add_router(self, router: Router):
        self.router = router
        return

    def set_path(self, path: str):
        self.path = path
        return None
