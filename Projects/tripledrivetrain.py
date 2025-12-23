# pyright: reportMissingImports=false
from machine import Pin, ADC
import time
import math
#from PWM_func.py import Tpwm


# Joystick connections
vrx = ADC(Pin(39))   # VN → X-axis
vry = ADC(Pin(36))   # VP → Y-axis
sw  = Pin(27, Pin.IN, Pin.PULL_UP)  # Button

# Set full ADC range
vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)


def stickCalib():
    print("dont tag, calibration!")
    centerx = vrx.read()
    centery = vry.read()
    print("DONE!")
    return centerx, centery


# x, y = input_stick()
'''
# Main loop
while True:
    time.sleep(1)
    x, y = input_stick()
    print(x, y)
'''

def input_stick(centerx, centery):
    x = vrx.read() - centerx # 0 .. 4095
    y = vry.read() - centery  # 0 .. 4095
    return x, y



def calc_alpha (X, Y): #calc M with x and y and then the alpha 
    m = Y / X
    print("m is ", m)
    alpha = math.degrees(math.atan(m)) #tan in D for m to find alpha
    print("alpha is ", alpha)
    return alpha
    #needs to calc V also

def motors_power (alpha):
    single_motor = 0
    if (alpha < 30) and (alpha > -30):
        single_motor=  1
    elif (alpha < -30):
        single_motor = 2
    single_motor = 3
    

def q (alpha, V): #returns q

     # calc 
    #q = V * math.sin(math.radians(90 - alpha)) -- wrong
    #q = V * math.sin(math.radians(alpha)) -- get y component
    q = V * math.cos(math.radians(alpha))

    

    print(q)
    return q



def playall ():
    cenx , ceny = stickCalib()
    print("finished stickCalib")
    Xx, Yy= input_stick (cenx, ceny)
    print("finished input_stick")
    alpha_value, v_value = calc_alpha(Xx, Yy, Vv)
    print("finished calc_alpha")
    cc = q(alpha_value, v_value)
    print("finished q")
    print (cc)
    return cc


while True:
    time.sleep(1)
    print (playall())
