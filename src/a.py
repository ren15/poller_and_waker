import sqlite3
import time

if __name__ == "__main__":
    print("a.py starting up")
    con = sqlite3.connect("data/db.sqlite3")
    con.execute("DROP TABLE IF EXISTS deployment_meta")
    con.executescript(
        """
        CREATE TABLE deployment_meta 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT, 
                status TEXT,
                updated_at INTEGER
            );
        CREATE INDEX deployment_meta_name ON deployment_meta (name);
        CREATE INDEX deployment_meta_status ON deployment_meta (status);
        CREATE INDEX deployment_meta_updated_at ON deployment_meta (updated_at);
        """,
    )
    con.execute(
        "INSERT INTO deployment_meta (name, status, updated_at) VALUES (?, ?, ?)",
        ("a.py", "pending", time.time()),
    )
    time.sleep(5)

    con.execute(
        "INSERT INTO deployment_meta (name, status, updated_at) VALUES (?, ?, ?)",
        ("a.py", "ready", time.time()),
    )

    con.commit()

    print("a.py shutting down")
