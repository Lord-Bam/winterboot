import components
import time

meter = components.VoltageMeter(pin=34, voltage_devider=True)

while True:
    print(meter.read())
    time.sleep(1)
