# database setup placeholder
import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect('regalert.db')
cursor = conn.cursor()

# Create table for SEBI circulars
cursor.execute('''
CREATE TABLE IF NOT EXISTS circulars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    summary TEXT,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Create table for alerts
cursor.execute('''
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    circular_id INTEGER,
    alert_message TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (circular_id) REFERENCES circulars(id)
)
''')

# Create table for chatbot queries
cursor.execute('''
CREATE TABLE IF NOT EXISTS queries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    context TEXT,
    answer TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit and close connection
conn.commit()
conn.close()

print("Database setup completed successfully!")
