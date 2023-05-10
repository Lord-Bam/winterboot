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
        
    def toggle(self):
        if self.led.value() == 0:
            self.led.value(1)
        else:
            self.led.value(0)
        
class Button():
    #https://docs.micropython.org/en/latest/library/machine.Pin.html
    #https://docs.micropython.org/en/latest/reference/isr_rules.html#isr-rules
    #
    
    def interrupt_handler(self, pin):
        if self.debouncer + 30 < time.ticks_ms():
            time.sleep(0.01)
            self.debouncer = time.ticks_ms()
            self.value = pin.value()
            self.interrupt = True
    
    def __init__(self, pin):
        self.debouncer = time.ticks_ms()
        button = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)
        button.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=self.interrupt_handler)
        self.value = button.value()
        self.interrupt = False
        
    @property
    def getvalue(self):
        return self.value
    
    def get_interrupt(self):
        return_value =  self.interrupt
        self.interrupt = False
        return return_value