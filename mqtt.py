#https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
import winterboot
import __main__
from umqttsimple import MQTTClient
import time
import network

wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(True)

wlan_sta.disconnect()
wlan_sta.connect("Sebastiaan's Galaxy S21 5G", "hahahihi")
for retry in range(200):
    connected = wlan_sta.isconnected()
    if connected:
        break
    time.sleep(0.1)
    print('.', end='')
if connected:
    print('\nConnected. Network config: ', wlan_sta.ifconfig())


mqtt_server = '192.168.68.70'
#client_id = ubinascii.hexlify(machine.unique_id())
client_id = "esp32"

topic_pub = "test"
msg = "haha hihi"

time.sleep(2)

client_id, mqtt_server
client = MQTTClient(client_id, mqtt_server,keepalive=5)
time.sleep(2)
client.connect()

while True:
    try:
        client.publish(topic_pub, msg)
    except:
        client.connect()
        client.publish(topic_pub, msg)
        client.disconnect()
    time.sleep(10)
    print("looping")
    

#wb = winterboot.WinterBoot()