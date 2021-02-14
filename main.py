import sqlite3
import random

# Connect to The Database
conn = sqlite3.connect("PasswordStorage.db")

# Create the Cursor
c = conn.cursor()

# 8 characters 1 uppercase 1 lowercase 1 Special Character 1 Number
def randomPassword():
    global password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    passwordlen = 8
    password_count = 1
    for x in range(0, password_count):
        password = ""
        for x in range(0, passwordlen):
            passwordChar = random.choice(characters)
            password = password + passwordChar
        print("\033[1;31;1m" +"Here is Your Passoword" + "\033[1;36;1m " + password)
        return password

def add_email():
    global password_final
    global name, websiteName, password
    name = input("\033[1;31;1m" + "Your Username: ")
    websiteName = input("\033[1;36;1m" + "WebsiteName: ")
    randomPassword()
    password = str(input("\033[1;36;1m" + "Please retype your Password: "))
    if password == password:
        Stored = [(name), (websiteName), (password)]
        c.executemany("INSERT INTO passwords VALUES (?,?,?)", (Stored,))
    
    # Commit 
    conn.commit()

def read_email():
    c.execute("SELECT rowid, * FROM passwords")

    items = c.fetchall()

    for item in items:
        print("\033[1;31;1m")
        print(item)


def Main():
    usrinp = int(input("\033[1;36;1m" + "Do You Want to Add A New Password Or View The Passwords (1 / 2): "))
    if usrinp == 1:
        add_email()
    elif usrinp == 2:
        read_email()

if __name__ == "__main__":
    Main()

conn.close()
