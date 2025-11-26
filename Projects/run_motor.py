# pyright: reportMissingImports=false

from machine import Pin
import time
IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
BOTTOn_pin = Pin(5, Pin.IN)

while True:
    if BOTTOn_pin.value() == 1:
        IN1.toggle()
        time.sleep(0.3)



'''


# Forward full power (assuming ENA is hard-wired to +5V)
IN1.value(1)
IN2.value(0)

print("Motor running forward at full power")
'''
