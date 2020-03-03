import socket
import uuid
import json
from itertools import islice

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "ping"
RETRY_COUNT = 5
PACKET_SIZE = 10

def read_next_packet(file_opened, N):
    return "".join([x for x in islice(file_opened, N)])

def send_packet(s, packet, seq, counter):

    try:
        msg_dict = {}
        msg_dict["data"] = packet
        msg_dict["ack"] = str(seq) + ":" + str(counter)
        msg = json.dumps(msg_dict)

        s.sendto(f"{msg}".encode(), (UDP_IP, UDP_PORT))
        s.settimeout(0.02)
        # print("Sent message ", msg_dict["data"])

        data, ip = s.recvfrom(BUFFER_SIZE)
        response = json.loads(data.decode(encoding="utf-8"))
        # print(response)

        print("Received ack({}) from the server.".format(response["ack"]))

        return True, response["ack"]

    except socket.timeout:
        print("This msg was not received by server: ", msg_dict["data"])

    return False, -1

def send():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Connected to the server.")

        s.setblocking(True) # Optional. By default, UDP socket is running on blocking mode.

        f = open("upload.txt")
        packet = read_next_packet(f, PACKET_SIZE)

        while packet:
            counter = 0
            seq = uuid.uuid4() # seq is a unique identifier for each package to be sent

            # Trying to send packet for 5 times if not received by server client will end
            while counter < RETRY_COUNT:
                counter += 1

                success, ack  = send_packet(s, packet, seq, counter)
                ack_received, counter_received = ack.split(":")

                if success and ack_received == str(seq) and int(counter_received) == int(counter + 1):
                    break

            if counter == RETRY_COUNT:
                print("File upload failed. Client Exiting!")
                exit()

            packet = read_next_packet(f, PACKET_SIZE)

    except socket.error:
        print("Error! {}".format(socket.error))
        exit()

    s.sendto("DONE".encode(), (UDP_IP, UDP_PORT))
    print("File upload successfully completed.")
    s.close()

# def get_client_id():
#     id = input("Enter client id:")
#     return id

send()