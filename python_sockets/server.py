import socket 
import time
import pickle 


HEADERSIZE = 10
# socket.socket( family_type , type_of_socket)
# socket is the endpoint that reciesves data, not the communication
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname() , 1234))
s.listen(5) # a queue of 5 connecitons 

while True: 
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established!")

	d = { 1:"Hey" , 2:"There"}
	msg = pickle.dumps(d)
	
	msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

	clientsocket.send(msg)

