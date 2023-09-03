#https://gist.github.com/aallan/3d45a062f26bc425b22a17ec9c81e3b6

import network
import socket
import time
import re
from machine import Pin
import uasyncio as asyncio
import json

def index():
    f = open("index.html", "r")
    return f.read()

def example():
    f = open("example.json", "r")
    return f.read()


wlan = network.WLAN(network.STA_IF)

def connect_to_network():
    ssid = 'chezlaget'
    password = 'haha'

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
    
    headers = []
    while True:
        line = await reader.readline()
        # print("line: "+str(line))
        line = line.decode('utf-8').strip()
        if line == "":
            break
        headers.append(line)
        
    request_raw = str("\r\n".join(headers))
    print(request_raw)
    request_pattern = re.compile(r"(GET|POST)\s+([^\s]+)\s+HTTP")
    match = request_pattern.search(request_raw)
    
    if match:
        protocol = match.group(0)
        method = match.group(1)
        url = match.group(2)
        print(method, url, protocol)
        
    
    if method == "GET":
        writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        
        #add the payload
        if url == "/":
            payload = index()
            content_type = 'Content-Type: text/html\n'
               
               
        elif url == "/example.json":
            payload =  example()
            content_type = 'Content-Type: application/json\n'
                
        else:
            payload = "404 Page not found."
            content_type = 'Content-Type: text/plain\n'
        
        writer.write(payload)

        await writer.drain()
        await writer.wait_closed()
        print("Client disconnected")
        
    if method == "POST":
        content_length_pattern = re.compile(r"Content-Length:\s+(\d+)")
        match = content_length_pattern.search(request_raw)
        boundary_patern = re.compile(r"boundary=(\S*)")
        boundary = boundary_patern.search(request_raw)
        print(request_raw)
        print("boundary == ", boundary.group(1))
        
        if match:
            content_length = int(match.group(1))
            print("content_length: "+str(content_length))
        
        if content_length > 0:
            post_data_raw = await reader.readexactly(content_length)
            post_data = post_data_raw.decode("utf-8")
            print("post_data == ",  post_data)
            
            #Fuck this!!!! there goes my evening: https://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.2
            delimiter1 = "--" + boundary.group(1)
            delimiter2 = "Content-Type: application/json"
            
            post_data = post_data.replace(delimiter2, "*")
            post_data = post_data.replace(delimiter1, "*")

            post_data = post_data.split("*")[2].strip()
            print("post_data === " , post_data)
            
            response = post_data
            content_type = 'Content-Type: application/json\r\n'
            
            
            
            
            writer.write('HTTP/1.1 200 OK\r\n')
            writer.write(content_type)
            writer.write('Connection: close\r\n')
            writer.write('\n')
            await writer.drain()
            writer.write(str(post_data))
            await writer.drain()
            await writer.wait_closed()


async def main():
    print('Connecting to Network...')
    connect_to_network()

    print('Setting up webserver...')
    asyncio.create_task(asyncio.start_server(serve_client, "0.0.0.0", 80))
    asyncio.create_task(asyncio.start_server(serve_client, "0.0.0.0", 81))
    while True:
        await asyncio.sleep(3)

        
try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()
