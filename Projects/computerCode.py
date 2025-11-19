# pyright: reportMissingImports=false

import serial
import keyboard
import time

PORT = "COM6"   # change if needed
BAUD = 115200

ser = serial.Serial(PORT, BAUD)
time.sleep(2)  # wait for ESP32 reset

print("Connected to ESP32. Press keys to send:")

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name  # e.g. 'a', '1', 'space'
        ser.write((key + "\n").encode())
        print("Sent:", key)