import sqlite3

DB_PATH = "macro.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            series_id TEXT NOT NULL,
            date      TEXT NOT NULL,
            value     REAL NOT NULL,
            PRIMARY KEY (series_id, date)
        )
    """)
    conn.commit()
    conn.close()

def save_observations(series_id, rows):
    conn = get_connection()
    conn.executemany(
        """
        INSERT INTO observations (series_id, date, value)
        VALUES (?, ?, ?)
        ON CONFLICT (series_id, date) DO UPDATE SET value = excluded.value
        """,
        [(series_id, date, value) for date, value in rows],
    )
    conn.commit()
    conn.close()
    return len(rows)


if __name__ == "__main__":
    init_db()
    print("Database ready.")
