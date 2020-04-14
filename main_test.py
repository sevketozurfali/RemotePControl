import threading
import libMain

client = libMain.libMain()

thread1 = threading.Thread(client.find_sound_devices())
thread2 = threading.Thread(client.start_server())

thread1.start()
thread2.start()

