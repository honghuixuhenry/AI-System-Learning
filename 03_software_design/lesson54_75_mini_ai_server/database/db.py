import sqlite3

DATABASE_PATH = "data/ai_server.db"

def init_db():
    conn = sqlite3.connect(
        DATABASE_PATH
    )
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS chat_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            prompt TEXT NOT NULL,

            response TEXT NOT NULL

        )
        """
    )
    conn.commit()
    conn.close()