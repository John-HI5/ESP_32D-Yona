# pyright: reportMissingImports=false
from machine import Pin
import time                            # Sleep/timestamps
import math                            # Misc math helpers (kept for completeness)
import keyboard


led = Pin(2, Pin.OUT)
led.value(1)
print(led.value())

