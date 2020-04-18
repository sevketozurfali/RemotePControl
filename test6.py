from pynput.keyboard import Listener


def on_press(key):
    if str(key) == '<179>':
        print("play pause media key was pressed")
    if str(key) == '<176>':
        print("next key was pressed")
    if str(key) == '<177>':
        print("previous key was pressed")
    if str(key) == '<269025044>':
        print("play pause key pressed.")

def on_release(key):
    pass

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# listener_thread = Listener(on_press=on_press, on_release=None)
# # This is a daemon=True thread, use .join() to prevent code from exiting  
# listener_thread.start()

