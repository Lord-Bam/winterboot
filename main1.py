import machine
import time
import winterboot
from hcsr04 import HCSR04
from time import sleep


wb = winterboot.WinterBoot()


direction = wb.joystick.read()



while True:

    direction = wb.joystick.read()
    x = direction[0] * -1 // 10 + 24
    y = direction[1] * -1 // 10 + 24
    
    left = y + x * -1
    right = y + x
    
    
    wb.motor_shield.control_motors(left, right)
    time.sleep(0.1)
    
    
#     actuel_left_pwm = (left_wheels + 24) *20
#     print("actuel_left_pwm", actuel_left_pwm)
#     
#     actuel_right_pwm = (right_wheels + 24) *20
#     print("actuel_right_pwm", actuel_right_pwm)
#     
#     wb.motor_shield.left_wheels_speed(actuel_left_pwm)
#     wb.motor_shield.right_wheels_speed(actuel_right_pwm)
    
    time.sleep(0.4)

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



