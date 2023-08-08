#https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
import winterboot
import __main__
import time
import machine
import sh1106
import json
import ntptime
import webserver

wb = winterboot.WinterBoot()
# led = machine.Pin (2, machine.Pin.OUT)

try:
    ntptime.settime()
except OSError as error:
    print(str("errornr="),error)
    
print(time.localtime())
wb.oled.write_line(0, wb.host)
wb.oled.write_line(1, wb.ip)

webserver.run()


while True:
    host_date = str(time.localtime()[0]) + "/" + str(time.localtime()[1]) + "/" + str(time.localtime()[2])
    host_time = str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]) 
    
    wb.oled.write_line(2, host_date)
    wb.oled.write_line(3, host_time)
    
    json_object = {}
    json_object["host"] = wb.host
    json_object["date"] = host_date
    json_object["time"] = host_time
    
    
    
    for key, value in wb.components.items():
        json_object[key] = value.measure()
        
    
        
    json_object = json.dumps(json_object)
    print(json_object)

    
    wb.mqtt_client.publish(json_object)
    #"fake sleeping"
    time.sleep(wb.sleep)


#     machine.sleep(wb.sleep)


