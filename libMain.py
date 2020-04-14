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
        pulse = pulsectl.Pulse("t")
        device_list = pulse.sink_list()
        print("Device list : {}" , device_list)