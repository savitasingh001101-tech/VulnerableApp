import os
import subprocess
import hashlib
import sqlite3

password = "123456"

user_input = input("Enter command: ")

subprocess.call(user_input, shell=True)

query = "SELECT * FROM users WHERE name = '" + user_input + "'"

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute(query)

hashed = hashlib.md5(password.encode()).hexdigest()

os.system(user_input)

print(hashed)
