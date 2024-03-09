def send(from_,to,password,text,filePath,isFile):
    if isFile:
        with open(filePath,"rb") as f:
            file=f.read()
        fileName=filePath
    else:
        file=None
        fileName=None
    x={"from":from_,"to":to,"password":password,"text":text,"file":file,"fileName":fileName}
    with open("promFile","wb") as f:
        f.write(pickle.dumps(x))
    sock = socket.socket()
    sock.connect(('localhost', 9090))
    f=open("promFile","rb")
    l=f.read(1024)
    while (l):
        sock.send(l)
        l=f.read()
    f.close()
    sock.close()



import socket,pickle
"""
sock = socket.socket()
sock.connect(('localhost', 9090))
with open("pckFL.dat","wb") as file:
    pickle.dump({"1":"2"},file)
f=open("pckFL.dat","rb")
l=f.read(1024)
while (l):
    sock.send(l)
    l=f.read(1024)
f.close()
sock.close()"""
send("1","12","1","sdffds","1",False)