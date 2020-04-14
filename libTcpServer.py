import socket
class tcpServer:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def server_listen(self, host_port):
        # print("Server will be started in a sec. at ip ", socket.gethostname(), " port : ", host_port)
        # self.sock.bind((socket.gethostname(), host_port))
        self.sock.bind(('192.168.0.104', host_port))
        
        self.sock.listen(5)
    
    def connect(self, host, port):
        self.sock.connect((host, port))

    def conn_listen(self):
        BUFFER_SIZE = 4096
        self.conn, self.addr = self.sock.accept()

        while 1:
            data = self.conn.recv(BUFFER_SIZE)
            if not data : break
            if data == "close" : self.conn.close()
            print ("received data : ", data.decode())
