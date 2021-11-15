import sqlite3


class DBParser:
    def __init__(self, path_to_db):
        self.conn = sqlite3.connect(path_to_db)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.conn.close()

        del self.conn
        del self.cursor
