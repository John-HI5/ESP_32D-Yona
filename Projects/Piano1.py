# pyright: reportMissingImports=false
from machine import Pin
import time

led = Pin(2, Pin.IN)
print(led.value())
