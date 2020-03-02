import socket
import time
import json

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "pong"

def listen_forever():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))

    print("Server started at port {}.".format(UDP_PORT))
    print("Accepting a file upload...")

    # x is used for Testing Purpose
    # x = 0
    data_write = ""

    while True:

        # x += 1
        data, ip = s.recvfrom(BUFFER_SIZE)
        data_recvd = data.decode(encoding="utf-8")

        if "DONE" not in data_recvd:
            msg_dict = json.loads(data.decode(encoding="utf-8").strip())
            # print("Message is ", msg_dict)
            data_upload = msg_dict["data"]
            ack, counter = msg_dict["ack"].split(":")

            data_write += data_upload

            response = {"data": MESSAGE, "ack": ack + ":" + str(int(counter) + 1)} # reply back to the client

            # if x == 10:
            #     time.sleep(5)
            s.sendto(json.dumps(response).encode(), ip)

        else:
            f = open("server_upload.txt", "w")
            f.write(data_write)
            f.close()
            print("Upload successfully completed.")
            data_write = ""

listen_forever()