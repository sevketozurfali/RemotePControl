from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl, QObject
from PyQt5.QtWidgets import QApplication
import sys


def run():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    engine.load('ui.qml')
    win = engine.rootObjects()[0]

    # testButton = engine.findChild(QObject, "myButton")
    # testButton.messageSend.connect(myfunction)
    # testButton.clicked.connect(myfunction)

    # testitem = engine.findChild(QObject, "butest")
    # testitem.clicked.connect(myfunction)

    buttoning = win.findChild(QObject, "firsttabbutton")
    buttoning.clicked.connect(myfunction)


    # button_text = win.findChild(QObject, "first_tab_border")
    # button_text.opacity = 0

    

    # testingitem = engine.findChild(QObject, "butesting")
    # testingitem.clicked.connect(myfunction)
    # testingitem.clicked.connect(myfunction)

    if not engine.rootObjects():
        return -1

    return app.exec_()



def myfunction():
    print ("Hello button1 clicked.")




if __name__ == "__main__":
    myfunction()
    sys.exit(run())