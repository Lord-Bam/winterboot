import machine
import classes
import ujson
import Create_classes
import time


# led = machine.Pin(13, machine.Pin.OUT)
# led.value(0)

debouncer = time.ticks_ms()


winter_boot = Create_classes.Winter_boot()
print(winter_boot.temp_sensor1.read_temp())

# def handle_interrupt(pin):
#     global debouncer
#     if debouncer + 30 < time.ticks_ms():
#         time.sleep(0.01)
#         debouncer = time.ticks_ms()
#         print(pin.value())
# 
# button1 = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
# button1.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=handle_interrupt)
# print(dir(button1))


# with open("config.json") as fp:
#     data = ujson.loads(fp.read())
#     
#     
# print(data)
# print(data["devices"])
# print(data["devices"][0])
# print(data["devices"][0])


# winter_boot.create_devices()