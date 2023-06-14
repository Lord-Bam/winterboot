import winterboot
import __main__
import car


import machine
import hcsr04
import neopixel
import components

import time


def wb_handler(message):
    print(message)
    if "XY: " in message:
        message = message.split(" ")
        car.x = float(message[1])
        car.y = float(message[2])
        
    if "Button1" in message:
        message = message.split(" ")
        car.dim_lights = bool(int(message[1]))
        
    if "Button2" in message:
        message = message.split(" ")
        car.alarm_lights = bool(int(message[1]))
        

wb = winterboot.WinterBoot()
car = car.Car(wb.motor_shield, wb.front_lights, wb.rear_lights, wb.distance_sensor, wb.df)

car.start()


























# while True:
#     print(f"{wb.front_lights.dim_lights=}")
#     wb.front_lights.dim_lights = 1
#     time.sleep(1)
#     wb.front_lights.dim_lights = 0
#     time.sleep(1)




    
    
    
# #forward
# car.control_motors(0.00, 0.00)
# time.sleep(0.5)
# car.control_motors(0.00, 9.00)
# time.sleep(0.5)
# car.control_motors(0.00, 20.00)
# time.sleep(0.5)
# car.control_motors(0.00, 50.00)
# time.sleep(0.5)
# car.control_motors(0.00, 100.00)
# #back
# time.sleep(0.5)
# car.control_motors(0.00, -9.00)
# time.sleep(0.5)
# car.control_motors(0.00, -20.00)
# time.sleep(0.5)
# car.control_motors(0.00, -50.00)
# time.sleep(0.5)
# car.control_motors(0.00, -100.00)
# time.sleep(0.5)
# #right forward
# car.control_motors(0.00, 0.00)
# time.sleep(0.5)
# car.control_motors(20.00, 100.00)
# time.sleep(0.5)
# car.control_motors(50.00, 100.00)
# time.sleep(0.5)
# car.control_motors(100.00, 100.00)
# #left forward
# time.sleep(0.5)
# car.control_motors(-20.00, 100.00)
# time.sleep(0.5)
# car.control_motors(-50.00, 100.00)
# time.sleep(0.5)
# car.control_motors(-100.00, 100.00)
# time.sleep(0.5)
# #right back
# car.control_motors(0.00, 0.00)
# time.sleep(0.5)
# car.control_motors(20.00, -100.00)
# time.sleep(0.5)
# car.control_motors(50.00, -100.00)
# time.sleep(0.5)
# car.control_motors(100.00, -100.00)
# time.sleep(0.5)
# #left back
# car.control_motors(0.00, 0.00)
# time.sleep(0.5)
# car.control_motors(-20.00, -100.00)
# time.sleep(0.5)
# car.control_motors(-50.00, -100.00)
# time.sleep(0.5)
# car.control_motors(-100.00, -100.00)
# time.sleep(0.5)
# car.control_motors(-0.00, -0.00)
# #test more right then forward
# time.sleep(0.5)
# car.control_motors(100.00, 20.00)
# #test more left then forward
# time.sleep(0.5)
# car.control_motors(-100.00, 20.00)
# #test more right then back
# time.sleep(0.5)
# car.control_motors(100.00, -20.00)
# #test more left then back
# time.sleep(0.5)
# car.control_motors(-100.00, -20.00)
    








##########joystick
#direction = wb.joystick.read()
# while True:
# 
#     direction = wb.joystick.read()
#     x = direction[0] * -1 // 10 + 24
#     y = direction[1] * -1 // 10 + 24
#     
#     left = y + x * -1
#     right = y + x
#     
#     
#     wb.control_motors(left, right)
#     time.sleep(0.1)
#     
    
#     actuel_left_pwm = (left_wheels + 24) *20
#     print("actuel_left_pwm", actuel_left_pwm)
#     
#     actuel_right_pwm = (right_wheels + 24) *20
#     print("actuel_right_pwm", actuel_right_pwm)
#     
#     wb.left_wheels_speed(actuel_left_pwm)
#     wb.right_wheels_speed(actuel_right_pwm)

###########motion sensor
# sensor = hcsr04.HCSR04(trigger_pin=25, echo_pin=26, echo_timeout_us=10000)
# 
# while True:
#     distance = sensor.distance_cm()
#     print('Distance:', distance, 'cm')
#     time.sleep(1)

############### 32 LED strip connected to X8.
# pin = machine.Pin(12, machine.Pin.OUT)
# np = neopixel.NeoPixel(pin, 12)
# 
# while True:
#     np[0] = (255,0,0)
#     np.write()
#     for x in range(1,8):
#         time.sleep(1)
#         np[x - 1] = (0,0,0)
#         np[x] = (255,0,0)
#         np.write()



#brake lights
# while True:
#     car.lights.brake_on()
#     time.sleep(1)
#     car.lights.brake_off()
#     time.sleep(1)