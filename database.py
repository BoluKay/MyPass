import sqlite3

def create_db():
    connection = sqlite3.connect('mypass.db')
    cursor = connection.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            security_questions TEXT NOT NULL
        )
    ''')

    # Create vault table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vault (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    connection.commit()
    connection.close()

create_db()
print("Database and tables created successfully!")
