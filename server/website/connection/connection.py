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
    cur.execute("SELECT * FROM dashboard_space")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def check_full(conn,Lot):
    cur = conn.cursor()
    #find number of spaces currently occupied in given lot
    cur.execute("SELECT * FROM dashboard_space WHERE Lot=?",(Lot,))
    num_spaces_occupied = len(cur.fetchall())
    #find total number of spaces in given lot
    cur.execute("SELECT * FROM dashboard_lotsize WHERE name=?",(Lot,))
    num_avail_spaces_list = cur.fetchone()
    num_avail_spaces = num_avail_spaces_list[2]
    print("Total number of spaces in",Lot,"is",num_avail_spaces)
    print("Number of occupied spaces in",Lot,"is",num_spaces_occupied)
    #check if lot is full
    if num_spaces_occupied >= num_avail_spaces:
        print("Lot is full")
        return 1
    else:
        return 0

def insert_RFID(conn,Lot,Username):
    cur = conn.cursor()
    cur.execute("INSERT INTO dashboard_space (Lot,Username) VALUES (?,?)",(Lot,Username,))
    conn.commit()
    return check_full(conn,Lot)

def delete_RFID(conn,Lot,Username):
    cur = conn.cursor()
    if Username == "000000000000000000000000":
        cur.execute("DELETE FROM dashboard_space WHERE rowid = (SELECT rowid FROM dashboard_space WHERE Username=? LIMIT 1)",(Username,))
    else:
        cur.execute("DELETE FROM dashboard_space WHERE Username=?",(Username,))
    conn.commit()
    return check_full(conn,Lot)

# conn = create_connection("../db.sqlite3")
# select_all_tasks(conn)
# insert_RFID(conn,'')
# delete_RFID(conn,'')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#print(BASE_DIR)
db_path = os.path.join(BASE_DIR, "../db.sqlite3")

#functions to update database
def updateDatabase(InorOut, Lot, RFID):
        full = 0
        db_conn = create_connection(db_path)
        cur=db_conn.cursor()
        #print("HERE", RFID)
        if RFID != "000000000000000000000000":
            cur.execute("SELECT * FROM dashboard_rfid WHERE RFID=?",(RFID,))
            Username_list = cur.fetchone()
            #print("Here2", Username_list)
            Username = Username_list[2]
        else:
             Username = "000000000000000000000000"
        if(InorOut == 0):
            full = remove_car(Lot,Username,db_conn)
        elif(InorOut == 1):
            full = add_car(Lot,Username,db_conn)
        else:
             print(InorOut + ": not a valid entrance or exit int")
        return full

def remove_car(Lot,Username,DB_Conn):
        full = 0
        if(Username == '11111111'):
            print("CUID not unpacked")
        else:
            #sql call to remove correspoding ID from the database
            print("deleting")
            full = delete_RFID(DB_Conn,Lot,Username)
        return full

def add_car(Lot,Username,DB_Conn):
        full = 0
        if(Username == '11111111'):
            print("CUID not unpacked")
        else:
            #sql call to add corresponding ID from Database
            print("inserting")
            full = insert_RFID(DB_Conn,Lot,Username)
        return full
