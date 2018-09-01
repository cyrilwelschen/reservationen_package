import sqlite3
import os


class DbUtil:

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

    def create_table(self, creation_string):
        self.c.execute(creation_string)
        self.conn.commit()

    def execute_on_db(self, execution_string):
        try:
            # todo: check if encode/decode is really necessary?
            exec_st = execution_string.encode("utf-8")
            self.c.execute(exec_st.decode("utf-8"))
        except sqlite3.OperationalError as e:
            # todo: send mail notification
            print(exec_st)
            raise e

    def close_db(self):
        self.conn.close()
