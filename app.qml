/*
Copyright 2023

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
*/


import QtQuick
import QtQuick.Controls


ApplicationWindow {
    width: 640
    height: 480
    flags: Qt.FramelessWindowHint | Qt.Window
    visible: true

    background: Rectangle {
       border.color: handler.active ? "green" : "red"
       border.width: 5
    }

    Item {
        anchors.fill: parent

        DragHandler {
            id: handler
            onActiveChanged: {
                if (active) startSystemMove()
            }
        }
    }
}
