import time

class Car():
    
    def __init__(self, motor_shield, lights, distance_sensor):
        self._motor_shield = motor_shield
        self._motor_shield.all_wheels_stop()
        #prevent overflows
        self._x = 0
        self._x_old_value = 0
        self._y = 0
        self._x_old_value = 0
        self._motor_control_changed = True
        
        self._distance_sensor = distance_sensor
        
        self.lights = lights
        for x in range(0,7):
            self.lights[x] = (0,0,0)
            self.lights.write()
            
        self._emergency_brake = False
        
    
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
    
    
    def start(self):
        print("start your engines")
        offset = time.ticks_ms()
        
        
        while True:
            
            #emergency break.
            #every second distance is checked. If the distance is less than 5 the car immediatly stops.
            if offset + 1000 < time.ticks_ms():
                offset = time.ticks_ms()
                distance = self._distance_sensor.distance_cm()
                if distance < 5:
                    self._emergency_brake = True
                    print(f"emergency brake: {distance}")
                    self._motor_shield.all_wheels_stop()
                    self._x = 0
                    self._y = 0
                else:
                    self._emergency_brake = False
                

                if abs(self._x) > 20:
                    print("blinker")
                
                else:
                    print("blinker off")
                    
                

            
            #motor control
            if self._motor_control_changed and self._emergency_brake == False:
                #print(f"{self._x=}, {self._y=}")
                self._motor_control_changed = False
                self._control_motors()
                
            #break light control
#             if self._x == 0 or abs(self._x_old_value) - abs(self._x) > 20:
#                 print("breaking")

                
                
            

        
        
    def _control_motors(self):
        #motorshield only handles int
        x = int(self._x) * 10
        y = int(self._y) * 10
        
        if not -100 < y < 100:
            if y > 0:
                print("vooruit")
                self._motor_shield.all_wheels_forward()
            else:
                print("achteruit")
                self._motor_shield.all_wheels_back()
                

            
        else:
            print("stop")
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
            

    def left_light_on(self):
        self.lights[0] = (255,0,0)
        self.lights.write()
        print("left light")
        
    def left_light_off(self):
        self.lights[0] = (0,0,0)
        self.lights.write()
        print("left light")
        
    def right_light_on(self):
        self.lights[7] = (255,0,0)
        self.lights.write()
        print("right light")
        
    def left_right_off(self):
        self.lights[7] = (0,0,0)
        self.lights.write()
        print("left light")
    
           
                

        
        
        
        
        
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
        
    
    
