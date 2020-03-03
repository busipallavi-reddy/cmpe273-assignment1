# Assignment 1 - Part A

To support multiple client support for TCP server, made the tcp_server.py multi-threaded by creating a new thread for every new client connection.

**Output:**

**tcp_server_out.txt**

pallavi@desktop:~/Desktop/cmpe273/assignments/cmpe273-assignment1/tcp$ python3 tcp_server.py
Server started at port 5000.
Connected Client: A.
Received data:A:ping
Connected Client: B.
Received data:B:ping
Received data:A:ping
Received data:B:ping
Received data:A:ping
Received data:B:ping
Connection closed with client A
Received data:B:ping
Received data:B:ping
Connection closed with client B

**tcp_clients_out.txt**

pallavi@desktop:~/Desktop/cmpe273/assignments/cmpe273-assignment1/tcp$ python3 tcp_client.py A 10 3
Sending data: ping
Received data: pong
Sending data: ping
Received data: pong
Sending data: ping
Received data: pong

pallavi@desktop:~/Desktop/cmpe273/assignments/cmpe273-assignment1/tcp$ python3 tcp_client.py B 10 5
Sending data: ping
Received data: pong
Sending data: ping
Received data: pong
Sending data: ping
Received data: pong
Sending data: ping
Received data: pong
Sending data: ping
Received data: pong

