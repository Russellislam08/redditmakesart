import os
from pprint import pprint
import sqlite3

from flask import Flask, jsonify, request
import pymysql
import requests


app = Flask(__name__)

SELECT_QUERY = """ SELECT uuid, title, author, image_url, permalink, score FROM reddit_images
                   ORDER BY Timestamp DESC LIMIT 10;
               """

OFFSET_QUERY = """ 
                   SELECT uuid, title, author, image_url, permalink, score
                   FROM testing_table
                   ORDER BY Timestamp DESC
                   LIMIT 10
                   OFFSET %s;
               """

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def filter_posts(response):
    return [post for post in response if 
            requests.get(post['image_url']).status_code == 200]

def get_images():
    connection = sqlite3.connect('reddit_images.db')
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    cursor.execute(SELECT_QUERY)
    # pprint(cursor.fetchall())
    return cursor.fetchall()

@app.route("/top10")
def hello():
    return jsonify(get_images())

@app.route("/images")
def img():
    offset = int(request.args.get('offset'))
    # connection = sqlite3.connect('reddit_images.db')

    conn = pymysql.connect(os.environ['DB_ENDPOINT'],
                           user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'],
                           db='test_db')

    # conn.row_factory = dict_factory
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(cursor.mogrify(OFFSET_QUERY, (offset,)))
    cursor.execute(OFFSET_QUERY, (offset,))

    response = cursor.fetchall()
    pprint(response)
    # modified_response = filter_posts(response)
    # pprint(modified_response)


    return jsonify(response)
    

if __name__ == '__main__':
    app.run(debug=True)
