import machine
import ds18x20
import onewire
import time


class Temp_sensor:
    
    def __init__(self, pin):
        print("constructor")
        _ds_pin = machine.Pin(pin)
        self._ds_sensor = ds18x20.DS18X20(onewire.OneWire(_ds_pin))
        _roms = self._ds_sensor.scan()
        print("Found DS devices: ", _roms)
        self._rom = _roms[0]
        
        
    def read_temp(self):
        self._ds_sensor.convert_temp() #needs to be done everytime you read a value.
        current_temp = self._ds_sensor.read_temp(self._rom)
        return current_temp
    
    
class Led:

    def __init__(self, pin):
        print("constructor")
        self.led = machine.Pin(pin, machine.Pin.OUT)
        
    def on(self):
        self.led.value(1)
        
    def off(self):
        self.led.value(0)
        
        
        
class Button():
    #https://docs.micropython.org/en/latest/library/machine.Pin.html
    #https://docs.micropython.org/en/latest/reference/isr_rules.html#isr-rules
    #
    def haha(self, pin):
        if self.debouncer + 30 < time.ticks_ms():
            time.sleep(0.01)
            self.debouncer = time.ticks_ms()
            print(pin.value())
    
    def __init__(self, pin, interrupt_variable):
        self.debouncer = time.ticks_ms()
        button = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)
        function = "self." + interrupt_handler
        print(function)
        button.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=function)
        



#     ds_pin = machine.Pin(4)
#     ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
#     roms = ds_sensor.scan()
#     print("Found DS devices: ", roms)
#     rom = roms[0]
# 
# 
#     ds_sensor.convert_temp() #needs to be done everytime you read a value.
#     current_temp = ds_sensor.read_temp(rom)
#     print(current_temp)
