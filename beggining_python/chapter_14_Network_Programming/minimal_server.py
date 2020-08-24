import socket 

s = socket.socket() 

host = socket.gethostname() 
port = 1234 
s.bind((host, port)) 

s.listen(5)

while True: 
    c, addr = s.accept()
    print(c) 
    print("Got connection form:", addr)
    c.send(b"Thank you for connecting!")
    c.close()