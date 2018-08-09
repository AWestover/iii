import sqlite3
import hashlib


# user database 
def createUserTable():
    conn = sqlite3.connect('../users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE users (uname text, pwdhash text, group1 text, group2 text, group3 text, group4 text)')
    conn.commit()
    conn.close()

def insertUser(unm, pwd):
    pwdhash = hashlib.sha256(str.encode(pwd)).hexdigest()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()    
    c.execute('SELECT * FROM users WHERE uname=?', (unm,))
    if len(c.fetchall()) == 0:
        c.execute('INSERT INTO users VALUES (?,?,?,?,?,?)', (unm, pwdhash, '', '', '', ''))
        conn.commit()
        conn.close()
        return True 
    else:
        conn.close()
    return False

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


# annoyance database 
def createAnnoyanceTable():
    conn = sqlite3.connect('../annoyances.db')
    c = conn.cursor()
    c.execute('CREATE TABLE annoyances (logtime text, thegroup text, thetype text, description text, user text)')
    conn.commit()
    conn.close()

def insertAnnoyance(annoyance):
    conn = sqlite3.connect('annoyances.db')
    c = conn.cursor()
    c.execute('INSERT INTO annoyances VALUES (?,?,?,?,?)', (
                annoyance["logtime"], annoyance["thegroup"], annoyance["thetype"], annoyance["description"], annoyance["user"]
            ))
    conn.commit()
    conn.close()

def selectAnnoyances(group):
    conn = sqlite3.connect('annoyances.db')
    c = conn.cursor()
    c.execute('SELECT * FROM annoyances WHERE thegroup=?', (group,))
    annoyances = c.fetchall()
    conn.close()
    return annoyances
    

# group database
def createGroupsTable():
    conn = sqlite3.connect('../groups.db')
    c = conn.cursor()
    c.execute('CREATE TABLE groups (creator text, thegroup text, pwdhash text)')
    conn.commit()
    conn.close()
    
def insertGroup(creator, thegroup, pwd):
    pwdhash = hashlib.sha256(str.encode(pwd)).hexdigest()
    conn = sqlite3.connect('groupss.db')
    c = conn.cursor()
    c.execute('SELECT * FROM groups WHERE thegroup=?', (thegroup,))
    if len(c.fetchall()) == 0:
        c.execute('INSERT INTO groups VALUES (?,?,?)', (creator, thegroup, pwdhash))
        conn.commit()
        conn.close()
        return True 
    else:
        conn.close()
    return False


# if __name__ == "__main__":
#     createUserTable()
#     createGroupsTable()
#     createAnnoyanceTable()
