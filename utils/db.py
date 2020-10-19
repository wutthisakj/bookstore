import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import asyncio
from databases import Database

from utils.const import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

async def connect_db():
    db = Database(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
    await db.connect()
    return db

async def disconnect_db(db):
    await db.disconnect()

async def execute(query, is_many, values=None):
    db = await connect_db()

    if is_many:
        await db.execute_many(query=query, values=values)
    else:
        await db.execute(query=query, values=values)
    
    await disconnect_db(db)

async def fetch(query, is_one, values=None):
    db = await connect_db()
    if is_one:
        result = await db.fetch_one(query=query, values=values)
        out = dict(result)
    else:
        result = await db.fetch_all(query=query, values=values)
        out = []
        for row in result:
            out.append(dict(row))
    await disconnect_db(db)
    
    print(out)
    return out

#query = "insert into books values(:custom, :name, :author, :year)"
#values = [{"custom": "isbn2", "name": "book2", "author": "author2", "year": 2018},
#          {"custom": "isbn3", "name": "book3", "author": "author3", "year": 2020}]

#query = "select * from books where isbn=:isbn"
#values ={"isbn": "isbn2"}

query = "select * from books"

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch(query, False))