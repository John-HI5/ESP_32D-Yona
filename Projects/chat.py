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
A_motor1 = Pin(32, Pin.OUT)      # direction
A_PWM_motor2 = PWM(Pin(33), freq=20000, duty=0)  # PWM

# Motor B
B_motor1 = Pin(27, Pin.OUT)      # direction
B_PWM_motor2 = PWM(Pin(14), freq=20000, duty=0)  # PWM

# Motor C
C_motor1 = Pin(26, Pin.OUT)      # direction
C_PWM_motor2 = PWM(Pin(25), freq=20000, duty=0)  # PWM

# =========================
# run motor functions
# =========================

def runmotor(motor, WithOrAgains, precent):
    motor_pin1 = motor + "_motor1"
    motor_pin2_pwm = motor + "_PWM_motor2"
    
    '''
    motor_pin1.value(1)        # set direction
    A_PWM_motor2.duty(0)   # 50% speed
    time.sleep(5)             # run for 5 seconds
    '''

    


    


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
def calc_speed(value):
    """Convert joystick value to 0–1023 PWM duty"""
    speed = max(0, abs(value) - DEADZONE) / (ADC_MAX - DEADZONE)
    return min(int(speed * 1023), 1023)

# =========================
# DRIVE MOTOR
# =========================
def drive_motor(value, direction_pin, pwm):
    if value > 0:
        direction_pin.value(1)
    elif value < 0:
        direction_pin.value(0)
    else:
        pwm.duty(0)
        return

    pwm.duty(calc_speed(value))

# =========================
# MAIN LOOP
# =========================
cx, cy = stickCalib()


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
A_motor1.value(1)

# Set PWM duty to 50% (ESP32 duty range 0–1023)
A_PWM_motor2.duty(512)

#A_PWM_motor2.duty(0)
