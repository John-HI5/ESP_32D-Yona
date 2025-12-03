# pyright: reportMissingImports=false
# MicroPython SERVER - WiFi details from serial terminal

import network
import socket
import time

# ---- 1. Ask the user over USB serial ----
ssid = input("Enter WiFi SSID: ")
password = input("Enter WiFi password: ")

# ---- 2. Connect to Wi-Fi ----
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Connecting to WiFi...")

while not wifi.isconnected():
    time.sleep(0.5)
    print("still not connected...")

print("Connected:", wifi.ifconfig())

# ---- 3. Create TCP server (same as your original) ----
server = socket.socket()
server.bind(("0.0.0.0", 1234))
server.listen(1)
print("Server listening...")

while True:
    print("WiFi strength (RSSI):", wifi.status('rssi'), "dBm")

    time.sleep(1)
    


while True:
    
    conn, addr = server.accept()
    print("Client connected:", addr)

    data = conn.recv(1024)
    print("Received:", data.decode())

    conn.send("OK".encode())
    conn.close()
    time.sleep(1)
    wifi.status('rssi')

while True:
    wifi.status('rssi')

