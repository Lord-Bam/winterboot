import time
import neopixel
import machine
import components

class Car():
    
    def __init__(self, motor_shield, front_lights, rear_lights, distance_sensor):
        self._motor_shield = motor_shield
        self._motor_shield.all_wheels_stop()
        #prevent overflows
        self._x = 0
        self._x_old_value = 0
        self._y = 0
        self._x_old_value = 0
        self._motor_control_changed = True
        
        self._distance_sensor = distance_sensor
        
        self._front_lights = front_lights
        self._rear_lights = rear_lights
        
        
        self._front_lights.lights_off()
        self._rear_lights.lights_off()
        
        self._emergency_brake = False
        self._dim_lights = False
        self._alarm_lights = False
        
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x_old_value = self._x
        self._x = x
        self._motor_control_changed = True
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        self._y_old_value = self._y
        self._y = y
        self._motor_control_changed = True
        
        
    @property
    def dim_lights(self):
        return self._dim_lights
    
    @dim_lights.setter
    def dim_lights(self, on_off):
        self._dim_lights = on_off
        print(self._dim_lights)
        
    @property
    def alarm_lights(self):
        return self._alarm_lights
    
    @dim_lights.setter
    def alarm_lights(self, on_off):
        self._alarm_lights = on_off
        print(self._alarm_lights)
    
    def start(self):
        print("start your engines")
        offset = time.ticks_ms()
        
        
        while True:
            
            #emergency break.
            #every second distance is checked. If the distance is less than 5 the car immediatly stops.
            if offset + 100 < time.ticks_ms():
                offset = time.ticks_ms()
                distance = self._distance_sensor.distance_cm()
                if distance < 5:
                    self._emergency_brake = True
                    print(f"emergency brake: {distance}")
                    self._x = 0
                    self._y = 0
                    self._control_motors()

                else:
                    self._emergency_brake = False
                
                #check if blinker needs to be lit
                self._front_lights.blinker_lights(self._x)
                self._rear_lights.blinker_lights(self._x)
                
                #check if dim lights need to be switched on             
                if self._dim_lights != self._front_lights.dim_lights:
                    self._front_lights.dim_lights = self.dim_lights
                    self._rear_lights.dim_lights = self.dim_lights
                    
                #alarm lights
                self._front_lights.blink_alarm_lights(self._alarm_lights)
                self._rear_lights.blink_alarm_lights(self._alarm_lights)
                    
                
                

            
            #motor control
            if self._motor_control_changed and self._emergency_brake == False:
                print("in motor control")
                self._motor_control_changed = False
                self._control_motors()
                
                
            #break light control
            #if self._x == 0 or abs(self._x_old_value) - abs(self._x) > 20:
            if self._x == 0:
                self._rear_lights.brake_on()
            else:
                self._rear_lights.brake_off()
       
        
    def _control_motors(self):
        #motorshield only handles int
        print("inside motor control")
        x = int(self._x) * 10
        y = int(self._y) * 10
        
        if not -100 < y < 100:
            if y > 0:
                self._motor_shield.all_wheels_forward()
            else:
                self._motor_shield.all_wheels_back()
                 
        else:
            self._motor_shield.all_wheels_stop()
        
        #set pwm speed:
        self._motor_shield.speed_all_wheels(abs(y))
        
        if not -100 < x < 100:
            if x > 0:
                pwm = abs(x)
                #slow down left wheels
                pwm = max(0, abs(y) - pwm)
                self._motor_shield.speed_left_wheels(pwm)
            else:
                pwm = abs(x)
                #slow down left wheels
                pwm = max(0, abs(y) - pwm)
                self._motor_shield.speed_right_wheels(pwm)
                
                
                
class CarLights():
    
    def __init__(self, pin):
        neo_pixel_pin = machine.Pin(pin, machine.Pin.OUT)
        self._lights = neopixel.NeoPixel(neo_pixel_pin, pin)
        
        self._blinker_direction = "off"
        self._blinker_old_state = False
        self._blinker_state = False
        self._brake_state = "off"
        self._dim_lights = False
        self._alarm_lights_on = False
        self._alarm_lights_old_state = False
        self._alarm_lights_state = False

        
    def brake_on(self):
        if self._brake_state != "on":
            self._brake_state = "on"
            self._lights[1] = (255,0,0)
            self._lights[6] = (255,0,0)
            self._lights.write()

    def brake_off(self):
        if self._brake_state != "off":
            self._brake_state = "off"
            self._lights[1] = (0,0,0)
            self._lights[6] = (0,0,0)
            self._lights.write()
        
    def lights_off(self):
        for x in range(0,7):
            self._lights[x] = (0,0,0)
            self._lights.write()
            
    def blink_alarm_lights(self):
        
        
        if self._alarm_lights_on == True and self._alarm_lights_old_state != self._alarm_lights_state:
            self._alarm_lights_old_state = self._alarm_lights_state
            if time.ticks_ms() // 1000 % 2 == 0:
                for x in range(0,7):
                    self._lights[x] = (0,0,255)
                    self._lights.write()                  
            else:
                for x in range(0,7):
                    self._lights[x] = (0,0,0)
                    self._lights.write() 
                    
        
    def blinker_lights(self, x):
        
        #decide if the blinker "light" should be on or off.
        if time.ticks_ms() // 1000 % 2 == 0:
            self._blinker_state = True
        else:
            self._blinker_state = False
        
        #decide direction:
            
        if self._blinker_state != self._blinker_old_state:
            self._blinker_old_state = self._blinker_state
            
            if self._blinker_state == False:
                self.right_light_off()
                self.left_light_off()
                
            else:
                if x < -20:
                    self._blinker_direction = "left"
                    self.right_light_off()
                    self.left_light_on()
                    
                elif x >= -20 and x <= 20:
                    self._blinker_direction = "off"
                    self.left_light_off()
                    self.right_light_off()
                
                elif x > 20:
                    self._blinker_direction = "right"
                    self.right_light_on()
                    self.left_light_off()


    def left_light_on(self):
        self._lights[0] = (255,255,0)
        self._lights.write()
        print("left light")
        
    def left_light_off(self):
        self._lights[0] = (0,0,0)
        self._lights.write()
        
    def right_light_on(self):
        self._lights[7] = (255,255,0)
        self._lights.write()
        print("right light")
        
    def right_light_off(self):
        self._lights[7] = (0,0,0)
        self._lights.write()


class CarLightsFront(CarLights):
    
    def __init__(self, pin):
        print("in constructor")
        super().__init__(pin)
        
    @property
    def dim_lights(self):
        return self._dim_lights
        
    @dim_lights.setter
    def dim_lights(self, state):
        print("setting lights")
        print(f"{state=}")
        self._dim_lights = state
        print(type(state))
        print(state == 1)
        if state == 1:
            print("in on")
            self._lights[2] = (255,255,255)
            self._lights[5] = (255,255,255)
            self._lights.write()
        else:
            print("in off")
            self._lights[2] = (0,0,0)
            self._lights[5] = (0,0,0)
            self._lights.write()
            
            
class CarLightsRear(CarLights):
    
    def __init__(self, pin):
        print("in constructor")
        super().__init__(pin)
        
    @property
    def dim_lights(self):
        return self._dim_lights
        
    @dim_lights.setter
    def dim_lights(self, state):
        print("setting lights")
        print(f"{state=}")
        self._dim_lights = state
        print(type(state))
        print(state == 1)
        if state == 1:
            print("in on")
            self._lights[2] = (255,0,0)
            self._lights[5] = (255,0,0)
            self._lights.write()
        else:
            print("in off")
            self._lights[2] = (0,0,0)
            self._lights[5] = (0,0,0)
            self._lights.write()
    
           
                

        
        
        
        
        
#          y_direction = "none"
#          x_direction = "none"
#         
        
#         if not -20 < y < 20:
#             if y < 0:
#                 y_direction = "back"
#             else:
#                 y_direction = "forward"
#             
#         if not -20 < x < 20:
#             
#             if x < 0:
#                 x_direction = "left"
#             else:
#                 x_direction = "right"
                
                
        
                
                
        
             
#         return x_direction, y_direction
        
    
    
