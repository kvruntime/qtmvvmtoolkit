# -*- coding:utf-8 -*-
import logging

from qtpy.QtCore import QObject
from qtpy.QtWidgets import QApplication, QWidget


class ObservableObject(QObject):
    def __init__(self):
        super().__init__()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.NOTSET)

        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(logging.NOTSET)
        self._logger.addHandler(stream_handler)
        return

    def update_viewmodel(self) -> None:
        return None

    def get_current_opened_widget(self) -> QWidget:
        current_widget = [w for w in QApplication.topLevelWidgets() if w.isVisible()][0]
        return current_widget
