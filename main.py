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


class MyApp(QGuiApplication):

    def __init__(self):
        super().__init__()
        self._engine = QQmlApplicationEngine()

        self._border_width = 8
        self._native_event_filter = None

    def install_event_filter(self):
        if sys.platform == "win32":
            from win import WindowsEventFilter
            self._native_event_filter = WindowsEventFilter(self._border_width)
            self.installNativeEventFilter(self._native_event_filter)
        elif sys.platform == 'linux':
            from linux import LinuxEventFilter
            self._native_event_filter = LinuxEventFilter(self._border_width)

    def start_qml_engine(self):
        self._engine.load(QUrl.fromLocalFile('app.qml'))

    def add_window_effects(self):
        if sys.platform == "win32":
            hwnd = self.topLevelWindows()[0].winId()
            from win import WindowsWindowEffect
            self._effects = WindowsWindowEffect()
            self._effects.addShadowEffect(hwnd)
            self._effects.addWindowAnimation(hwnd)

    def verify(self):
        if not self._engine.rootObjects():
            sys.exit(-1)

    def run(self):
        sys.exit(self.exec())


if __name__ == '__main__':
    app = MyApp()
    app.install_event_filter()
    app.start_qml_engine()
    app.add_window_effects()
    app.verify()
    app.run()
