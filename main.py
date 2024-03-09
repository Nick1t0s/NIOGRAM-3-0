import pickle

import SQLTOOLS,socket
sock=socket.socket()
SQLTOOLS.createUsers()
SQLTOOLS.createMessages()
sock = socket.socket()
sock.bind(('0.0.0.0', 9090))
sock.listen(1)
while True:
    dic,conn=SQLTOOLS.getBDict(sock)
    print("agsdds")
    print(dic)
#    dic=SQLTOOLS.readDtFromDict(res)
    if dic["type"] == "send":
        result=SQLTOOLS.insertMessToDB(dic["fromHash"],dic["toHash"],dic["textMessage"],dic["fileB"])
        conn.send(result)
        print("ok")
    elif dic["type"] == "checkHash":
        result=SQLTOOLS.chechHash(dic["type"]).encode()
        conn.send(result)
    elif dic["type"] == "getMess":
        result=SQLTOOLS.getMessages(dic["hash"])
        conn.send(result)
    elif dic["type"] == "regUser":
        result.regUser(dic["hash"],dic["name"],dic["lastName"],dic["password"])
        conn.send(result)


