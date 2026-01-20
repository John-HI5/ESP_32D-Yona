# pyright: reportMissingImports=false

import network
import esp

esp.osdebug(None)

AP_SSID = "ESP32_X1C_LAN"
AP_PASSWORD = "BARAKSHELEFALLCAPS"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(
    essid=AP_SSID,
    password=AP_PASSWORD,
    authmode=network.AUTH_WPA2_PSK
)

print("AP ready:", ap.ifconfig())

while True:
    pass


'''
# ==============================
# USER CONFIGURATION (EDIT HERE)
# ==============================
import network


AP_SSID = "ESP32_D-X1C"
AP_PASSWORD = "BUG"   # min 8 chars

# Known WiFi networks the ESP32 may connect to
# Add / remove networks freely
KNOWN_NETWORKS = {
    "Jonathan123": "12345678",
    "HomeWiFi": "home_wifi_password",
    "OfficeWiFi": "office_wifi_password",
}

SCAN_INTERVAL_SEC = 10



import network
import time
import esp

esp.osdebug(None)

# --- Access Point (Printer side) ---
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(
    essid=AP_SSID,
    password=AP_PASSWORD,
    authmode=network.AUTH_WPA2_PSK
)

print("[AP] Started:", ap.ifconfig())

# --- Station (Internet side) ---
sta = network.WLAN(network.STA_IF)
sta.active(True)

def connect_to_known_wifi():
    if sta.isconnected():
        return

    print("[STA] Scanning...")
    try:
        networks = sta.scan()
    except Exception as e:
        print("[STA] Scan failed:", e)
        return

    for net in networks:
        ssid = net[0].decode()
        if ssid in KNOWN_NETWORKS:
            print("[STA] Connecting to:", ssid)
            sta.connect(ssid, KNOWN_NETWORKS[ssid])

            for _ in range(10):
                if sta.isconnected():
                    print("[STA] Connected:", sta.ifconfig())
                    return
                time.sleep(1)

    print("[STA] No known networks found")

# --- Main loop ---
while True:
    connect_to_known_wifi()
    time.sleep(SCAN_INTERVAL_SEC)

'''

