import random
import sqlite3

from datetime import date, timedelta

TODAY = date.today()


def create_tables(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    price INTEGER NOT NULL
    );""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS purchase (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN KEY (item_id) REFERENCES item (id)
    );""")


def fill_random_values(connection, cursor):
    for i in range(1, 5001):
        random_age = random.randint(10, 80)
        cursor.execute("""
        INSERT INTO user (age) VALUES (?)
        """, (random_age, ))
        random_price = random.randint(500, 10000)
        cursor.execute("""
        INSERT INTO item (price) VALUES (?)
        """, (random_price, ))
        random_date = str(TODAY - timedelta(random.randint(0, 1500)))
        random_user_id = random.randint(1, i)
        random_item_id = random.randint(1, i)
        cursor.execute("""
        INSERT INTO purchase (user_id, item_id, date) VALUES (?, ?, ?)
        """, (random_user_id, random_item_id, random_date))
        if not i % 1000:
            connection.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('/tmp/wib.sqlite3')
    curr = conn.cursor()
    create_tables(cursor=curr)
    fill_random_values(connection=conn, cursor=curr)
    conn.close()
