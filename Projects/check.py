# pyright: reportMissingImports=false
from machine import Pin, PWM
import time

#pin 27 is motor C
#pin 14 is motor C

# Motor pins
A_motor1 = Pin(26, Pin.OUT)      # direction
A_PWM_motor2 = PWM(Pin(25), freq=20000, duty=0)  # PWM

# Forward 50%
A_motor1.value(1)        # set direction
A_PWM_motor2.duty(0)   # 50% speed
time.sleep(5)             # run for 5 seconds

# Stop
A_PWM_motor2.duty(0)
A_motor1.value(0)  
