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

    @staticmethod
    def safe_string(s):
        return s

    def write_to_db(self, row):
        execution_string = "INSERT OR REPLACE INTO reservations VALUES ("
        execution_string += "'" + self.safe_string(row[0]) + "', "
        execution_string += "'" + self.safe_string(row[1]) + "', "
        execution_string += "'" + self.safe_string(row[2]) + "', "
        execution_string += "'" + self.safe_string(row[3]) + "', "
        execution_string += "'" + self.safe_string(row[4]) + "', "
        execution_string += "'" + self.safe_string(row[5]) + "')"
        try:
            exec_st = execution_string.encode("utf-8")
            self.c.execute(exec_st.decode("utf-8"))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            print(execution_string)
            raise e

    def update_db(self):
        pass

    def delete_from_db(self):
        pass
