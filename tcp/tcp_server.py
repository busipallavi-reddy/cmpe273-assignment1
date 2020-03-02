import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

def new_connection(conn, addr):
    # print(f'Connection address:{addr}')
    data = conn.recv(BUFFER_SIZE)
    client_id = data.decode().split(":")[0]
    print("Connected Client: {}.".format(client_id))
    print(f"Received data:{data.decode()}")
    conn.send("pong".encode())
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            # print("No data received.")
            break
        print(f"Received data:{data.decode()}")
        conn.send("pong".encode())
    print('Connection closed with client {}'.format(client_id))
    conn.close()

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print("Server started at port {}.".format(TCP_PORT))
    while True:
        conn, addr = s.accept()
        new_client = threading.Thread(target=new_connection, args=(conn, addr))
        new_client.start()

listen_forever()