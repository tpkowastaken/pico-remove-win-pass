# Pico script to remove windows password
script using curcuitpy to remove windows password on non-encrypted (without bitlocker) drives.
# Use this only on devices that you have permission to use it on. This Repo is for educational purposes only!
# How to use
1. Install [circuitpy](https://circuitpython.org/board/raspberry_pi_pico/) on the rpi pico. You can do this simply by holding the bootsel button when plugging the rpi and then putting the file in the link inside the rpi pico directory (on the disk that was mounted). Note: if You installed Anything on this rpi pico previously you have to wipe it first by putting [flash_nuke.uf2](https://github.com/dwelch67/raspberrypi-pico/raw/main/flash_nuke.uf2) into the same directory.
2. Get a bootable windows usb
3. copy the files from here to rpi pico (adafruit_hid to lib)
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
2. Once windows boots we get 
