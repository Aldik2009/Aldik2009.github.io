import sqlite3

def create():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS names (name VARCHAR)''')
    conn.commit()
    cursor.close()
    conn.close()

def clear_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS names''')
    conn.commit()
    cursor.close()
    conn.close()

def insert_db(name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO names (name) VALUES (?)''', [name])
    conn.commit()
    cursor.close()
    conn.close()