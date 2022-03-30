# For convenience sake we won't use SQLAlchemy, but instead use sqlite
import sqlite3
from datetime import datetime

def init():
    db = sqlite3.connect('data.db')
    
    # Create table to store comments in
    db.cursor().execute('CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY, comment TEXT, date TEXT)')

    return db

def add(comment):
    db = init()
    db.cursor().execute('INSERT INTO comments (comment, date) VALUES (?, ?)', (comment, datetime.utcnow().strftime('%B %d %Y - %H:%M')))

    db.commit()

def get(query=None):
    db = init()
    results = []
    
    for(comment, date) in db.cursor().execute('SELECT comment, date FROM comments').fetchall():
        if query is None or query in comment:
            results.append((comment, date))

    return results