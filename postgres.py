import asyncio
import asyncpg
import json
import os


class JSONPostGresData(object):
    def __init__(self):
        db_file = open(os.environ["DB_SECRET"], "r+")
        data = json.load(db_file)
        self.query = data.pop("query")
        self.db = data

    # async def _init(self):
    #     self.pool = await create_pool()

    async def connect(self):
        try:
            self.conn = await asyncpg.connect(**self.db)
            print(self.conn)
        except Exception as error:
            await conn.close()

    async def get_items(self, query):
        all_items = await self.conn.fetch(query)
        return all_items


selection = input("Write new query or from db file (new, db): ")


async def main(query):
    c = JSONPostGresData()
    # c = await connect_db()
    await c.connect()

    if c.conn is not None:
        if selection == "new":
            query = input("Write query here: ")
        elif selection == "db":
            query = c.query
        else:
            query = None

        if query:
            items = await c.get_items(query)
        else:
            print("Need to pass a query in.")
        for item in items:
            print(item[0])
    else:
        print("Error connecting")


loop = asyncio.get_event_loop()
loop.run_until_complete(main(selection))
