import time
import board
import digitalio
import storage

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True
storage.remount("/", 0)
file = open("./var.txt", "r")
num = file.read()
file.close()
file = open("./var.txt", "w+")
file.write(str(int(num) + 1))
file.close()
storage.remount("/",1)
time.sleep(3)
led.value = False