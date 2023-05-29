import machine
import time
import winterboot


from hcsr04 import HCSR04
from time import sleep


wb = winterboot.WinterBoot()

wb.led1.on()
time.sleep(1)
wb.led1.off()

wb.motor_shield.forward()
time.sleep(1)
wb.motor_shield.back()

# ESP32
sensor = HCSR04(trigger_pin=25, echo_pin=26, echo_timeout_us=10000)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(1)


# 32 LED strip connected to X8.
pin = machine.Pin(12, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 12)

while True:
    np[0] = (255,0,0)
    np.write()
    for x in range(1,8):
        time.sleep(1)
        np[x - 1] = (0,0,0)
        np[x] = (255,0,0)
        np.write()



# Update the strip.







# wb.led1.on()
# time.sleep(1)
# wb.led1.off()
# 
# wb.motor_shield.forward()
# time.sleep(1)
# wb.motor_shield.back()
# time.sleep(1)
# wb.motor_shield.stop()