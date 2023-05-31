import ujson
import time
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

            
            module_obj = __import__(device["module"])
            globals()[device["module"]] = module_obj
            
            module = getattr(sys.modules[__name__], device["module"])
            print(deviceclass, name, attributes, module)

            setattr(self, name, getattr(module, deviceclass)(**attributes))
    
