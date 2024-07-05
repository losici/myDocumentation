# Udev Rule
To ensure that the Arduino connected to the raspberry pi get the same device name, a custom udev rule was created. 
The file `99-usb-serial.rules` in `/etc/udev/rules.d/99-usb-serial.rules` contains a rule which creates a symbolic link `/dev/arduino that` always pointing to the Arduino connected to the raspberry Pi, regardless of the dynamically assigned ttyACM number (which can change with power cycle, disconnecting the device etc).

1. Identify unique attributes of the used Arduino in the setup. Use the udevadm command
   ```
   udevadm info -a -p $(udevadm info -q path -n /dev/ttyACM0)
   ```
   The number in **/dev/ttyACM0** is subjected to change.

1. Create a new udev rule file
   ```
   sudo nano /etc/udev/rules.d/99-usb-serial.rules
   ```
1. Add a rule using the identified attributes
   ```
   SUBSYSTEM=="tty", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="0042", ATTRS{serial}=="75131313932351405091", SYMLINK+="arduino"
   ```
1. After creating or modifying the udev rule, reload the rules:
   ```
   sudo udevadm control --reload-rules
   ```
#### steps to verify the udev rule
1. Check the udev Rule File:
   ```
   cat /etc/udev/rules.d/99-usb-serial.rules
   ```
1. Reload the udev rules to apply the changes:
   ```
   sudo udevadm control --reload-rules
   ```
1. Trigger udev to process the rules:
   ```
   sudo udevadm trigger
   ```
1. Be sure that the arduino is connected and check the symbolic link
   ```
   ls -l /dev/arduino
   ```
   The output should look like something like this if the link is correclty created:
   ```
   lrwxrwxrwx 1 root root 7 May 27 12:34 /dev/arduino -> ttyACM0
   ```
1. Finally, if the system is restard reload the rules
    ```
    sudo udevadm control --reload-rules
    sudo udevadm trigger
    ```