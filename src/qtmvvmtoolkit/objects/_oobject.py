# -*- coding:utf-8 -*-

from qtpy.QtCore import QObject
from qtpy.QtWidgets import QApplication, QWidget
from loguru import logger


class ObservableObject(QObject):
    def __init__(self):
        super().__init__()
        self._logger = logger
        return

    def update_viewmodel(self) -> None:
        return None

    def get_current_opened_widget(self) -> QWidget:
        current_widget = [w for w in QApplication.topLevelWidgets() if w.isVisible()][0]
        return current_widget
