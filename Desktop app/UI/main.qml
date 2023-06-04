import QtQuick
import QtQuick.Controls.Basic

ApplicationWindow {

    visible: true
    width: 400
    height: 600
    title: "HelloApp"
    property string currTime: "16:38:33"

    Rectangle {

        anchors.fill: parent

        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./img/playas.jpg"
            fillMode: Image.PreserveAspectCrop
        }

        Rectangle {

            anchors.fill: parent
            color: "transparent"

            Text {

                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }

                text: currTime
                font.pixelSize: 30
                color: "white"
            }
        }
    }
}