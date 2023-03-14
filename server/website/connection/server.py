# echo-server.py

import socket
import struct
import sqlite3
from testConnection import *
import os.path, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#print(BASE_DIR)
db_path = os.path.join(BASE_DIR, "../db.sqlite3")

#fucntons to update database
def updateDatabase(InorOut, ID):
        db_conn = create_connection(db_path)
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
            #sql call to remove correspoding ID from the database
            print("deleting")
            delete_RFID(DB_Conn,ID)

def add_car(ID,DB_Conn):
        if(ID == '11111111'):
            print("CUID not unpacked")
        else:
            #sql call to add corresponding ID from Database
            print("inserting")
            insert_RFID(DB_Conn,ID)

#db_conn = create_connection("../db.sqlite3")
IoO = 2
CUID = '11111111'

HOST = "169.254.185.103"  # This is the IP of the admin PC. This needs to be set statically
PORT = 5005  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket created at %s:%d" % (HOST, PORT))
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            print("p")
            data = conn.recv(9)
            print("p1")
            if data:
                print(struct.unpack('?8s',data))
                IoO = data[0]
                CUID = data[1]
                updateDatabase(IoO, CUID)

#conn.sendall(data)
