# Pico script to remove windows password
script using curcuitpy to remove windows password on non-encrypted (without bitlocker) drives.
## Use this only on devices that you have permission to use it on. This Repo is for educational purposes only!
This was tested on windows 10
# LED
The led first lights up to give you some time to react. Then it flashes x number of times with x being the mode number. 
1. mode - This is in the booted usb
2. mode - This is once windows boots
3. mode - This is once windows is logged in
# How to use
1. Install [circuitpy](https://circuitpython.org/board/raspberry_pi_pico/) on the rpi pico. You can do this simply by holding the bootsel button when plugging the rpi and then putting the file in the link inside the rpi pico directory (on the disk that was mounted). Note: if You installed Anything on this rpi pico previously you have to wipe it first by putting [flash_nuke.uf2](https://github.com/dwelch67/raspberrypi-pico/raw/main/flash_nuke.uf2) into the same directory.
2. Get a bootable windows usb - You can create one [here](https://support.microsoft.com/en-us/windows/create-installation-media-for-windows-99a58364-8c02-206f-aa6f-40c3b507420d)
3. copy the files from here to rpi pico ([adafruit_hid](https://github.com/adafruit/Adafruit_CircuitPython_HID/tree/main/adafruit_hid) to lib)
4. make sure to keep the var.txt as 0 before plugging it in to the target pc (every time you plug it in it increases)
5. boot to the to the windows usb
6. plug the rpi
7. after it's done unplug it and plug it once windows loads
9. rewrite [user] with your username and 123 with your new password
10. login with your new credentials
11. plug the rpi again so that it can revert the system to it's previous state (the password will stay as the new one set)
12. enjoy unlocked windows!
# How does this work
1. When you boot to the windows usb the rpi replicates an hid device (like a keyboard) and does inputs to the computer. It will try to replace sethc.exe with cmd.exe in system32. To preserve the system it also creates sethc_backup.exe in system32 to backup sethc. This allows us to execute command prompt in the login screen. This cannot work if the drive is encrypted tho as we do not have access to system32 when it's encrypted.
2. Once windows boots we get the rpi to press shift multiple times which starts sethc.exe (sticky keys). This opens the command prompt with administrator privileges. Now the rpi types ```net user [username] 123```. This command changes the login information for the user. This works only with non-microsoft accounts tho. If you want to retrieve data from a microsoft account you can instead type ```net user administrator /active:yes ```. This will create a new user called administrator with absolute administrator privileges. It is recommended to delete this account once you're finished. You can do so using this command: ```net user administrator /active:no```.
3. Once you're logged in plugging the rpi again replaces sethc.exe with sethc_backup.exe so that we can have sticky keys back again. It's possible that windows defender will popup with privilige escalation warning. This was neccessary to do the password removal. Once the rpi finishes the system is back to normal but with the new password.
