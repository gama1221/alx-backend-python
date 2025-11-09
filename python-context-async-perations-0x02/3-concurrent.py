#!/usr/bin/python3
import asyncio
import aiosqlite

DB_FILE = "users.db"

async def async_fetch_users():
    """Fetch all users asynchronously."""
    async with aiosqlite.connect(DB_FILE) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM users") as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]

async def async_fetch_older_users():
    """Fetch users older than 40 asynchronously."""
    async with aiosqlite.connect(DB_FILE) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]

async def fetch_concurrently():
    """Run both queries concurrently."""
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    print("All users:")
    for user in all_users:
        print(user)

    print("\nUsers older than 40:")
    for user in older_users:
        print(user)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
