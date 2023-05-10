import classes
import ujson
import time

class Winter_boot:

    def __init__(self):
        print("constructor")
        with open("config.json") as fp:
            data = ujson.loads(fp.read())
            
        
        #temp_sensor
        deviceclass = data["devices"][0]["device_class"]
        pin = data["devices"][0]["pin"]
        name = data["devices"][0]["name"]

        setattr(self, name, getattr(classes, deviceclass)(pin))

        print(self.temp_sensor1.read_temp())
        
        
        #led
        deviceclass = data["devices"][1]["device_class"]
        pin = data["devices"][1]["pin"]
        name = data["devices"][1]["name"]
        
        setattr(self, name, getattr(classes, deviceclass)(pin))
        print(self.led1)
        self.led1.on()
        time.sleep(1)
        self.led1.off()
        
        #button
        deviceclass = data["devices"][2]["device_class"]
        pin = data["devices"][2]["pin"]
        name = data["devices"][2]["name"]
        interrupt_variable = data["devices"][2]["interrupt_variable"]
        
        
        #set a variabel and pass the variable to the button interrupt handler.
        #from the main we can check this class variable to see if an interrupt happened.
        setattr(self, name, getattr(classes, deviceclass)(pin, interrupt_variable))
       
        

    def create_devices(self):
        print("creating devices")
    
