import machine
import components
import ujson
import time
import winterboot
import motorshield



wb = winterboot.WinterBoot()


wb.led1.on()
time.sleep(1)
wb.led1.off()

wb.motor_shield.forward()
time.sleep(1)
wb.motor_shield.back()
time.sleep(1)
wb.motor_shield.stop()





# with open("config.json") as fp:
#     data = ujson.loads(fp.read())
# 
# for device in data["devices"]:
#     print(device)
#     print(device["device_class"])
#     print(device["name"])
# 
# 
# motorshield = motorshield.MotorShield(data["devices"][1]["attributes"])
# print(motorshield.motorstates)
# motorshield.forward()
# time.sleep(1)
# motorshield.back()


# print(data["devices"][0]["attributes"])
# print(type(data["devices"][0]["attributes"]))
# 
# led1 = components.Led(data["devices"][0]["attributes"])
# led1.on()
# time.sleep(1)
# led1.off()







# led1 = components.Led(pin=13, hihi="haha")
# led1.on()
# time.sleep(1)
# led1.off()





# print(winter_boot.temp_sensor1.read_temp())


# my_pin = components.WinterPin(13, "out")
# my_pin.value(1)
# time.sleep(0.5)
# my_pin.value(0)

# while True:
#     print("test")
#     time.sleep(1)

# winter_boot = winterboot.Winter_boot()
# print(winter_boot.temp_sensor1.read_temp())
# 
# i2c = machine.I2C(scl=machine.Pin(23), sda=machine.Pin(22), freq=400000)
# print(i2c.scan())
# display = sh1106.SH1106_I2C(128, 60, i2c, machine.Pin(16), 0x3C, rotate=180)
# display.sleep(False)
# display_line = []
# display.fill(0)
# 
# for x in range(5):
#     display_line.append(str(x))
# 
# for x in range(5):
#     display.text(display_line[x], 0, x * 10, 1)           
# 
# display.show() 
# 
# while True:
#     if winter_boot.button1.get_interrupt() == True:
#         print(winter_boot.button1.value)
#         winter_boot.led1.toggle()