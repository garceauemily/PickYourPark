import sqlite3

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
    cur.execute("DELETE FROM dashboard_rfid WHERE RFID=?",(RFID_str,))
    conn.commit()

#conn = create_connection("../db.sqlite3")
# select_all_tasks(conn,'')
# insert_RFID(conn,'')
# #delete_RFID(conn,'')
