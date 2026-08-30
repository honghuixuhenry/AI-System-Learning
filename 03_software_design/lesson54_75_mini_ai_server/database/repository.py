import sqlite3
from database.db import DATABASE_PATH

class ChatHistoryRepository:
    def save(
            self,
            prompt: str,
            response: str
    ):
        conn = sqlite3.connect(
            DATABASE_PATH
        )
        cursor = conn.cursor()
        cursor.execute(
            """

            INSERT INTO chat_history (

                prompt,

                response

            )

            VALUES (?, ?)

            """,
            (
                prompt,
                response
            )
        )
        conn.commit()
        conn.close()