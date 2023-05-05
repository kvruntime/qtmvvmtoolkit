import logging

from PyQt6.QtCore import QObject

from .strproperty import ObservableStrProperty


class ObservableObject(QObject):
    def __init__(self):
        super().__init__()
        self.title: str = "ViewModel"

        self.title = ObservableStrProperty("ViewModel")

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.NOTSET)

        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(logging.NOTSET)
        self._logger.addHandler(stream_handler)
        pass
