import sqlite3

# Conn
conn = sqlite3.connect("PasswordStorage.db")

# Create the Cursor
c = conn.cursor()

c.execute("""CREATE TABLE passwords (
username text,
website text,
password text
)""")

# Commit
conn.commit()

# Close the Conn

conn.close()