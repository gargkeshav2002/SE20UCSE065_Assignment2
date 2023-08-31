# Keshav Garg
# SE20UCSE065

import socket, sys

s = socket.socket()
host = '0.0.0.0'
port = 5555
s.bind((host, port))
       
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

while True:
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print("recv:", message)