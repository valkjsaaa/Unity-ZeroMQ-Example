#! /usr/local/bin/python3
import zmq
import time
import random
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:12345")

while True:
	message = str(random.uniform(-1.0, 1.0)) + " " + str(random.uniform(-1.0, 1.0)) + " " + str(random.uniform(-1.0, 1.0))
	socket.send_string(message)
	print(message)
	time.sleep(1)
