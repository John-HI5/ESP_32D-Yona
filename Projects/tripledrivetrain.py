# pyright: reportMissingImports=false
from machine import Pin, PWM
import time
from machine import Pin, PWM
import time

# One motor example
IN1 = PWM(Pin(18))
IN2 = Pin(19, Pin.OUT)

IN1.freq(2000)  # PWM frequency

def change_motor(power, direction):
    """
    power: 0.0–1.0
    direction: 0=left, 1=right, 2=stop
    """

    duty = int(power * 1023)

    if direction == 0:      # left
        IN2.value(0)
        IN1.duty(duty)

    elif direction == 1:    # right
        
        IN2.value(1)
        IN1.duty(duty)

    else:                  # stop
        IN1.duty(0)
        IN2.value(0)

for p in [0.01, 0.1, 0.2, 0.3, 0.5, 1]:
    change_motor(p, 1, 1)
    print("Power:", p)
    time.sleep(1)
