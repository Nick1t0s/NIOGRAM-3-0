import sqlite3 as sq
import pickle
from PIL import Image, ImageDraw, ImageFont


def createUsers():
    with sq.connect("USERS.db") as con:
        cur=con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
        hash TEXT PRIMARY KEY,
        name TEXT,
        lastName TEXT, 
        password TEXT, 
        photo BLOB, 
        tp TEXT )""")
#def createMessages():
#    with sq.connect("MESS.db") as con:
#        cur=con.cursor()
#        cur.execute("""CREATE TABLE IF NOT EXISTS messages (
#        FR TEXT,
#        TO TEXT,
#        PASSWORD TEXT,
#        MESS TEXT,
#        FL TEXT )""")

def createMessages():
    with sq.connect("MES.db") as con:
        cur=con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS messages (
        fromHash TEXT,
        toHash TEXT,
        textMessage TEXT,
        file BLOB,
        isRead INTAGER)""")
def readDtFromDict(dictB):
    dictNB=pickle.loads(dictB)
    return dictNB

def getBDict(sock):
    conn,addr=sock.accept()
    print("dn")
    f=open("clientDataFile.cldt","wb")
    while True:
        i = conn.recv(1024)
        f.write(i)
        if not i: break
    f.close()
    print("doneWrite")
    with open("clientDataFile.cldt","rb") as file:
        dictB = pickle.load(file)
    return dictB,conn

def insertMessToDB(fromHash,toHash,textMessage,fileB):
    with sq.connect("MES.db") as con:
        cur=con.cursor()
        vopr = """INSERT INTO messages (fromHash, toHash, textMessage, file, isRead) VALUES (?, ?, ?, ?, ?)"""
        data_tuple = (fromHash,toHash,textMessage,fileB,0)
        cur.execute(vopr, data_tuple)
    return "done".encode()
#    conn.send("done".encode())

def chechHash(hash):
    with sq.connect("MESS.db") as con:
        cur=con.cursor()
        cur.execute("""SELECT hash FROM users""")
    res=cur.fetchall()
    res2=bool(list(res[0]))
    print(res2)
    return str(res2).encode()
#    conn.send(str(res2).encode())


def getMessages(hash):
    with sq.connect("MESS.db") as con:
        cur=con.cursor()
        cur.execute("""SELECT textMessage, file FROM messages WHERE isRead = 0""")
    res=cur.fetchall()
    res2=[]
    for row in res:
        res2.append(list(row))
    rotated = list(zip(*res2[:]))
    print(rotated)
    return pickle.dumps(rotated)

def regUser(hash,name,lastName,password):
    photo=createPhotoForUser(name,lastName)
    comand="INSERT INTO users (hash, name, lastName, password, photo, type) VALUES(?,?,?,?,?,?)"
    data=(hash,name,lastName,password,photo,"basik")
    with sq.connect("users.db") as con:
        cur=con.cursor()
        cur.execute(comand,data)
    return "done".encode()

def createPhotoForUser(name,lastName):
    rgb = (0, 128, 128)  # переменная цвета)
    rgb2 = (rgb[0] + 45, rgb[1] + 45, rgb[2] + 45)
    back = Image.new("RGB", (500, 500), rgb)  # объект картинки
    font = ImageFont.truetype("arial.ttf", 300)  # импорт шрифта
    drawer = ImageDraw.Draw(back)  # объект класса рисователя
    drawer.text((50, 80), name[0] + lastName[0], font=font, fill=rgb2)  # накладываем текст на картинку
    back.save("foto.png")  # сохраняе
    with open("foto.png","rb") as file:
         photo = file.read()
    return photo

