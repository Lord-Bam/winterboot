from umqttsimple import MQTTClient
import time

class mqtt_client():
    
    def __init__(self, mqtt_server, client_id, topic, username, password):
        self.__client = MQTTClient(client_id, mqtt_server, port=1883, user=username, password=password, ssl=False)
        self.__topic = topic
        
    def publish(self, msg):
        try:
            self.__client.publish(self.__topic, msg)
        except:
            self.__client.connect()
            self.__client.publish(self.__topic, msg)
            self.__client.disconnect()

        
    
        