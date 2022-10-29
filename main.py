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
        print("Here is Your Passoword " + "\033[1;32;1m" + password)
        return password


def enterPassword():
    global password
    password = input("Enter Your Password : ")


def add_email():
    global password_final
    global name, websiteName, password
    name = input("\033[1;33;1m" + "Your Username: ")
    websiteName = input("\033[1;36;1m" + "WebsiteName: ")
    RandomOrUsual = int(input(
        "\033[1;31;1m" + "Would You like to use Your Password or A Randomly Generated Password (1 / 2) : "))
    if RandomOrUsual == 1:
        enterPassword()
    if RandomOrUsual == 2:
        randomPassword()
    password = str(input("\033[1;36;1m" + "Please retype your Password: "))
    EncOrUsual = int(input("\033[1;32;1m" + "Should the Password be Usual Or " +
                     "\033[1;31;1m" + "Encrypted (Use if Smtn Important) (1 / 2) : "))
    if EncOrUsual == 1:
        if password == password:
            Stored = [(name), (websiteName), (password)]
            c.executemany("INSERT INTO passwords VALUES (?,?,?)", (Stored,))
    if EncOrUsual == 2:
        if password == password:
            NoobText = password
            pw = f"{f.encryptText(NoobText)}"
            password = pw
            Stored = [(name), (websiteName), (pw)]
            c.executemany("INSERT INTO passwords VALUES (?,?,?)", (Stored,))
        else:
            print("\033[1;31;1m" + "KAL AANA KAL")

    # Commit
    conn.commit()


def read_email():
    c.execute("SELECT rowid, * FROM passwords")

    items = c.fetchall()

    for item in items:
        print("\033[1;36;1m")
        print(item)


def Main():
    usrinp = int(
        input("\033[1;35;1m" + "Do You Want to Add A New Password Or View The Passwords (1 / 2): "))
    if usrinp == 1:
        add_email()
    elif usrinp == 2:
        read_email()


if __name__ == "__main__":
    Main()

conn.close()
