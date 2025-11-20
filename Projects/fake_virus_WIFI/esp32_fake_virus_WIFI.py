# pyright: reportMissingImports=false

import network

# Create Access Point
ap = network.WLAN(network.AP_IF)
ap.active(True)

# Set your hotspot name (SSID) and password
ap.config(essid="Tlv-Sch.free_for_students")

print("Fake hotspot running...")
print("SSID:", ap.config('essid'))
print("Password:", ap.config('password'))

# Check IP
print("IP address:", ap.ifconfig()[0])
