import sqlite3
import os


class DbUtil():

    def __init__(self, db_file):
        self.db_path = db_file
        self.conn = self.create_connection()
        self.c = self.create_cursor()

    def create_connection(self):
        try:
            os.remove(self.db_path)
            print("removing existing db file")
        except OSError as e:
            print(e)
            print("Db file doesn't exist, creating it...")
        conn = sqlite3.connect(self.db_path)
        return conn

    def create_cursor(self):
        return self.conn.cursor()
