#!/usr/bin/python

from datetime import date
import sqlite3

## Connector SQL
def connector():
    conn = sqlite3.connect('test.db')
    return conn

## Create Table
def createTable(conn):
    db = conn
    print("Opened database successfully")

    db.execute('''CREATE TABLE IF NOT EXISTS auth
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            NAME           TEXT    NOT NULL,
            NationalCode   TEXT    NOT NULL,
            WithPicture    INTEGER NOT NULL,
            WithFinger     INTEGER NOT NULL,
            isRead         INTEGER NOT NULL,
            Date           TIMESTAMP NOT NULL,
            Time           TIMESTAMP NOT NULL,
            RegisteredFinger INTEGER NOT NULL,
            RegisteredFace   INTEGER NOT NULL);''')

    print("Table created successfully")

    db.close()

## Insert Function
def insertData(conn, Name, NatiCode, WithPic, WithFin, Date, Time, RegFin, RegFac):
    cursor = conn.cursor()
    print("Successfully Connected to SQLite")

    cursor.execute("""INSERT INTO auth 
                            (NAME, NationalCode, WithPicture, WithFinger, 
                            isRead, Date, Time, RegisteredFinger, RegisteredFace)
                            VALUES
                            (?, ?, ?, ?, ?, ?, ?, ?, ?) """, (Name, NatiCode, WithPic, WithFin, 0, Date, Time, RegFin, RegFac))
    conn.commit()
    cursor.close()

## Select Function
def selectAll(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM auth")
    rows = cursor.fetchall()
    cursor.close()
    return rows


## Update Functions
def updateWithPic(conn, Val, NatiCode):
    cursor = conn.cursor()
    cursor.execute("""UPDATE auth SET WithPicture = ? WHERE NationalCode = ?""", (Val, NatiCode))
    conn.commit()
    cursor.close()

def updateWithFin(conn, Val, NatiCode):
    cursor = conn.cursor()
    cursor.execute("""UPDATE auth SET WithFinger = ? WHERE NationalCode = ?""", (Val, NatiCode))
    conn.commit()
    cursor.close()

def updateIsRead(conn, Val, NatiCode):
    cursor = conn.cursor()
    cursor.execute("""UPDATE auth SET isRead = ? WHERE NationalCode = ?""", (Val, NatiCode))
    conn.commit()
    cursor.close()

def updateRegFace(conn, Val, NatiCode):
    cursor = conn.cursor()
    cursor.execute("""UPDATE auth SET RegisteredFace = ? WHERE NationalCode = ?""", (Val, NatiCode))
    conn.commit()
    cursor.close()

def updateRegFin(conn, Val, NatiCode):
    cursor = conn.cursor()
    cursor.execute("""UPDATE auth SET RegisteredFinger = ? WHERE NationalCode = ?""", (Val, NatiCode))
    conn.commit()
    cursor.close()


# if __name__ == "__main__":
    # import datetime
# 
    # conn = connector()
    # createTable(conn)
    insertData/(conn, "Salar", "0770222005", 0, 0,datetime.datetime.today().strftime("%Y-%m-%d"), datetime.datetime.now().strftime("%H:%M:%S"), 1, 1)