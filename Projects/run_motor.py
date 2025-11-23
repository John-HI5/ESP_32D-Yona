# pyright: reportMissingImports=false

from machine import Pin

IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)

# Forward full power (assuming ENA is hard-wired to +5V)
IN1.value(1)
IN2.value(0)

print("Motor running forward at full power")
