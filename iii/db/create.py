import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE users (uname text, pwdhash text)')
    conn.commit()
    conn.close()
