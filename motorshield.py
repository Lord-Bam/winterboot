import machine
import time


class MotorShield():
    
    def __init__(self, args):
        self.dir_latch = machine.Pin(args["dir_latch"], machine.Pin.OUT)
        self.dir_clk = machine.Pin(args["dir_clk"], machine.Pin.OUT)
        self.dir_ser = machine.Pin(args["dir_ser"], machine.Pin.OUT)

        self.pwm1 = machine.PWM(machine.Pin(args["pwm_pin1"]))
        self.pwm1.freq(800)
        self.pwm1.duty(1023)

        self.pwm2 = machine.PWM(machine.Pin(args["pwm_pin2"]))
        self.pwm2.freq(800)
        self.pwm2.duty(1023)

        self.pwm3 = machine.PWM(machine.Pin(args["pwm_pin3"]))
        self.pwm3.freq(800)
        self.pwm3.duty(1023)

        self.pwm4 = machine.PWM(machine.Pin(args["pwm_pin4"]))
        self.pwm4.freq(800)
        self.pwm4.duty(1023)
        
        self.motorstates = [0,0,0,0,0,0,0,0]
        print(self.motorstates)
        self.shift_write(self.motorstates)

    #dir_en.off()

    def pulse_clock(self):  
        self.dir_clk.value(1)
        self.dir_clk.value(0)

    def pulse_latch(self):  
        self.dir_latch.value(1)
        self.dir_latch.value(0)

    def shift_write(self, motorstates):
        print(self.motorstates)
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
    

        
        
#     msgstr = ""
#     motorstates = [0,0,0,0,0,0,0,0]
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
