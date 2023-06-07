import machine
import time


class MotorShield():
    
    def __init__(self, dir_latch, dir_clk, dir_ser, pwm_pin1, pwm_pin2, pwm_pin3, pwm_pin4):
        self.dir_latch = machine.Pin(dir_latch, machine.Pin.OUT)
        self.dir_clk = machine.Pin(dir_clk, machine.Pin.OUT)
        self.dir_ser = machine.Pin(dir_ser, machine.Pin.OUT)

        self.pwm1 = machine.PWM(machine.Pin(pwm_pin1))
        self.pwm1.freq(800)
        self.pwm1.duty(1023)

        self.pwm2 = machine.PWM(machine.Pin(pwm_pin2))
        self.pwm2.freq(800)
        self.pwm2.duty(1023)

        self.pwm3 = machine.PWM(machine.Pin(pwm_pin3))
        self.pwm3.freq(800)
        self.pwm3.duty(1023)

        self.pwm4 = machine.PWM(machine.Pin(pwm_pin4))
        self.pwm4.freq(800)
        self.pwm4.duty(1023)
        
        self.motorstates = [0,0,0,0,0,0,0,0]
        self.shift_write(self.motorstates)

    #dir_en.off()

    def pulse_clock(self):  
        self.dir_clk.value(1)
        self.dir_clk.value(0)

    def pulse_latch(self):  
        self.dir_latch.value(1)
        self.dir_latch.value(0)

    def shift_write(self, motorstates):
        for motorstate in self.motorstates:
            if motorstate == 1:
                self.dir_ser.on()          
            else:
                self.dir_ser.off()          
                
            self.pulse_clock()
            
        self.pulse_latch()
        print()
        
    def forward(self):
        #set motostate to full stop
        self.motorstates = [0 for motor in self.motorstates]
        #set all engines to forward
        self.motorstates[5] = 1
        self.motorstates[6] = 1
        self.motorstates[2] = 1
        self.motorstates[7] = 1
        self.shift_write(self.motorstates)
        
    def back(self):
        #set motostate to full stop
        self.motorstates = [0 for motor in self.motorstates]
        #set all engines to forward
        self.motorstates[4] = 1
        self.motorstates[3] = 1
        self.motorstates[0] = 1
        self.motorstates[1] = 1
        self.shift_write(self.motorstates)
        
    def stop(self):
        #set motostate to full stop
        self.motorstates = [0 for motor in self.motorstates]
        self.shift_write(self.motorstates)
        
      
    #motor 1
    def left_front_forward(self):
        self.motorstates[4] = 0
        self.motorstates[5] = 1
        self.shift_write(self.motorstates)
        
    def left_front_back(self):
        self.motorstates[4] = 1
        self.motorstates[5] = 0
        self.shift_write(self.motorstates)
        
    def left_front_stop(self):
        self.motorstates[4] = 0
        self.motorstates[5] = 0
        self.shift_write(self.motorstates)

    #motor2
    def right_front_forward(self):
        self.motorstates[3] = 0
        self.motorstates[6] = 1
        self.shift_write(self.motorstates)
        
    def right_front_back(self):
        self.motorstates[3] = 1
        self.motorstates[6] = 0
        self.shift_write(self.motorstates)
        
    def right_front_stop(self):
        self.motorstates[3] = 0
        self.motorstates[6] = 0
        self.shift_write(self.motorstates)
        
    #motor 3
    def left_rear_forward(self):
        self.motorstates[0] = 0
        self.motorstates[2] = 1
        self.shift_write(self.motorstates)
        
    def left_rear_back(self):
        self.motorstates[0] = 1
        self.motorstates[2] = 0
        self.shift_write(self.motorstates)
        
    def left_rear_stop(self):
        self.motorstates[0] = 0
        self.motorstates[2] = 0
        self.shift_write(self.motorstates)
        
    #motor 4
    def right_rear_forward(self):
        self.motorstates[1] = 0
        self.motorstates[7] = 1
        self.shift_write(self.motorstates)
        
    def right_rear_back(self):
        self.motorstates[1] = 1
        self.motorstates[7] = 0
        self.shift_write(self.motorstates)
        
    def right_rear_stop(self):
        self.motorstates[1] = 0
        self.motorstates[7] = 0
        self.shift_write(self.motorstates)
        
        
    def left_wheels_forward(self):
        self.motorstates[4] = 0
        self.motorstates[5] = 1
        self.motorstates[0] = 0
        self.motorstates[2] = 1
        self.shift_write(self.motorstates)
        
    def left_wheels_back(self):
        self.motorstates[4] = 1
        self.motorstates[5] = 0
        self.motorstates[0] = 1
        self.motorstates[2] = 0
        self.shift_write(self.motorstates)
        
    def left_wheels_stop(self):
        self.motorstates[4] = 0
        self.motorstates[5] = 0
        self.motorstates[0] = 0
        self.motorstates[2] = 0
        self.shift_write(self.motorstates)
        
        
    def right_wheels_forward(self):
        self.motorstates[3] = 0
        self.motorstates[6] = 1
        self.motorstates[1] = 0
        self.motorstates[7] = 1
        self.shift_write(self.motorstates)

        
    def right_wheels_back(self):
        self.motorstates[3] = 1
        self.motorstates[6] = 0
        self.motorstates[1] = 1
        self.motorstates[7] = 0
        self.shift_write(self.motorstates)
        
    def right_wheels_stop(self):
        self.motorstates[3] = 0
        self.motorstates[6] = 0
        self.motorstates[1] = 0
        self.motorstates[7] = 0
        self.shift_write(self.motorstates)


    def all_wheels_forward(self):
        self.left_wheels_forward()
        self.right_wheels_forward()

    def all_wheels_back(self):
        self.left_wheels_back()
        self.right_wheels_back()

    def all_wheels_stop(self):
        self.left_wheels_stop()
        self.right_wheels_stop()
        
    def speed_left_wheels(self, speed):
        self.pwm1.duty(speed)
        self.pwm2.duty(speed)
        
    def speed_right_wheels(self, speed):
        self.pwm3.duty(speed)
        self.pwm4.duty(speed)
        
    def speed_all_wheels(self, speed):
        self.speed_left_wheels(speed)
        self.speed_right_wheels(speed)
        

            
        
        
#         self.left_wheels_back() if left < 0 else  self.left_wheels_forward()
#         self.right_wheels_back() if right < 0 else  self.right_wheels_forward()
#         
#         #left_pwm
#         left_pwm = abs(left)* 40
#         
#         if left_pwm < 0: left_pwm = 0 
#         if left_pwm > 1023: left_pwm = 1023 
#         self.pwm1.duty(left_pwm)
#         self.pwm2.duty(left_pwm)
#         
#         #right_pwm
#         
#         right_pwm = abs(right)* 40
#         
#         if right_pwm < 0: right_pwm = 0 
#         if right_pwm > 1023: right_pwm = 1023 
#         self.pwm3.duty(right_pwm)
#         self.pwm4.duty(right_pwm)
#         
#         print(f'{left_pwm=}, {right_pwm=}')
        
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
    
        
        
#     msgstr = ""
#     self.motorstates = [0,0,0,0,0,0,0,0]
#     shift_write(motorstates)
# 
#     while True:
#         msgstr = input()
#         old_motorstates = motorstates.copy()
#         
#         #motor1
#         if msgstr == "1/v":
#             motorstates[4] = 0
#             motorstates[5] = 1
# 
#         elif msgstr == "1/a":
#             motorstates[4] = 1
#             motorstates[5] = 0
#             
#         elif msgstr == "1/0":
#             motorstates[5] = 0
#             motorstates[4] = 0
#             
#         #motor2
#         elif msgstr == "2/v":
#             motorstates[3] = 0
#             motorstates[6] = 1
#             
#         elif msgstr == "2/a":
#             motorstates[3] = 1
#             motorstates[6] = 0
#             
#         elif msgstr == "2/0":
#             motorstates[3] = 0
#             motorstates[6] = 0
#             
#         #motor3
#         elif msgstr == "3/v":
#             motorstates[0] = 0
#             motorstates[2] = 1
#             
#         elif msgstr == "3/a":
#             motorstates[0] = 1
#             motorstates[2] = 0
#             
#         elif msgstr == "3/0":
#             motorstates[0] = 0
#             motorstates[2] = 0
#             
#         #motor4
#         elif msgstr == "4/v":
#             motorstates[1] = 0
#             motorstates[7] = 1
#             
#         elif msgstr == "4/a":
#             motorstates[1] = 1
#             motorstates[7] = 0
#             
#         elif msgstr == "4/0":
#             motorstates[1] = 0
#             motorstates[7] = 0
#             
#         elif msgstr == "a/v":
#             motorstates = [0 for motor in motorstates]
#             motorstates[5] = 1
#             motorstates[6] = 1
#             motorstates[2] = 1
#             motorstates[7] = 1
#             
#             
#         elif msgstr == "a/a":
#             motorstates = [0 for motor in motorstates]
#             motorstates[4] = 1
#             motorstates[3] = 1
#             motorstates[0] = 1
#             motorstates[1] = 1
#         
#         elif msgstr == "a/0":
#             motorstates = [0 for motor in motorstates]
# 
#             
#         else:
#             print("verkeerd commando")
#             
#         if motorstates != old_motorstates:
#             shift_write(motorstates)
