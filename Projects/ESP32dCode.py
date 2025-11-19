# pyright: reportMissingImports=false

import sys
import select
from machine import Pin
import time

print("ESP32 ready.")
led = Pin(2, Pin.OUT)
while True:
    # Check if there's input waiting
    if select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline().strip()
        led.toggle()

        # TODO: handle keys here
        # if line == "a": play_note(A4)  

    # ESP32 can do other things here:
    # update screen, play sounds, blink LED, run game loop, etc.
    # This loop NEVER blocks!
    time.sleep(0.01)
