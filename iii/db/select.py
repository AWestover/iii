import sqlite3
import hashlib

def selectAll():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    result = c.fetchall()
    conn.close()
    return result

def verifyUser(unm, pwd):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE uname=?', (unm,))
    usr = c.fetchone()
    realpwdhash = usr[1]
    legit = False
    if usr:
        if hashlib.sha256(str.encode(pwd)).hexdigest() == realpwdhash:
            legit = True
    conn.close()
    return legit

def selectUser(unm):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE uname=?', (unm,))
    result = c.fetchone()
    conn.close()
    return result
