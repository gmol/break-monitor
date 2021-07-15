# breakalert project

## Raspberry Pi Zero Setup

### Setting up wireless networking

Source: <https://www.raspberrypi.org/documentation/configuration/wireless/headless.md>  
Put this file onto the boot partition of the SD card `wpa_supplicant.conf`.   
:warning: **5G wireless does not work!**

```properties
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IE

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```

#### Setting up more than one wireless network

Source: <https://raspberrypi.stackexchange.com/questions/11631/how-to-setup-multiple-wifi-networks>

Edit `/etc/wpa_supplicant/wpa_supplicant.conf` and add id_str="home" under the schools wpa info and id_str="work".

```properties
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IE

network={
    ssid="HOME NETWORK NAME"
    psk="HOME PASSWORD"
    id_str="home"
}

network={
    ssid="WORK NETWORK NAME"
    psk="WORK PASSWORD"
    id_str="work"
}
```

### Enable SSH on a headless Raspberry Pi (add file to SD card on another machine)

Source: <https://www.raspberrypi.org/documentation/remote-access/ssh/README.md>
For headless setup, SSH can be enabled by placing a file named `ssh`, without any extension, onto the boot partition of the SD card from another computer. The content of the file does not matter; it could contain text, or nothing at all.

### Password-less SSH access

`ssh-copy-id -i ~/.ssh/id_rsa.pub pi@192.168.1.10`

### Configure I2C

Type `sudo raspi-config`  

Choose interface  
![raspi-config](./docs/img/rasp-config.png)  
Enable i2c  
![i2c](./docs/img/i2c.png)  

### TMUX

- [tmux cheatsheet](./docs/img/tmux.png)
- [tmux cheatsheet b/w](./docs/img/tmux-printer.png)

## Software

### How to install dependencies

Look at the [Makefile](./Makefile) file.

### Run app

```bat
REM Set PYTHONPATH
set PYTHONPATH=.
REM Run app using python from ven
.\venv\Scripts\python.exe states/main.py
```

### Run unit tests

Run command from the root directory:

```shell
  pytest
```

### Get coverage report

Activate venv and run the following commands:

```shell
    (venv) C:\git\python\breakalert>coverage run -m pytest
    (venv) C:\git\python\breakalert>coverage html
```

## TODO

- [x] Update/restore get_distance method by adding while loop and not returning None(s)
- [ ] Remove color enum
- [ ] Fix IP address light brightness
- [ ] Add workflow to generate plantuml files
- [ ] Go back to idle when Workstate was very short. For example <5min
- [ ] Add movement detection for Distant Threshold Detection Strategy
  - when probability 1.0, normalize distance values and check how the distance has been changed
- [ ] Statistics (how much time in front of computer in total so far during the day)
- [ ] Last 3 LEDs to count break time
  
 
![todo](./docs/uml/todo-mindmap.svg)

## Components

![compenents](./docs/uml/compenents.svg)

## Configuration

![configuration](./docs/uml/configuration.svg)

## Cancelable repetitive task

| Note                       | Link                                                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Cancelable repetitive task | <https://stackoverflow.com/questions/22498038/improve-current-implementation-of-a-setinterval/22498708#22498708> |
| metronome like ticks       | <https://stackoverflow.com/a/25251804/4279>                                                                      |
