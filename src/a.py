import sqlite3
import time

if __name__ == "__main__":
    print("a.py starting up")
    version = 0
    con = sqlite3.connect("data/db.sqlite3")
    con.execute("DROP TABLE IF EXISTS deployment_meta")
    con.executescript(
        """
        CREATE TABLE deployment_meta 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT, 
                status TEXT,
                updated_at INTEGER,
                version INTEGER
            );
        CREATE INDEX deployment_meta_name ON deployment_meta (name);
        CREATE INDEX deployment_meta_status ON deployment_meta (status);
        CREATE INDEX deployment_meta_updated_at ON deployment_meta (updated_at);
        CREATE INDEX deployment_meta_version ON deployment_meta (version);
        """,
    )
    con.execute(
        "INSERT INTO deployment_meta (name, status, updated_at, version) VALUES (?, ?, ?, ?)",
        ("a.py", "pending", time.time(), version),
    )
    time.sleep(5)

    con.execute(
        "INSERT INTO deployment_meta (name, status, updated_at, version) VALUES (?, ?, ?, ?)",
        ("a.py", "success", time.time(), version),
    )

    con.commit()

    print("a.py shutting down")
