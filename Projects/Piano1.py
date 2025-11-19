# pyright: reportMissingImports=false

from machine import Pin
import time                            # Sleep/timestamps
import math                            # Misc math helpers (kept for completeness)
from machine import ADC, Pin

adc = ADC(Pin(25))   # choose an analog-capable pin
value = adc.read()   # returns 0–4095


while True:
    print(value)
    time.sleep(0.5)


