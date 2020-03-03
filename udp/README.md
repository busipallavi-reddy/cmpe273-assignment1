# Assignment 1 - Part B

To make UDP reliable and upload the file, designed the protocol as follows:

* PACKET_SIZE is the number of lines each packet contains. Here, I have assumed that each packet sent to the server consists of 10 lines from the file.
* For each packet, uuid is generated with a retry counter initialized to 1 and is then sent over to the server.
* When the server receives a packet, it sends the acknowledgement back to the client which is the uuid received plus the value of retry counter received+1, and the server writes the data to a file, only if the uuid is not seen before. To handle duplicate requests, the received uuids are stored at the server and before writing to a file, the uuid is first checked that it was never received before.
* The client receives the acknowledgement, checks if the uuid is same as that sent and the retry counter is 1 more than the retry counter sent. If yes, the client moves on to read next PACKET_SIZE data and sends to the server. If there was a mismatch or the ack was not received for any reason, the client retries sending the same packet. This controls the package order.
* RETRY_COUNT is set to 5. If the packet is still not received by the server, the client exits and upload fails.
* If all is fine, all packets are received by the server, the upload is complete and is written to server_upload.txt.

**Output:**

**udp_client_out.txt**

```
Connected to the server.
Received ack(d7167a7e-7f70-4394-a9e5-68290c06602a:2) from the server.
Received ack(8855b4c8-d5a4-44e0-bb41-e3d5894ac7ec:2) from the server.
Received ack(8a40e7ec-dcec-45e4-b390-3d0b09549935:2) from the server.
Received ack(36fe5e1b-df0b-4351-bb31-b6a112166670:2) from the server.
Received ack(368dca05-abf2-491e-ae79-bf027a9fd49f:2) from the server.
.
.
.
Received ack(043013e6-5afd-4c7b-835b-adc361d47075:2) from the server.
Received ack(1dc57811-8805-40cd-bf8f-76890128cbf6:2) from the server.
Received ack(6bc6712c-b0b3-4387-9ad3-e34af59b071b:2) from the server.
Received ack(e0832359-6d78-49c5-b3e0-caa2b6675505:2) from the server.
Received ack(7db200c1-bfe4-48da-a252-a8e868960781:2) from the server.
File upload successfully completed.

```

**udp_server_out.txt**

```
Server started at port 4000.
Accepting a file upload...
Upload successfully completed.
```

