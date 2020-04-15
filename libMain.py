import libTcpServer
import socket
from random import randint
import pulsectl
import threading


class libMain:
    
    def __init__(self):
        self.server = libTcpServer.tcpServer()
        print("Start sequence starting....")

    def start_server(self):
        host_port = randint(1000, 9999)
        print("Host port : ", host_port)
        self.server.server_listen(host_port)

    def start_server_listenning(self):
        self.server.conn_listen()

    def find_sound_devices(self):
        self.pulse = pulsectl.Pulse("t")
        self.device_list = self.pulse.sink_list()
        print("Device list : {}" , self.device_list)
        return self.device_list

    def set_sound_output(self,sound_output_index):
        print("Sound ouptut index : " ,sound_output_index)
        self.selected_output_index = sound_output_index
        # self.pulse.sink_default_set(self.device_list[0])
        # self.pulse.sink_input_move()
        # self.pulse.sink_default_set(self.pulse.sink_list()[0])
        # self.pulse.sink_default_set(sound_output_index)
    
    def set_sound_mute(self):
        self.device_list = self.pulse.sink_list()

        if int(self.device_list[self.selected_output_index].mute) == 1:
            self.pulse.mute(self.device_list[self.selected_output_index], False)
        else:
            self.pulse.mute(self.device_list[self.selected_output_index], True)


    def decrease_sound_volume(self):
        self.pulse.volume_change_all_chans(self.device_list[self.selected_output_index], -0.01)
        # self.pulse.volume_set(self.device_list[self.selected_output_index], 0.1)

    def increase_sound_volume(self):
        self.pulse.volume_change_all_chans(self.device_list[self.selected_output_index], +0.01)