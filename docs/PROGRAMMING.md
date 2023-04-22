# Programming

The macropad is essentially a Raspberry Pi Pico, so you can program it in any way a Raspberry Pi Pico can be programmed. We'll use [CircuitPython](https://circuitpython.org/) and the [`adafruit_hid`](https://docs.circuitpython.org/projects/hid/en/latest/index.html) library.

## Installing CircuitPython

If you plug in the macropad and a `CIRCUITPY` drive appears, then CircuitPython is already installed; skip this step. If not, follow [this guide](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython)!

## Add the Code

If you have a Mac, download the [`code/mac`](../code/mac) folder. If you have a Windows computer, download the [`code/non-mac`](../code/non-mac) folder.

Copy the `lib` and `code.py` into the `CIRCUITPY` drive. The default code sets the 3 keys to <kbd>cmd</kbd> / <kbd>ctrl</kbd>, <kbd>c</kbd>, and <kbd>v</kbd>, but change them to whatever you want! Refer to the [`adafruit_hid` documentation](https://docs.circuitpython.org/projects/hid/en/latest/index.html) to control the keys and the [`neopixel` documentation](https://docs.circuitpython.org/projects/neopixel/en/latest/index.html) to control the LEDs.
