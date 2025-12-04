# pyright: reportMissingImports=false
import time

start = time.ticks_ms()

for i in range(100000):
    x = i * 2

end = time.ticks_ms()
elapsed = time.ticks_diff(end, start)

print("Loop time (ms):", elapsed)
print("Average per iteration (ms):", elapsed / 100000)
