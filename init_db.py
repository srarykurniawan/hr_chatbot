import sqlite3

# Buat dan hubungkan ke database
conn = sqlite3.connect("hrchatbot.db")

# Buat tabel chatbot_logs
conn.execute("""
CREATE TABLE IF NOT EXISTS chatbot_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    response TEXT,
    category TEXT,
    timestamp DATETIME
)
""")

conn.commit()
conn.close()

print("Database dan tabel berhasil dibuat.")
