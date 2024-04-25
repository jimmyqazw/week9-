import sqlite3
from threading import Lock


class Connection:
    db_file_path = str()
    db_lock = Lock()

    def __init__(self):
        Connection.db_lock.acquire()
        self.connection = sqlite3.connect(self.db_file_path)
        self.connection.row_factory = sqlite3.Row

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        Connection.db_lock.release()
