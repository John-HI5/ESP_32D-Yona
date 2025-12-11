# pyright: reportMissingImports=false
#from machine import Pin, PWM
import time
import math
#from PWM_func.py import Tpwm
v = 100
def input_stick (pin1, pin2): #needs to normalize the stick values and return x,y
    print("make me")


    x = 110
    y = 30
    # v = 100  #v = ((y**2) + (x**2))** 0.5      wtf why did i do that

    print("v is ", v)
    return (x,y)



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


playall()