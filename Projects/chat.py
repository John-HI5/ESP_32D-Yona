# pyright: reportMissingImports=false
from machine import Pin, ADC, PWM
import time

# =========================
# JOYSTICK
# =========================
vrx = ADC(Pin(35))  # X-axis
vry = ADC(Pin(34))  # Y-axis

vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

# =========================
# MOTORS
# =========================

# Motor A
A_motor1 = Pin(32, Pin.OUT)      # direction WHEN ON RIGHT
A_PWM_motor2 = PWM(Pin(33), freq=20000, duty=0)  # PWM

# Motor B
B_motor1 = Pin(27, Pin.OUT)      # direction WHEN ON RIGHT
B_PWM_motor2 = PWM(Pin(14), freq=20000, duty=0)  # PWM

# Motor C
C_motor1 = Pin(26, Pin.OUT)      # direction WHEN ON RIGHT
C_PWM_motor2 = PWM(Pin(25), freq=20000, duty=0)  # PWM

# =========================
# dic for motors
# =========================
motors = {
    "A": {"dir": A_motor1, "pwm": A_PWM_motor2},
    "B": {"dir": B_motor1, "pwm": B_PWM_motor2},
    "C": {"dir": C_motor1, "pwm": C_PWM_motor2},
}


# =========================
# CONSTANTS
# =========================
ADC_MAX = 4095
DEADZONE = 80

# =========================
# CALIBRATION
# =========================
def stickCalib():
    print("Calibrating...")
    time.sleep(1)
    cx = sum(vrx.read() for _ in range(20)) // 20
    cy = sum(vry.read() for _ in range(20)) // 20
    print("Center:", cx, cy)
    return cx, cy

# =========================
# READ STICK
# =========================
def read_stick(cx, cy):
    x = vrx.read() - cx
    y = vry.read() - cy

    if abs(x) < DEADZONE:
        x = 0
    if abs(y) < DEADZONE:
        y = 0

    return x, y

# =========================
# CALCULATE SPEED
# =========================
def calc_cords(value):
    """Convert joystick value to 0–1023 PWM duty"""
    speed = max(0, abs(value) - DEADZONE) / (ADC_MAX - DEADZONE)
    return min(int(speed * 1023), 1023)


# =========================
# run motor functions
# =========================
def run_motor(motor, WithOrAgainst, P): #(A, B, C), (0, 1), (0.0 - 100).
    m = motors[motor]
    # direction
    m["dir"].value(WithOrAgainst)
    # PWM (0–1023 on ESP32)
    duty = int((P / 100) * 1023)
    m["pwm"].duty(duty)

    '''
    motor_pin1.value(1)        # set direction
    A_PWM_motor2.duty(0)   # 50% speed
    time.sleep(5)             # run for 5 seconds
    '''

# =========================
# run motor functions
# =========================
def power_des (x, y, v):
    m = y / x
    Y = m*x
    X = Y*m

    import math
    angle_rad = math.atan2(y, x)     
    angle_deg = math.degrees(angle_rad) 

    print(angle_deg)


    q = V * math.cos(math.radians(alpha))
    if (x > 0 and y > 0):
        if (y > x):




#q = V * math.cos(math.radians(alpha))
# =========================
# MAIN LOOP
# =========================

cx, cy = stickCalib()
x , y = read_stick(cx, cy)


'''
while True:
    x, y = read_stick(cx, cy)
    print  (x,y)
    # Motor 1 → Y-axis
    drive_motor(y, IN1, PWM1)

    # Motor 2 → X-axis
    drive_motor(x, IN2, PWM2)

    print(f"X:{x} Y:{y}")
    time.sleep(0.01)
'''
# Set direction forward
#A_motor1.value(1)

# Set PWM duty to 50% (ESP32 duty range 0–1023)
#A_PWM_motor2.duty(512)

#A_PWM_motor2.duty(0)
