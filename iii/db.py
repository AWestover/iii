import sqlite3
import hashlib

# users should also store what groups you are in

def createUserTable():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE users (uname text, pwdhash text)')
    conn.commit()
    conn.close()

def insertUser(unm, pwd):
    pwdhash = hashlib.sha256(str.encode(pwd)).hexdigest()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users VALUES (?,?)', (unm, pwdhash))
    conn.commit()
    conn.close()

def selectAllUsers():
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
    legit = False
    if usr:
        realpwdhash = usr[1]
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

def createAnnoyanceTable():
    conn = sqlite3.connect('annoyances.db')
    c = conn.cursor()
    c.execute('CREATE TABLE annoyances (stupid text, thegroup text)')
    conn.commit()
    conn.close()

def insertAnnoyance(annoyance):
    conn = sqlite3.connect('annoyances.db')
    c = conn.cursor()
    c.execute('INSERT INTO annoyances VALUES (?,?)', (annoyance["stupid"], annoyance["thegroup"]))
    conn.commit()
    conn.close()

def selectAnnoyances(group):
    conn = sqlite3.connect('annoyances.db')
    c = conn.cursor()
    c.execute('SELECT * FROM annoyances WHERE thegroup=?', (group,))
    annoyances = c.fetchall()
    conn.close()
    return annoyances
    
def createGroupsTable():
    conn = sqlite3.connect('annoyances.db')
    c = conn.cursor()
    c.execute('CREATE TABLE groups (groupid text)')
    conn.commit()
    conn.close()
    
