import QtQuick.Window 2.2
import QtQuick 2.3
import QtQuick.Controls 1.4

Window{
    visible:true
    width:1024
    height : 720
    Image {
        id: bg
        source: "images/bg.png"
        x: 0
        y: -7
        opacity: 1
    }
    Button {
        text : "Hello"
    }
    Image {
        id: newbattery
        source: "images/newbattery.png"
        x: 385
        y: 555
        opacity: 1
    }
    Image {
        id: scale
        source: "images/scale.png"
        x: 353
        y: 205
        opacity: 1
    }
    Image {
        id: ibre
        source: "images/ibre.png"
        x: 492
        y: 363
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
        opacity: 1
    }
    Image {
        id: firsttab
        source: "images/firsttab.png"
        x: 350
        y: 653
        opacity: 1
    }
    Image {
        id: thirdtab
        source: "images/thirdtab.png"
        x: 776
        y: 653
        opacity: 1
    }
    
}

