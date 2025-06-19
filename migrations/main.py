from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import psycopg2
import os

MIGRATIONS_PATH = os.path.join(os.path.dirname(__file__), "files")

def get_applied_migrations(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS migrations (
                id SERIAL PRIMARY KEY,
                filename VARCHAR(255) UNIQUE NOT NULL,
                run_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

        cursor.execute("SELECT filename FROM migrations")
        return {row['filename'] for row in cursor.fetchall()}

def apply_migration(conn, filename):
    with open(os.path.join(MIGRATIONS_PATH, filename), "r") as f:
        sql = f.read()
    with conn.cursor() as cursor:
        cursor.execute(sql)
        cursor.execute("INSERT INTO migrations (filename) VALUES (%s)", (filename,))
    conn.commit()
    print(f"Applied migration {filename}")

def main():
    load_dotenv()

    conn = psycopg2.connect(
        host = os.getenv("DB_HOST", "localhost"),
        database = os.getenv("DB_NAME", "kyberfin"),
        user = os.getenv("DB_USER", "postgres"),
        password = os.getenv("DB_PASSWORD", "password"),
        cursor_factory = RealDictCursor,
        client_encoding = 'utf8'
    )

    applied = get_applied_migrations(conn)
    files = sorted(f for f in os.listdir(MIGRATIONS_PATH) if f.endswith(".sql"))

    migrations_applied = False
    for f in files:
        if f not in applied:
            apply_migration(conn, f)
            migrations_applied = True

    if not migrations_applied:
        print("No migrations to apply")

    conn.close()

if __name__ == "__main__":
    main()
