import sys
import time

print("ESP32 ready. Waiting for input...")

while True:
    line = sys.stdin.readline()  # receives data from PC
    if not line:
        continue

    key = line.strip()
    print("Received key:", key)

    # Example: play tones, trigger output, etc.
    # For now just print it.
