from umqttsimple import MQTTClient
import time

class mqtt_client():
    
    def __init__(self, mqtt_server, topic, client_id):
        self.__client = MQTTClient(client_id, mqtt_server)
        self.__topic = topic
        
    def publish(self, msg):
        try:
            self.__client.publish(self.__topic, msg)
        except:
            self.__client.connect()
            self.__client.publish(self.__topic, msg)
            self.__client.disconnect()

        
    
        