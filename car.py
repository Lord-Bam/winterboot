import time

class Car():
    
    def __init__(self, motor_shield, lights):
        self.motor_shield = motor_shield
        self.motor_shield.all_wheels_stop()
        #prevent overflows
        self.timer =  time.ticks_ms()
        self.x = 0
        self.y = 0
        
        self.lights = lights.np
        for x in range(0,7):
            self.lights[x] = (0,0,0)
            self.lights.write()
        
        
        
        

        
        
    def control_motors(self, x, y):
        #motorshield only handles int
        x = int(x)* 10
        y = int(y)* 10
        
        if not -100 < y < 100:
            if y > 0:
                print("vooruit")
                self.motor_shield.all_wheels_forward()
            else:
                print("achteruit")
                self.motor_shield.all_wheels_back()
                

            
        else:
            print("stop")
            self.motor_shield.all_wheels_stop()
        
        #set pwm speed:
        self.motor_shield.speed_all_wheels(abs(y))
        
        if not -100 < x < 100:
            if x > 0:
                pwm = abs(x)
                #slow down left wheels
                pwm = max(0, abs(y) - pwm)
                print(pwm)
                self.motor_shield.speed_left_wheels(pwm)
            else:
                pwm = abs(x)
                #slow down left wheels
                pwm = max(0, abs(y) - pwm)
                print(pwm)
                self.motor_shield.speed_right_wheels(pwm)
            

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
        
    
    
