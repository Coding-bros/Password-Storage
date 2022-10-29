import sqlite3
import random
from traceback import print_tb
from cryptography.fernet import Fernet

# Connect to The Database
conn = sqlite3.connect("PasswordStorage.db")

# Create the Cursor
c = conn.cursor()

key = Fernet.generate_key()
encrypter = Fernet('a3bpzn0WdTjj0JUClTeuo8logNYoQM6mKluczRuzTQw=')
# encrypter = Fernet(key)


'a3bpzn0WdTjj0JUClTeuo8logNYoQM6mKluczRuzTQw='

def encryptText(text):
    pw = encrypter.encrypt(text.encode())
    return pw


def decryptText(text):
  return encrypter.decrypt(text).decode()


# a3bpzn0WdTjj0JUClTeuo8logNYoQM6mKluczRuzTQw=



if __name__=="__main__":
    y = input()
    z = bytes(y, 'utf-8')
    print(z, encrypter.decrypt(z).decode())

conn.close()
