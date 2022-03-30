# For convenience sake we won't use SQLAlchemy, but instead use sqlite
import sqlite3

def init():
    db = sqlite3.connect('data.db')
    
    # Create table to store comments in
    db.cursor().execute('CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY, comment TEXT)')

    return db

def add(comment):
    db = init()
    db.cursor().execute('INSERT INTO comments (comment) VALUES (?)', (comment,))

    db.commit()

def get(query=None):
    db = init()
    results = []
    
    for(comment,) in db.cursor().execute('SELECT comment FROM comments').fetchall():
        if query is None or query in comment:
            results.append(comment)

    return results