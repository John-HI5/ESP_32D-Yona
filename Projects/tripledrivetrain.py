# pyright: reportMissingImports=false
#from machine import Pin, PWM
import time
import math
#from PWM_func.py import Tpwm

def input_stick (pin1, pin2): #needs to normalize the stick values and return x,y,and strength(lenth is Pythagoras)
    print("make me")
    x = 300
    y = 400
    v = (y**2 + x**2)** 0.5
    return (x,y,v)


def calc_alpha (X, Y, V): #calc M with x and y and then the alpha 
    m = Y / X
    alpha = math.degrees(math.atan(m)) #tan in D for m to find alpha
    return alpha , V

def q (alpha, V): #returns q

     # calc 
    q = V * math.sin(math.radians(90 - alpha))
    print(q)
    return q

def playall ():
    aa = input_stick (1, 2)
    print("finished aa")
    bb = calc_alpha(aa)
    print("finished bb")
    cc = q(bb)
    print("finished cc")
    print (cc)
    return cc


playall()