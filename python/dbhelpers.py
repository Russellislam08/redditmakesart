import os
from pprint import pprint
import sqlite3

import boto3
import pymysql

# INSERT_QUERY = """ INSERT OR IGNORE INTO testing_table (uuid, title, author, image_url, permalink,
#                    score) VALUES (?, ?, ?, ?, ?, ?);
#                """

INSERT_QUERY = """ INSERT IGNORE INTO testing_table (uuid, title, author, image_url, permalink,
                   score) VALUES (%s, %s, %s, %s, %s, %s);
               """

def submit_posts(posts):
    conn = sqlite3.connect("reddit_images.db")
    cursor = conn.cursor()

    for post in posts:
        pprint(post)
        cursor.execute(INSERT_QUERY, tuple(post))
        conn.commit()
    
    conn.close()



def submit_to_dynamo(posts):
    dynamo = boto3.resource('dynamodb')
    print("dynamo client has been initialized")
    images_table = dynamo.Table('test')
    print("dynamo TABLE has been initialized")

    with images_table.batch_writer() as batch:
        for post in posts:
            batch.put_item(Item=post)
            # batch.put_item(Item={"uuid": post.uuid

    pass

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
        print(c.execute(INSERT_QUERY, tuple(post)))
        conn.commit()

    conn.close()
