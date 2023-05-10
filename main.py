import machine
import ujson
import winterboot
import time
import sh1106



winter_boot = winterboot.Winter_boot()
print(winter_boot.temp_sensor1.read_temp())

i2c = machine.I2C(scl=machine.Pin(23), sda=machine.Pin(22), freq=400000)
print(i2c.scan())
display = sh1106.SH1106_I2C(128, 60, i2c, machine.Pin(16), 0x3C, rotate=180)
display.sleep(False)
display_line = []
display.fill(0)

for x in range(5):
    display_line.append(str(x))

for x in range(5):
    display.text(display_line[x], 0, x * 10, 1)           

display.show() 

while True:
    if winter_boot.button1.get_interrupt() == True:
        print(winter_boot.button1.value)
        winter_boot.led1.toggle()