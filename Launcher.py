import time
from pynput.mouse import Controller
mouse = Controller()

class Launcher:
    def __init__(self):
        pass

    def run(self):
        with open(r'C:\MouseDatas\movement', 'r') as file:
            coords = file.read().splitlines()
            for coord in coords:
                try:
                    coord = coord.split('\t')
                    x,y = mouse.position
                    mouse.move(int(coord[0])-x,int(coord[1])-y)
                    time.sleep(0.006)
                except:
                    pass

