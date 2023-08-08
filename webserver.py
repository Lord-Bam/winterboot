import usocket as socket
import json
import network
import time
import uasyncio as asyncio

def index():
    f = open("index.html", "r")
    return f.read()

def example():
    f = open("example.json", "r")
    return f.read()


async def bar(x, y):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        await asyncio.sleep(y)  # Pause 1s

async def run():
    #create websocket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 80))
    s.listen(5)

    while True:
        #Listen on the socket.
        conn, addr = s.accept()
        #print('Got a connection from %s' % str(addr))
        request = conn.recv(4096)

        #Decode and split the request to get the HTTP method.
        print("request: ", str(request.decode("utf-8")))
        request = str(request.decode("utf-8"))
        request_array = request.split("\r\n")
        url = request_array[0].split(" ")[1]
        
        print("url:", url)
#         for x in range(0,len(request_array)):
#             print(x, request_array[x])
        
        payload = "404"
        if "GET" in request_array[0]:
        
            if url == "/":
               payload = index()
               content_type = 'Content-Type: text/html\n'
               
               
            elif url == "/example.json":
                payload =  example()
                content_type = 'Content-Type: application/json\n'
                
            else:
                payload = "404"
                content_type = 'Content-Type: text/plain\n'
            
        
        if "POST" in request_array[0]:
            try:
                print("request header length: ",len(request_array))
                payload = request_array[17]
                content_type = 'Content-Type: application/json\n'
                
            except:
                payload = "something went wrong"
                content_type = 'Content-Type: text/plain\n'
                print("exception")
        
        #Sending response.
        conn.send('HTTP/1.1 200 OK\r\n')
        conn.send(content_type)
        conn.send('Connection: close\r\n')
        conn.send('\n')
        conn.sendall(payload)
        conn.close()     



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


async def main():
    task1 = asyncio.create_task(bar(1, 1))
    task2 = asyncio.create_task(bar(2, 2))
    task3 = asyncio.create_task(run())

    
    while True:
        print("test")
        time.sleep(5)
    


#     # running task
#     task = asyncio.create_task(bar(1, 1))
#     await asyncio.sleep(0)  # bar has now started
#     task = asyncio.create_task(bar(1, 1))

asyncio.run(main())







