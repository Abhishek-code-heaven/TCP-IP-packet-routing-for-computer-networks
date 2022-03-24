import socket
import random
import json
import time
n = 10000
randoms = []
x = 0
while x != int(n*(1/100)):
    rand = random.randint(1,n-2)
    if rand in randoms:
        pass
    else:
        x = x+1
        randoms.append(rand)
#randoms = [13,14]
client = '192.168.1.1'
host = '192.168.1.2'
port = 42424                   # The same port as used by the server
print("Client started at IP "+client+" on port "+str(port))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((('192.168.1.2', 42424)))
message = input("-> ")
val = []
while True:
    s.sendall(str.encode(message))
    data = s.recv(1024)
    print('Received', repr(data))
    for i in range(1,n):
        if i in randoms:
            pass
        else:
            s.sendall(str.encode(str(i)))
            data = s.recv(1024)
           
            # print('Received', len(data))
            if len(data) > 6:
                jj = data.decode()
               # print(jj)
                data = json.loads(jj.replace("ACK",""))
                print(data," ","json")
                for d in range(0,len(data['a'][0])):  
                    s.sendall(str.encode(str(data['a'][0][d])))
                    bjh = s.recv(1024)
                    #print('Received', len(bjh))
    break
    # per = 0
    # for i in range(1,1001):
    #     s.sendall(str.encode(str(i))
    #     data = s.recv(1024)
    #     print('Received', repr(data))
        # if i in jj:
        #     pass
        # else:
        #     s.sendall(str.encode(str(i))
        #     data = s.recv(1024)
        #     print('Received', repr(data))
