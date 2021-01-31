import sqlite3
import random

# Connect to The Database
conn = sqlite3.connect("MyDatabase.db")

# Create the Cursor
c = conn.cursor()

def add_email():
    name = input("\033[1;31;1m" + "Your Username: ")
    websiteName = input("\033[1;36;1m" + "Your Email: ")
    randomPassword = randomPassword
    Stored = [(name, websiteName, randomPassword)]

    c.executemany("INSERT INTO emails VALUES (?,?,?)", Stored)

    # Commit 
    conn.commit()

conn.close()