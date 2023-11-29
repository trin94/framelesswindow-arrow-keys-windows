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
    id: appWindow

    width: 640
    height: 480
    flags: Qt.FramelessWindowHint | Qt.Window
    visible: true

    background: Rectangle {
       border.color: handler.active ? "green" : "red"
       border.width: 5
    }

    Rectangle {
        id: titleBar
        height: 40
        color: handler.active ? "green" : "red"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.rightMargin: 2
        anchors.leftMargin: 2
        anchors.topMargin: 2

        DragHandler {
            id: handler
            onActiveChanged: {
                if (active) {
                     appWindow.startSystemMove()
                 }
            }
        }

        Button {
            id: btnClose
            x: 1140
            text: 'Close'
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.rightMargin: 8
            anchors.topMargin: 8

            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor

                onReleased: {
                    appWindow.close()
                }
            }
        }

        Button {
            id: btnMaximizeRestore
            x: 1105
            text: 'Toggle Maximized'
            anchors.right: btnClose.left
            anchors.top: parent.top
            anchors.rightMargin: 0
            anchors.topMargin: 8

            onClicked: {
                if (appWindow.visibility === Window.Maximized) {
                    appWindow.showNormal()
                } else {
                    appWindow.showMaximized()
                }
            }
        }

        Button {
            x: 1070
            text: 'Minimize'
            anchors.right: btnMaximizeRestore.left
            anchors.top: parent.top
            anchors.rightMargin: 0
            anchors.topMargin: 8

            onClicked: {
                appWindow.showMinimized()
            }
        }
    }

}
