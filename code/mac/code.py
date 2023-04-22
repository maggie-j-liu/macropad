# see https://uwu.cx/macropad for instructions

import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import neopixel

num_pixels = 3

# https://github.com/maxking/micropython/blob/master/rainbow.py#L14
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


pixels = neopixel.NeoPixel(board.GP17, num_pixels, auto_write=False)
pixels.brightness = 0.5

pins = (
    board.GP0,
    board.GP1,
    board.GP2
)

keycodes = (
    Keycode.COMMAND,
    Keycode.C,
    Keycode.V
)

switches = []

for pin in pins:
    switch = digitalio.DigitalInOut(pin)
    switch.pull = digitalio.Pull.UP
    switches.append(switch)

keyboard = Keyboard(usb_hid.devices)

key_pressed = [False] * len(pins)

j = 0

while True:
    for i in range(num_pixels):
        rc_index = (i * 256 // num_pixels) + j
        pixels[i] = wheel(rc_index & 255)
    pixels.show()
    j += 1
    
    for i in range(len(pins)):
        if not key_pressed[i]:
            # if key is now pressed
            if not switches[i].value:
                keyboard.press(keycodes[i])
                key_pressed[i] = True
        else:
            # if key is now released
            if switches[i].value:
                keyboard.release(keycodes[i])
                key_pressed[i] = False
    time.sleep(0.01)
