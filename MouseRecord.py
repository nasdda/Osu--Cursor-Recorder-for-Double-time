import pyautogui
import time
import threading
from pynput.mouse import Controller
mouse = Controller()
class MouseRecord:
    def __init__(self):
       pass
    
    def run(self):
        with open(r'C:\MouseDatas\movement', 'w') as file:
            while(True):
                x,y = mouse.position
                s = f'{x}\t{y}\n'
                file.write(s)
                time.sleep(0.009)
                file.flush()
            file.close()
            print('end')
            
    
    def run_thread(self):
        t = threading.Thread(target=self.run).start()
        