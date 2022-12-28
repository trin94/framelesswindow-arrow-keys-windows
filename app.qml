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
            onActiveChanged: if (active) startSystemMove()
        }
    }
}
