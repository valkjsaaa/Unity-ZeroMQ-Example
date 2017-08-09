#! /usr/local/bin/python3
import zmq
import time
import random
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:12346")

TIMEOUT = 10000

while True:
	socket.send_string("request")
	poller = zmq.Poller()
	poller.register(socket, zmq.POLLIN)
	evt = dict(poller.poll(TIMEOUT))
	if evt:
		if evt.get(socket) == zmq.POLLIN:
			response = socket.recv(zmq.NOBLOCK)
			print(response)
			continue
	time.sleep(0.5)
	socket.close()
	socket = context.socket(zmq.REQ)
	socket.connect("tcp://localhost:12346")
