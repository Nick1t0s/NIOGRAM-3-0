import pickle

def sendDic(dic):
    dataB = pickle.dumps(dic)
    with open("clientMessageDB.cldt", "wb") as file:
        file.write(dataB)
    sock = socket.socket()
    sock.connect(('localhost', 9090))
    f = open("clientMessageDB.cldt", "rb")
    l = f.read(1024)
    while (l):
        sock.send(l)
        l = f.read()
    f.close()
    result=sock.recv(1024)
    sock.close()
    return result




def sendMessage(message,fromHash,toHash,password,filePath):
    if '.' in filePath:
        with open(filePath,"rb") as file:
            fl=file.read()
    else:
        fl=None
    data={"type":"send","fromHash":fromHash,"toHash":toHash,"textMessage":message,"password":password,"fileB":fl}
    return sendDic(data)
def getMessages(hash,password):
    data={"type":"getMess","hash":hash,"password":password}
    return sendDic(data)
def checkHash(hash):
    data={"type":"checkHash","hash":hash}
    return sendDic(data)
def regUser(hash,password,name,lastName):
    data={"type":"regUser","hash":hash,"password":password,"name":name,"lastName":lastName}
    return sendDic(data)


import socket
regHash=input("hasTag: >>>")
regPass=input("password: >>>")
while True:
    text=input(">>>")
    if text=="send":
        text=input("Message: >>>")
        to=input("toHash: >>>")
        fileP=input("filePath: >>>")
        res1=sendMessage(text,regHash,to,regPass,fileP)
        print(res1)
    elif text=="getMessages":
        res1=getMessages(regHash,regPass)
        print(res1)
    elif text=="regUser":
        hs=input("hash: >>>")
        ps=input("password: >>>")
        nm=input("name: >>>")
        ls=input("lastName: >>>")
        res1=regUser(hs,ps,nm,ls)
        print(res1)