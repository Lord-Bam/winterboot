import components
import ujson
import time
import motorshield
import sys

class WinterBoot:

    def __init__(self):
             
        with open("config.json") as fp:
            data = ujson.loads(fp.read())
        
        
        for device in data["devices"]:
            print(device)
            deviceclass = device["device_class"]
            name = device["name"]
            attributes = device["attributes"]
            module = getattr(sys.modules[__name__], device["module"])
            print(deviceclass, name, attributes, module)
            setattr(self, name, getattr(module, deviceclass)(attributes))
        
        
        
        
        
#         parent.led1.on()
#         time.sleep(1)
#         parent.led1.off()
# 
#         print(self.temp_sensor1.read_temp())
        
        
        #led
#         deviceclass = data["devices"][1]["device_class"]
#         pin = data["devices"][1]["pin"]
#         name = data["devices"][1]["name"]
#         
#         setattr(self, name, getattr(components, deviceclass)(pin))


        #button
#         deviceclass = data["devices"][2]["device_class"]
#         pin = data["devices"][2]["pin"]
#         name = data["devices"][2]["name"]
        
        
        #set a variabel and pass the variable to the button interrupt handler.
        #from the main we can check this class variable to see if an interrupt happened.
#         setattr(self, name, getattr(components, deviceclass)(pin))
       
        

    def create_devices(self):
        print("creating devices")
    
