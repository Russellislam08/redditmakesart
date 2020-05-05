import pymysql
import os

from pprint import pprint

conn = pymysql.connect(os.environ['DB_ENDPOINT'], user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'],
                       db='test_db')

c = conn.cursor()

# c.execute(""" INSERT INTO testing_table (uuid, title, author, image_url, permalink,
#               score) VALUES (?, ?, ?, ?, ?, ?);
#           """)



c.execute("SELECT * FROM testing_table;")

pprint(c.fetchall())
