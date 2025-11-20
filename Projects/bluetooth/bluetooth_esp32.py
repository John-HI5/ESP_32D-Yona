import bluetooth

ble = bluetooth.BLE()
ble.active(True)

# Your desired Bluetooth name
bt_name = "MY_ESP32"

# Advertising packet: "\x02\x01\x06" is flags, "\x09\x09" is name length + type
adv_data = b"\x02\x01\x06" + bytes([len(bt_name)+1, 0x09]) + bt_name.encode()

ble.gap_advertise(100_000, adv_data)

print("Bluetooth advertising as", bt_name)
