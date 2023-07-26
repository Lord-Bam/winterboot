#https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
import winterboot
import __main__
import time
import machine
import sh1106
import json
import ntptime

wb = winterboot.WinterBoot()
led = machine.Pin (2, machine.Pin.OUT)

try:
    ntptime.settime()
except OSError as error:
    print(str("errornr="),error)
    
print(time.localtime())

wb.oled.write_line(0, wb.ip)
wb.oled.write_line(1, str(time.localtime()[0]) + "/" + str(time.localtime()[1]) + "/" + str(time.localtime()[2]))
wb.oled.write_line(2, str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]))

while True:
    json_object = {}
    for key, value in wb.components.items():
        json_object[key] = value.measure()
        
    json_object = json.dumps(json_object)
    print(json_object)
    
    wb.oled.write_line(1, str(time.localtime()[0]) + "/" + str(time.localtime()[1]) + "/" + str(time.localtime()[2]))
    wb.oled.write_line(2, str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]))
    
    #"fake sleeping"
    time.sleep(wb.sleep)


#     machine.sleep(wb.sleep)


