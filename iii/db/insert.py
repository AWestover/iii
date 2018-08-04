import sqlite3
import hashlib

def insertUser(unm, pwd):
    pwdhash = hashlib.sha256(str.encode(pwd)).hexdigest()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users VALUES (?,?)', (unm, pwdhash))
    conn.commit()
    conn.close()

# if __name__ == "__main__":
    # insertUser('alek', 'alek')
