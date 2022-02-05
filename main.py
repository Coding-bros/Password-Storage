import sqlite3
import random
from cryptography.fernet import Fernet

# Connect to The Database
conn = sqlite3.connect("PasswordStorage.db")

# Create the Cursor
c = conn.cursor()

key = Fernet.generate_key()
encrypter = Fernet('a3bpzn0WdTjj0JUClTeuo8logNYoQM6mKluczRuzTQw=')


def encryptText(text):
    pw = encrypter.encrypt(text.encode())
    return pw


def decryptText(text):
    decryptString = encrypter.decrypt(text)
    return decryptString


# a3bpzn0WdTjj0JUClTeuo8logNYoQM6mKluczRuzTQw=

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
        print("Here is Your Passoword" + password)
        return password


def add_email():
    global password_final
    global name, websiteName, password
    name = input("Your Username: ")
    websiteName = input("WebsiteName: ")
    randomPassword()
    password = str(input("Please retype your Password: "))
    if password == password:
        NoobText = password
        pw = encryptText(NoobText)
        password = pw
        Stored = [(name), (websiteName), (pw)]
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
    usrinp = int(
        input("Do You Want to Add A New Password Or View The Passwords (1 / 2): "))
    if usrinp == 1:
        add_email()
    elif usrinp == 2:
        read_email()


if __name__ == "__main__":
    Main()

conn.close()
