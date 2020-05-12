import os
import pymysql
from pprint import pprint

INSERT_QUERY = """ INSERT IGNORE INTO {}
                   (uuid, title, author, image_url, permalink, score)
                   VALUES (%s, %s, %s, %s, %s, %s);
               """

def submit_to_rds(posts):
    print("Attempting to connect to database...")
    conn = pymysql.connect(os.environ['DB_ENDPOINT'],
                           user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'],
                           db='test_db')
    print("Successfully connected to database")

    c = conn.cursor()
    print("Initialized connection and cursor")

    for post in posts:
        pprint(tuple(post))
        print(c.execute(INSERT_QUERY.format(os.environ['DB_TABLE']), tuple(post)))
        conn.commit()

    conn.close()
