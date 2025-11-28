# pyright: reportMissingImports=false
from machine import Pin, PWM
import time


motors = {
    1: (Pin(18, Pin.OUT), Pin(19, Pin.OUT)),
    2: (Pin(21, Pin.OUT), Pin(22, Pin.OUT)),
    3: (Pin(23, Pin.OUT), Pin(5, Pin.OUT))
}

FREQ = 2000

def change_motor(power, direction, motor):
    """
    power: 0–1 (duty)
    direction: 0=left, 1=right, 2=stop
    motor: motor number (1,2,3)
    """

    IN1, IN2 = motors[motor]

    duty = int(power * 1023)  # 10bit PWM

    if direction == 0:       # LEFT
        IN1.value(1)
        IN2.value(0)

    elif direction == 1:     # RIGHT
        IN1.value(0)
        IN2.value(1)

    else:                    # STOP
        IN1.value(0)
        IN2.value(0)
        return


    pwm = PWM(IN1, freq=FREQ, duty=duty)
