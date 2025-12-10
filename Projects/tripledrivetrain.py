# pyright: reportMissingImports=false
from machine import Pin, PWM
import time
import math
from PWM_func import Tpwm

def input_stick (pin1, pin2): #needs to normalize the stick values and return x,y,and strength(lenth is Pythagoras)
    print("make me")
    x = 300
    y = 400
    v = (y**2 + x**2)** 0.5
    return x,y,v

def calc_alpha (X, Y, L): #calc M with x and y and then the alpha 
    m = Y / X
    angle_degrees = math.degrees(math.atan(m)) #tan in D for m to find alpha

def q (V, alpha, length):
    print("make me")
    
