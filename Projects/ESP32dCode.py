# pyright: reportMissingImports=false
from machine import Pin, ADC
import time

# Joystick connections
vrx = ADC(Pin(39))   # VN → X-axis
vry = ADC(Pin(36))   # VP → Y-axis
sw  = Pin(27, Pin.IN, Pin.PULL_UP)  # Button

# Set full ADC range
vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

def input_stick():
    x = vrx.read()   # 0 .. 4095
    y = vry.read()   # 0 .. 4095
    return x, y

# Main loop
while True:
    time.sleep(1)
    x, y = input_stick()
    print(x, y)
