# echo-server.py

import socket
import struct
import sqlite3
from testConnection import *

#fucntons to update database
def updateDatabase(InorOut, ID):
        db_conn = create_connection("../db.sqlite3")
        if(InorOut == 0):
            remove_car(ID,db_conn)
        elif(InorOut == 1):
            add_car(ID,db_conn)
        else:
             print(InorOut + ": not a valid entrance or exit int")

def remove_car(ID,DB_Conn):
        if(ID == '11111111'):
            print("CUID not unpacked")
        else:
            print("sql call to remove car")
            #sql call to remove correspodign ID from the database
            #delete_RFID(DB_Conn,ID)

def add_car(ID,DB_Conn):
        if(ID == '11111111'):
            print("CUID not unpacked")
        else:
            print("sql call to add car")
            #sql call to add corresponding ID from Database
            #insert_RFID(DB_Conn,ID)

#db_conn = sqlite3.connect("db.sq")
IoO = 2
CUID = '11111111'

HOST = "169.254.185.103"  # This is the IP of the admin PC. This needs to be set statically
PORT = 5005  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket created at %s:%d" % (HOST, PORT))
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(9)
            if not data:
                continue
            else:
                print(struct.unpack('?8s',data))
                IoO = data[0]
                CUID = data[1]
                updateDatabase(IoO, CUID)

#conn.sendall(data)




