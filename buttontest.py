from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl, QObject
from PyQt5.QtWidgets import QApplication
import sys


def run():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    engine.load('m.qml')
    if not engine.rootObjects():
        return -1

    return app.exec_()



def myfunction():
    print ("Hello button1 clicked.")




if __name__ == "__main__":
    myfunction()
    sys.exit(run())