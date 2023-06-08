#https://github.com/lavron/micropython-dfplayermini

# from dfplayermini import Player
# 
# from time import sleep
# 
# music = Player(pin_RX=16, pin_TX=17)
# 
# print("set volume")
# music.volume(20)
# music.resume()
# print("start play")
# music.play(1)



###########################
# Some winterboot testing #
###########################
import components
import time

np = components.NeoPixel(12)

       
led1 = components.Led(14)

while True:
    led1.toggle()
    time.sleep(1)

while True:
    np[0] = (255,0,0)
    np.write()
    for x in range(1,8):
        time.sleep(1)
        np[x - 1] = (0,0,0)
        np[x] = (255,0,0)
        np.write()
