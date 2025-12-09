# pyright: reportMissingImports=false

from machine import Pin
import time
IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
BOTTOn_pin = Pin(5, Pin.IN)


def Tpwm(duration, Hz, percent):
    end_time = time.time() + duration   
    duration2 = 1/Hz

    while time.time() < end_time: #big timer - duration
        end_time2 = time.time() + duration2

        while time.time() < end_time2:
            IN2.value(1)
            time.sleep(Hz * percent)
            IN2.value(0)





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
