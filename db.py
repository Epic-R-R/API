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
            NationalCode   INTEGER NOT NULL,
            WithPicture    INTEGER NOT NULL,
            WithFinger     INTEGER NOT NULL,
            isRead         INTEGER NOT NULL,
            Date           TIMESTAMP NOT NULL,
            Time           TIMESTAMP NOT NULL,
            RegisteredFinger INTEGER NOT NULL,
            RegisteredFace   INTEGER NOT NULL, 
            PositionNumber   INTEGER NULL);''')

    print("Table created successfully")

    db.close()

## Insert Function
def insertData(conn, Name, NatiCode, WithPic, WithFin, isread, Date, Time, RegFin, RegFac, posNumber):
    cursor = conn.cursor()
    print("Successfully Connected to SQLite")

    cursor.execute("""INSERT INTO auth 
                            (NAME, NationalCode, WithPicture, WithFinger, 
                            isRead, Date, Time, RegisteredFinger, RegisteredFace, PositionNumber)
                            VALUES
                            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """, (Name, NatiCode, WithPic, WithFin, isread, Date, Time, RegFin, RegFac, posNumber))
    conn.commit()
    cursor.close()

## Select Function
def selectAllisRead(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM auth WHERE isRead = 0")
    rows = cursor.fetchall()
    cursor.close()
    return rows

def selectAllDate(conn, date1, date2):
    cursor = conn.cursor()
    cursor.execute("select * from auth where Date >= ? and Date <= ?", (date1, date2))
    rows = cursor.fetchall()
    cursor.close()
    return rows

## Update Functions
def updateIsRead(conn, Val, NatiCode):
    cursor = conn.cursor()
    cursor.execute("""UPDATE auth SET isRead = ? WHERE NationalCode = ?""", (Val, NatiCode))
    conn.commit()
    cursor.close()

def updateRegFin(conn, Val, NatiCode):
    cursor = conn.cursor()
    cursor.execute("""UPDATE auth SET RegisteredFinger = ? WHERE NationalCode = ?""", (Val, NatiCode))
    conn.commit()
    cursor.close()

## Delete Row
def deleteRow(conn, NatiCode):
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM auth WHERE NationalCode = ?""", (NatiCode,))
    conn.commit()
    cursor.close()

## Delete All Records
def deleteAll(conn):
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM auth;""")
    conn.commit()
    cursor.close()

## Search function
def search(conn, NatiCode):
    cursor = conn.cursor()
    result = cursor.execute("""SELECT * FROM auth WHERE NationalCode = ?""", (NatiCode,))
    rows = result.fetchall()
    cursor.close()
    return rows

# if __name__ == "__main__":
#     import datetime

    # conn = connector()
    # createTable(conn)
    # insertData(conn, "Mehti", "0770222002", 0, 0,"2021-09-15", datetime.datetime.now().strftime("%H:%M:%S"), 1, 1)
    # print(selectAllDate(conn, "2021-09-10", "2021-09-12"))