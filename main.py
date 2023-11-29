# Copyright 2023
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from win import WindowsEventFilter as EventFilter
from win import WindowsWindowEffect as WindowEffect


class MyApp(QGuiApplication):

    def __init__(self):
        super().__init__()
        self._engine = QQmlApplicationEngine()

        self.event_filter = EventFilter(5)
        self.installNativeEventFilter(self.event_filter)
        self.win_utilities = WindowEffect()

    def start_engine(self):
        self._engine.load(QUrl.fromLocalFile('app.qml'))

        for win in self.allWindows():
            self.win_utilities.addShadowEffect(win.winId())
            self.win_utilities.addWindowAnimation(win.winId())

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
