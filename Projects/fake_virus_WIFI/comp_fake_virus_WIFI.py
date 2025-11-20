import network
import time

ap = network.WLAN(network.AP_IF)
ap.active(True)

# Proper config format for your firmware
ap.config(essid="soon_free_for_students", authmode=0)


print("Hotspot Running!")
print("SSID:", ap.config('essid'))
print("IP:", ap.ifconfig()[0])

connected_macs = set()

while True:
    stations = ap.status('stations')
    current_macs = set([s[0] for s in stations])

    new = current_macs - connected_macs
    for mac in new:
        print("New device connected:", mac)

    gone = connected_macs - current_macs
    for mac in gone:
        print("Device disconnected:", mac)

    connected_macs = current_macs
    time.sleep(2)
