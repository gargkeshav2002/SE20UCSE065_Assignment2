#Keshav Garg
#SE20UCSE065

import time, socket, sys

s = socket.socket()
host = "139.59.15.75"
port = 5555
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

while True:
    message = s.recv(1024)
    message = message.decode()
    print("recv:", message)
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())