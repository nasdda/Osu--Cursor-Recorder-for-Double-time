from pynput import keyboard
from MouseRecord import MouseRecord
from Launcher import Launcher
import threading
import sys
#### r to record and z to start
started = False

def on_press(key):
    MR = MouseRecord()
    launch = Launcher()
    t = threading.Thread(target=launch.run)
    global started
    try:
        if str(key.char) == 'q' and not started:
            MR.run_thread()
            print('detected')
            started = True
        if str(key.char) == 'z' and not started:
            t.start()
            started = True
    except:
        pass





listener = keyboard.Listener(
    on_press=on_press)
listener.start()
listener.join()

