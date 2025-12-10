# pyright: reportMissingImports=false

from machine import Pin
import time

IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
BUTTON_pin = Pin(5, Pin.IN)

def Tpwm(duration, Hz, percent):
    period = 1_000_000 // Hz                # period in microseconds
    on_time = int(period * percent)         # % ON
    off_time = period - on_time

    end_time = time.ticks_us() + duration * 1_000_000

    while time.ticks_diff(end_time, time.ticks_us()) > 0:
        # ON time
        IN2.value(1)
        time.sleep_us(on_time)

        # OFF time
        IN2.value(0)
        time.sleep_us(off_time)
x=1.0
for i in range(8):
    x=x-0.1
    Tpwm(2, 20_000, x)
    time.sleep(0.4)



'''
from machine import Pin
import time
IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
BOTTOn_pin = Pin(5, Pin.IN)

while True:
    if BOTTOn_pin.value() == 1:
        IN1.toggle()
        time.sleep(0.3)
        print("moving")
    print(BOTTOn_pin.value())
'''