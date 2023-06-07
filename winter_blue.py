from ble_uart import BLEUART
import bluetooth
    
    
class WinterBlue():
    
    def __init__(self, name, handler):
        print("creating bluetooth")
    
        ble = bluetooth.BLE()
        uart = BLEUART(ble, name)

        def on_rx():
#             print("rx: ", uart.read().decode().strip())
            handler(uart.read().decode().strip())

        uart.irq(handler=on_rx)
        uart.close()
