#https://gist.github.com/aallan/3d45a062f26bc425b22a17ec9c81e3b6

import network
import socket
import time

from machine import Pin
import uasyncio as asyncio


ssid = 'Sebastiaan\'s Galaxy S21 5G'
password = 'hahahihi'

html = """<!DOCTYPE html>
<html>
    <head> <title>Pico W</title> </head>
    <body> <h1>Pico W</h1>
        <p>haha</p>
    </body>
</html>
"""

wlan = network.WLAN(network.STA_IF)

def connect_to_network():
    ssid = 'Sebastiaan\'s Galaxy S21 5G'
    password = 'hahahihi'

    station = network.WLAN(network.STA_IF)

    station.active(False)
    time.sleep(1)
    station.active(True)
    time.sleep(1)
    station.connect(ssid, password)

    while station.isconnected() == False:
      pass

    print('Connection successful')
    print(station.ifconfig())

async def serve_client(reader, writer):
    print("Client connected")
    request_line = await reader.readline()
    print("Request:", request_line)
    
    # We are not interested in HTTP request headers, skip them
    while await reader.readline() != b"\r\n":
        pass
    print(request_line) 
    response = html
    writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(response)

    await writer.drain()
    await writer.wait_closed()
    print("Client disconnected")

async def main():
    print('Connecting to Network...')
    connect_to_network()

    print('Setting up webserver...')
    asyncio.create_task(asyncio.start_server(serve_client, "0.0.0.0", 80))
    asyncio.create_task(asyncio.start_server(serve_client, "0.0.0.0", 81))
    while True:
        print("heartbeat")
        await asyncio.sleep(3)
        
try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()