# pyright: reportMissingImports=false
from machine import Pin, ADC
import time
import math
#from PWM_func.py import Tpwm




# החיבורים שלך
vrx = ADC(Pin(14))   # X
vry = ADC(Pin(13))   # Y
sw  = Pin(27, Pin.IN, Pin.PULL_UP)

vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

def findnum():
    numx = vrx.read()   # 0 .. 4095
    numy = vry.read()   # 0 .. 4095
    return numx, numy

def input_stick(numx, numy):
    x = vrx.read()   # 0 .. 4095
    y = vry.read()   # 0 .. 4095

    print (x)
    print (y)
    x = x-(4095/2) -numx
    y = y-(4095/2) - numy
    return x, y






def calc_alpha (X, Y, V): #calc M with x and y and then the alpha 
    m = Y / X
    print("m is ", m)
    alpha = math.degrees(math.atan(m)) #tan in D for m to find alpha
    print("alpha is ", alpha)
    return alpha , V

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
    Xx, Yy, Vv = input_stick (1, 2)
    print("finished aa")
    alpha_value, v_value = calc_alpha(Xx, Yy, Vv)
    print("finished bb")
    cc = q(alpha_value, v_value)
    print("finished cc")
    print (cc)
    return cc

numx = findnum()
numy = findnum()
while True:
    time.sleep(1)
    print (input_stick(numx, numy))