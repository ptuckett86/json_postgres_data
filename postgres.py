import psycopg2
import json
import os


class JSONPostGresData:
    def __init__(self):
        db_file = open(os.environ["DB_SECRET"], "r+")
        data = json.load(db_file)
        self.query = data.pop("query")
        self.db = data

    def connect(self):
        try:
            self.conn = psycopg2.connect(**self.db).cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            self.conn = None
            print(error)

    def get_items(self, query):
        self.conn.execute(query)
        return self.conn.fetchall()


selection = input("Write new query or from db file (new, db): ")

c = JSONPostGresData()
c.connect()
if c.conn is not None:
    if selection == "new":
        query = input("Write query here: ")
    elif selection == "db":
        query = c.query
    else:
        query = None

    if query:
        items = c.get_items(query)
    else:
        print("Need to pass a query in.")
    for item in items:
        print(item[0])
else:
    print("Error connecting")
