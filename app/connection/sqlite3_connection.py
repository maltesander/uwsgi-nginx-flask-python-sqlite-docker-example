import sqlite3


class Sqlite3Connection:
    """
    Sqlite3 wrapper class to open, close and access the connection
    """
    path = None
    conn = None

    def __init__(self, path):
        self.path = path

    def open(self):
        if self.conn is None:
            try:
                self.conn = sqlite3.connect(self.path)
            except sqlite3.Error as e:
                print(e)

    def close(self):
        if self.conn is not None:
            self.conn.close()

    def get(self, query):
        if self.conn is None:
            self.open()

        try:
            cur = self.conn.cursor()
            cur.execute(query)
            result = cur.fetchall()
        except sqlite3.Error as err:
            result = "Error - " + err.args[0]

        self.close()
        return result

    def put(self, query):
        if self.conn is None:
            self.open()

        try:
            cur = self.conn.cursor()
            cur.execute(query)
            row_count = cur.rowcount
            self.conn.commit()
            response = "Done - Rows affected: " + str(row_count)
        except sqlite3.Error as err:
            response = "Error - " + err.args[0]

        self.close()
        return response


def sqlite3_call(database, query):
    """
    Differentiate between SELECT and INSERT, UPDATE, DELETE
    (hack -> wont work with sub-selects in e.g. update)
    """
    if query == "" or query is None:
        return "Warning: Empty query string!"
    elif query and query.lower().find("select") >= 0:
        return database.get(query)
    else:
        return database.put(query)
