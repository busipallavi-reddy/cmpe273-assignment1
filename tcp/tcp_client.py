import socket
import sys
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"

def send(id, delay, num_msgs):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    for _ in range(num_msgs):
        print("Sending data: {}".format(MESSAGE))
        s.send(f"{id}:{MESSAGE}".encode())
        data = s.recv(BUFFER_SIZE)
        print("Received data:", data.decode())
        time.sleep(delay)
    s.close()

send(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))