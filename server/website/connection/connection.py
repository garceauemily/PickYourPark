import sqlite3
import os.path, os

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("connection made")
    except sqlite3.Error as e:
        print(e)

    return conn

def select_all_tasks(conn):
    """
    Query all rows in the auth_user table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM dashboard_rfid")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def insert_RFID(conn,RFID_str):
    cur = conn.cursor()
    cur.execute("INSERT INTO dashboard_rfid (Lot,RFID) VALUES ('C02',?)",(RFID_str,))
    conn.commit()

def delete_RFID(conn,RFID_str):
    cur = conn.cursor()
    if RFID_str == '00000000':
        cur.execute("DELETE FROM dashboard_rfid WHERE RFID=? LIMIT 1",(RFID_str,))
    else:
        cur.execute("DELETE FROM dashboard_rfid WHERE RFID=?",(RFID_str,))
    conn.commit()

# conn = create_connection("../db.sqlite3")
# select_all_tasks(conn)
# insert_RFID(conn,'')
# #delete_RFID(conn,'')

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
