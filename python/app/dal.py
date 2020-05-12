''' Database Abstraction Layer '''
import os

import pymysql
import requests

from pprint import pprint


SELECT_QUERY = """ SELECT uuid, title, author, image_url, permalink, score
                   FROM {}
                   ORDER BY Timestamp DESC
                   LIMIT 10;
               """

OFFSET_QUERY = """ 
                   SELECT uuid, title, author, image_url, permalink, score
                   FROM {}
                   ORDER BY Timestamp DESC
                   LIMIT 5
                   OFFSET %s;
               """

def establish_connection():
    return pymysql.connect(os.environ['DB_ENDPOINT'],
                           user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'],
                           db='test_db')

def verify_urls(urls):
    return [post for post in urls if 
            requests.get(post['image_url']).status_code == 200]

def get_images():
    connection = establish_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(SELECT_QUERY, (os.environ['DB_TABLE'],))
        response = cursor.fetchall()
        pprint(response)
        connection.close()
    except Exception as e:
        print("An unhandled exception has occured: ", e)
        return []
    else:
        return response

def get_offset_images(offset):
    connection = establish_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(OFFSET_QUERY.format(os.environ['DB_TABLE']), (offset,))
        response = cursor.fetchall()
        pprint(response)
        connection.close()
    except Exception as e:
        print("An unhandled exception has occured: ", e)
        return []
    else:
        return verify_urls(response)