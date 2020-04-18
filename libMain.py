import libTcpServer
import socket
from random import randint
import pulsectl
import threading
from pynput.keyboard import Key, Controller
import psutil
import math


class libMain:
    
    def __init__(self):
        self.server = libTcpServer.tcpServer()
        self.keyboard = Controller()
        self.psutil = psutil

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

    def play_pause_sound(self):
        print("Music playing and pausing....")
        self.keyboard.press(Key.media_play_pause)

    def get_cpu_percent(self):
        self.cpu_per = self.psutil.cpu_percent(interval = 0.5)
        # print("Cpu : ",self.cpu_per)
        return str(self.cpu_per)

    def get_cpu_frequency(self):
        self.cpu_frequency = psutil.cpu_freq()
        return self.cpu_frequency

    def get_battery_status(self):
        self.battery = psutil.sensors_battery()
        self.status = self.battery.power_plugged

        return self.status
    
    def get_battery_level(self):
        self.battery_level = self.battery.percent
        return self.battery_level

    def get_memory_percent(self):
        self.memory = psutil.virtual_memory()
        self.memory_per = self.byte_to_gigabyte(self.memory[2])
        return str(self.memory_per)

    def byte_to_gigabyte(self, size):
	    # size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	    i = int(math.floor(math.log(size, 1024)))
	    p = math.pow(1024, i)
	    s = round(size / p, 2)
	    return s

    def get_core_temp(self):
        self.all_temps = psutil.sensors_temperatures()
        self.total_temp = 0

        print("Temp : " + str(self.all_temps["coretemp"][1]))

        for i in range(1,len(self.all_temps["coretemp"])):
            self.temp = self.all_temps["coretemp"][i][1]
            # print("temp : " + str(self.temp))
            self.total_temp = self.total_temp + self.temp

        self.average_temp = self.total_temp / (len(self.all_temps["coretemp"]) - 1)
        # print("Average temp : " + str(self.average_temp))

        return self.average_temp