<!-- markdownlint-disable MD033 -->

# Breakalert project (Simple)

## Raspberry Pi Zero Setup

```shell
sudo apt install python3-dev
python3 -m venv foobar
# or
# see https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi#setup-virtual-environment-3157129
python -m venv foobar --system-site-packages

```

❗NOTE❗  
 Properly installed venv on RPi should have `pyvenv`.cfg file inside the main directory. See [Adafruit tutorial](https://tinyurl.com/2524dums).

### Distance measure

File: requirements.txt. Try without this installation. The [Adafruit tutorial](https://tinyurl.com/2524dums) about venv said `gpiozero` should be installed with the system (but maybe not the headless one)

```plain
rpi.gpio
pigpio==1.78
RPi.GPIO==0.7.1
gpiozero==2.0.1
```

```shell
# this could be useful as well, see https://gpiozero.readthedocs.io/en/stable/api_input.html#distancesensor-hc-sr04
# Do not install until you try install it view requirements.txt
sudo apt-get install pigpio python-pigpio python3-pigpio
```

```shell
# start the app
GPIOZERO_PIN_FACTORY=pigpio ./venv/bin/python main.py
```

If there are any issues see:

```shell
GPIOZERO_PIN_FACTORY=pigpio ./venv/bin/python main.py
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Can't connect to pigpio at localhost(8888)

Did you start the pigpio daemon? E.g. sudo pigpiod

Did you specify the correct Pi host/port in the environment
variables PIGPIO_ADDR/PIGPIO_PORT?
E.g. export PIGPIO_ADDR=soft, export PIGPIO_PORT=8888

Did you specify the correct Pi host/port in the
pigpio.pi() function? E.g. pigpio.pi('soft', 8888)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```

### Program

```python
from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(max_distance=2, trigger=23, echo=24)

while True:
    print('Distance to nearest object is', sensor.distance*100, 'cm')
    sleep(1)
```

### Light

Try install `blinka` via automated install in venv, i.e. after activating the environment: <https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi#automated-install-3081632>.  
Or install manually: <https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi#manual-install-3157124>

```plain
rpi.gpio
pigpio==1.78
RPi.GPIO==0.7.1
gpiozero==2.0.1
rpi-ws281x==5.0.0
adafruit-blinka==8.35.0
adafruit-circuitpython-neopixel==6.3.11
```

```python
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D12

# The number of NeoPixels
num_pixels = 1

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 0, 255))
    pixels.show()
    time.sleep(1)

    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step

    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(3)
```
