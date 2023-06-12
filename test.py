import time

wait_time = time.ticks_ms()

while True:
    if wait_time + 1000 < time.ticks_ms():
        wait_time = time.ticks_ms()
        print("test")