import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class MyApp(QGuiApplication):

    def __init__(self):
        super().__init__()
        self._engine = QQmlApplicationEngine()

    def start_engine(self):
        self._engine.load(QUrl.fromLocalFile('app.qml'))

    def verify(self):
        if not self._engine.rootObjects():
            sys.exit(-1)

    def run(self):
        sys.exit(self.exec())


if __name__ == '__main__':
    app = MyApp()
    app.start_engine()
    app.verify()
    app.run()
