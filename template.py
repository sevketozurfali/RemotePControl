# Created by: PyQt5 UI code generator 5.14.2
# author : Sevket Ozurfali
# Email : sevketozurfali@gmail.com


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import threading
import libMain


class Ui_MainWindow(object):
    # ...........................................................Edit..........................
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.pool = QtCore.QThreadPool.globalInstance()
        self.pool.setMaxThreadCount(3)
        self.sound_output_indexes = []

    # .........................................................................................

    def setupUi(self, MainWindow):
        # .............................................................:edit...................
        self.client = libMain.libMain()
        # .....................................................................................
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.power_utilities = QtWidgets.QWidget()
        self.power_utilities.setObjectName("power_utilities")
        self.f_cpu = QtWidgets.QFrame(self.power_utilities)
        self.f_cpu.setGeometry(QtCore.QRect(0, 90, 281, 261))
        self.f_cpu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_cpu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_cpu.setObjectName("f_cpu")
        self.f_battery = QtWidgets.QFrame(self.power_utilities)
        self.f_battery.setGeometry(QtCore.QRect(290, 90, 361, 261))
        self.f_battery.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_battery.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_battery.setObjectName("f_battery")
        self.f_ram = QtWidgets.QFrame(self.power_utilities)
        self.f_ram.setGeometry(QtCore.QRect(660, 90, 321, 261))
        self.f_ram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_ram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_ram.setObjectName("f_ram")
        self.tabWidget.addTab(self.power_utilities, "")
        self.sound_utilities = QtWidgets.QWidget()
        self.sound_utilities.setObjectName("sound_utilities")
        self.f_sound_source = QtWidgets.QFrame(self.sound_utilities)
        self.f_sound_source.setGeometry(QtCore.QRect(0, 130, 331, 221))
        self.f_sound_source.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_sound_source.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_sound_source.setObjectName("f_sound_source")
        self.combi_sound_output = QtWidgets.QComboBox(self.f_sound_source)
        self.combi_sound_output.setGeometry(QtCore.QRect(20, 20, 291, 33))
        self.combi_sound_output.setObjectName("combi_sound_output")
        self.f_media_player = QtWidgets.QFrame(self.sound_utilities)
        self.f_media_player.setGeometry(QtCore.QRect(330, 130, 321, 221))
        self.f_media_player.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_media_player.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_media_player.setObjectName("f_media_player")
        self.btn_play_pause = QtWidgets.QPushButton(self.f_media_player)
        self.btn_play_pause.setGeometry(QtCore.QRect(110, 80, 88, 33))
        self.btn_play_pause.setObjectName("btn_play_pause")
        self.f_volume_control = QtWidgets.QFrame(self.sound_utilities)
        self.f_volume_control.setGeometry(QtCore.QRect(650, 130, 331, 221))
        self.f_volume_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_volume_control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_volume_control.setObjectName("f_volume_control")
        self.btn_volume_up = QtWidgets.QPushButton(self.f_volume_control)
        self.btn_volume_up.setGeometry(QtCore.QRect(20, 20, 131, 33))
        self.btn_volume_up.setObjectName("btn_volume_up")
        self.btn_volume_mute = QtWidgets.QPushButton(self.f_volume_control)
        self.btn_volume_mute.setGeometry(QtCore.QRect(110, 150, 88, 33))
        self.btn_volume_mute.setObjectName("btn_volume_mute")
        self.btn_volume_down = QtWidgets.QPushButton(self.f_volume_control)
        self.btn_volume_down.setGeometry(QtCore.QRect(167, 20, 121, 33))
        self.btn_volume_down.setObjectName("btn_volume_down")
        self.tabWidget.addTab(self.sound_utilities, "")
        self.control_utilities = QtWidgets.QWidget()
        self.control_utilities.setObjectName("control_utilities")
        self.f_qr_code = QtWidgets.QFrame(self.control_utilities)
        self.f_qr_code.setGeometry(QtCore.QRect(0, 90, 301, 261))
        self.f_qr_code.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_qr_code.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_qr_code.setObjectName("f_qr_code")
        self.lbl_qr_code = QtWidgets.QLabel(self.f_qr_code)
        self.lbl_qr_code.setGeometry(QtCore.QRect(10, 0, 291, 181))
        self.lbl_qr_code.setObjectName("lbl_qr_code")
        self.btn_refresh_server = QtWidgets.QPushButton(self.f_qr_code)
        self.btn_refresh_server.setGeometry(QtCore.QRect(30, 190, 231, 33))
        self.btn_refresh_server.setObjectName("btn_refresh_server")
        self.f_pc_controls = QtWidgets.QFrame(self.control_utilities)
        self.f_pc_controls.setGeometry(QtCore.QRect(300, 90, 291, 261))
        self.f_pc_controls.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_pc_controls.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_pc_controls.setObjectName("f_pc_controls")
        self.line_password = QtWidgets.QLineEdit(self.f_pc_controls)
        self.line_password.setGeometry(QtCore.QRect(20, 30, 251, 33))
        self.line_password.setObjectName("line_password")
        self.lbl_password = QtWidgets.QLabel(self.f_pc_controls)
        self.lbl_password.setGeometry(QtCore.QRect(20, 10, 71, 17))
        self.lbl_password.setObjectName("lbl_password")
        self.btn_pc_shutdown = QtWidgets.QPushButton(self.f_pc_controls)
        self.btn_pc_shutdown.setGeometry(QtCore.QRect(20, 110, 251, 33))
        self.btn_pc_shutdown.setObjectName("btn_pc_shutdown")
        self.btn_pc_reset = QtWidgets.QPushButton(self.f_pc_controls)
        self.btn_pc_reset.setGeometry(QtCore.QRect(20, 140, 251, 33))
        self.btn_pc_reset.setObjectName("btn_pc_reset")
        self.btn_pc_suspend = QtWidgets.QPushButton(self.f_pc_controls)
        self.btn_pc_suspend.setGeometry(QtCore.QRect(20, 170, 251, 33))
        self.btn_pc_suspend.setObjectName("btn_pc_suspend")
        self.btn_pc_lock = QtWidgets.QPushButton(self.f_pc_controls)
        self.btn_pc_lock.setGeometry(QtCore.QRect(20, 200, 251, 33))
        self.btn_pc_lock.setObjectName("btn_pc_lock")
        self.chckbox_remember = QtWidgets.QCheckBox(self.f_pc_controls)
        self.chckbox_remember.setGeometry(QtCore.QRect(20, 70, 241, 23))
        self.chckbox_remember.setObjectName("chckbox_remember")
        self.f_about = QtWidgets.QFrame(self.control_utilities)
        self.f_about.setGeometry(QtCore.QRect(590, 90, 391, 261))
        self.f_about.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_about.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_about.setObjectName("f_about")
        self.lbl_about = QtWidgets.QLabel(self.f_about)
        self.lbl_about.setGeometry(QtCore.QRect(10, 10, 371, 241))
        self.lbl_about.setObjectName("lbl_about")
        self.tabWidget.addTab(self.control_utilities, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1023, 25))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionExit)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connections...........................................................
        self.btn_play_pause.clicked.connect(self.working_worker)
        self.tabWidget.currentChanged.connect(self.working_worker)
        self.combi_sound_output.currentIndexChanged.connect(self.slot_changed_media_output)
        self.btn_volume_mute.clicked.connect(self.slot_mute)
        self.btn_volume_down.clicked.connect(self.slot_decrease_volume)

        #......................................................................
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.power_utilities), _translate("MainWindow", "Tab 1"))
        self.btn_play_pause.setText(_translate("MainWindow", "Play/Pause"))
        self.btn_volume_up.setText(_translate("MainWindow", "Volume UP + "))
        self.btn_volume_mute.setText(_translate("MainWindow", "Mute"))
        self.btn_volume_down.setText(_translate("MainWindow", "Volume Down -"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sound_utilities), _translate("MainWindow", "Tab 2"))
        self.lbl_qr_code.setText(_translate("MainWindow", "QR Code is in here"))
        self.btn_refresh_server.setText(_translate("MainWindow", "Refresh"))
        self.lbl_password.setText(_translate("MainWindow", "Password"))
        self.btn_pc_shutdown.setText(_translate("MainWindow", "ShutDown"))
        self.btn_pc_reset.setText(_translate("MainWindow", "Reset"))
        self.btn_pc_suspend.setText(_translate("MainWindow", "Suspend"))
        self.btn_pc_lock.setText(_translate("MainWindow", "Lock"))
        self.chckbox_remember.setText(_translate("MainWindow", "Remember"))
        self.lbl_about.setText(_translate("MainWindow", "About"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.control_utilities), _translate("MainWindow", "Page"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

#.....................................................Edit..........................................
    def definitions(self):
        self.tabWidget.setTabText(0, "Power")
        self.tabWidget.setTabText(1, "Media")
        self.tabWidget.setTabText(2, "System")
        self.initialization()
        
    def initialization(self):
        for item in self.client.find_sound_devices():
            self.combi_sound_output.addItem(item.description)
            self.sound_output_indexes.append(item.index)

        # self.client.start_server_listenning()
    
    def working_worker(self):
        if(self.tabWidget.currentIndex() == 2):
            worker = Worker()
            self.pool.start(worker)


# Media......................................................................................................................................................................
    def slot_changed_media_output(self,new_index):
        print("New index : " ,new_index)
        self.client.set_sound_output(new_index)

    def slot_mute(self):
        self.client.set_sound_mute()

    def slot_decrease_volume(self):
        self.client.decrease_sound_volume()

# ...........................................................................................................................................................................

class Worker(QtCore.QRunnable):
    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        server = libMain.libMain()
        server.find_sound_devices()
        server.start_server()
        server.start_server_listenning()

# ............................................................................................

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # .......................................................edit................................
    ui.definitions()
    # ...........................................................................................
    MainWindow.show()
    sys.exit(app.exec_())