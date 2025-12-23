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
# Motor 1
IN1 = Pin(18, Pin.OUT)  # direction
PWM1 = PWM(Pin(19), freq=20000, duty=0)  # PWM pin

# Motor 2
IN2 = Pin(23, Pin.OUT)  # direction
PWM2 = PWM(Pin(22), freq=20000, duty=0)  # PWM pin

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

while True:
    x, y = read_stick(cx, cy)
    print  (x,y)
    # Motor 1 → Y-axis
    drive_motor(y, IN1, PWM1)

    # Motor 2 → X-axis
    drive_motor(x, IN2, PWM2)

    print(f"X:{x} Y:{y}")
    time.sleep(0.01)
