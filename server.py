#Imports modules
import socket
# import RPi.GPIO as GPIO
import time
import json
listensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates an instance of socket
Port = 42424 #Port to host server on
#maxConnections = 999
IP = "198.168.1.2" #IP address of local machine

listensocket.bind(('',Port)) 

#Starts server
listensocket.listen()
print("Server started at " + IP + " on port " + str(Port))

#Accepts the incomming connection
(clientsocket, address) = listensocket.accept()


print("New connection made!")

running = True


x = -1
lok = []
miss = []
resv = 0
while running:
    
    message = clientsocket.recv(1024).decode() #Gets the incomming message
    
    if len(message)>0:
        x = x+1
        if x==0:
            clientsocket.send(str.encode("success")) 
            message1 = 1
        else:
            #print(message1,"  ",message)
           
            message = int(message)
            
            if message - message1 >1:
                if len(str(message))-len(str(x))>2:
                    print("check")
                    print(message)
                else:
                
                    maxv = message
                    j = message - message1
                    resv = resv-j
                    
                    for b in range(1,j):
                        miss.append(message1+(b))
                    data = json.dumps({"a":[miss,x]})
                    lok.append(data)
                    miss = []
                    print(lok, " data json")
                    message1 = message
            if message - message1 == 1: 
                message1 = message
            try:
                
                if x - (json.loads(lok[0]))['a'][1] == 100:
                    print(lok, " data json")
                    clientsocket.send(data.encode())
                    lok.pop(0)
                    print(lok)
            except:
                pass
            try:
                if x%1000 == 0:
                    goodput= ((maxv+resv)/maxv)
                    print(goodput," goodput") 
            except:
                pass
            clientsocket.send(str.encode("ACK")) 
 
        