#https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
import winterboot
import __main__
from umqttsimple import MQTTClient
import time

import network_service

wifi = network_service.Wifi("chezlaget", "wifi_password.txt")

mqtt_server = '192.168.0.133'
#client_id = ubinascii.hexlify(machine.unique_id())
client_id = "esp32"

topic_pub = "test"
msg = "haha hihi"

client_id, mqtt_server
client = MQTTClient(client_id, mqtt_server)

client.connect()

while True:
    client.publish(topic_pub, msg)
    time.sleep(1)
    print("looping")
    

#wb = winterboot.WinterBoot()