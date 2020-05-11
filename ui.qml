import QtQuick.Window 2.2
import QtQuick 2.6
import QtQuick.Controls 1.3
import QtQuick.Layouts 1.1
import QtQuick.Dialogs 1.1
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4

Window {
    visible:true
    width:1024
    height:720
    Image {
        id: layer_0
        source: "images/layer_0.png"
        x: 0
        y: 0
        opacity: 1
    }
    Image {
        id: bg
        source: "images/bg.png"
        x: -1
        y: -7
        opacity: 1
    }
    Image {
        id: newbattery
        source: "images/newbattery.png"
        x: 385
        y: 555
        opacity: 1
    }

    
    Image {
        id: backgroundline
        source: "images/backgroundline.png"
        x: 13
        y: 9
        opacity: 1
    }
    Image {
        id: secondtab
        source: "images/secondtab.png"
        x: 562
        y: 652
        opacity: 0
    }
    Image {
        id: thirdtab
        source: "images/thirdtab.png"
        x: 776
        y: 653
        opacity: 1
    }
    Image {
        id: firsttab
        source: "images/firsttab.png"
        x: 350
        y: 653
        opacity: 0
    }
    Button {
        x : 345
        y : 650
        objectName : "firsttabbutton"
        iconSource : "images/firsttab.png"

        style: ButtonStyle {
            background: Rectangle {
                implicitWidth: 50
                implicitHeight: 5
                border.width: control.activeFocus ? 2 : 1
                border.color: "transparent"
                radius: 4
                gradient: Gradient {
                    GradientStop { position: 0 ; color: control.pressed ? "transparent" : "transparent" }
                    GradientStop { position: 1 ; color: control.pressed ? "transparent" : "transparent" }
                }
                Text {
                    id: st_text
                    anchors.centerIn: parent
                    text: "System"
                    font.bold: true
                    font.pixelSize: 15
                    color : control.pressed ? "#336699" : "#0099FF";
                }
            }
        }
        onClicked: {
            firsttab.opacity = 1
            secondtab.opacity = 0
            stack.pop()
        }
    }

    Button {
        x : 558
        y : 649
        objectName : "secondtabbutton"
        iconSource : "images/secondtab.png"

        style: ButtonStyle {
            background: Rectangle {
                implicitWidth: 50
                implicitHeight: 5
                border.width: control.activeFocus ? 2 : 1
                border.color: "transparent"
                radius: 4
                gradient: Gradient {
                    GradientStop { position: 0 ; color: control.pressed ? "transparent" : "transparent" }
                    GradientStop { position: 1 ; color: control.pressed ? "transparent" : "transparent" }
                }
                Text {
                    id: st_text
                    anchors.centerIn: parent
                    text: "Media"
                    font.bold: true
                    font.pixelSize: 15
                    color : control.pressed ? "#336699" : "#0099FF";
                }
            }
        }
        onClicked: {
            secondtab.opacity = 1
            firsttab.opacity = 0
            stack.push(page2)
        }
    }
    StackView{
        id: stack
        x: 30
        y: 30
        width: 960
        height: 610
        initialItem : page1

        Rectangle {
            id: page1
            color: "transparent"

            Image {
                id: scale
                source: "images/scale.png"
                x: 353
                y: 205
                opacity: 1
            }

            Label {
                id : labelone
                text : "Hello lightgreen"
                x : 400
                y : 400

            }

        }

        Rectangle {
            id : page2
            color : "transparent"

            Image {
                id: ibre
                source: "images/ibre.png"
                x: 492
                y: 363
                opacity: 1
            }
             CircularGauge {
                x: 400
                y: 200
                style: CircularGaugeStyle {
                    needle: Rectangle {
                        y: outerRadius * 1
                        implicitWidth: outerRadius * 0.03
                        implicitHeight: outerRadius * 0.9
                        antialiasing: true
                        color: Qt.rgba(0.66, 0.3, 0, 1)
                    }
                }
            }           
        }

        Component{
            id : view
        

            MouseArea {
                Text {
                    text: stack.depth
                    anchors.centerIn: parent
                }
                onClicked: stack.push(view)
            }
        }
    }
}
