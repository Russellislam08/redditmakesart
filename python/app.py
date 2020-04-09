import sqlite3

from flask import Flask, jsonify

app = Flask(__name__)

SELECT_QUERY = """ SELECT title, author, image_url, permalink, score FROM reddit_images
                   ORDER BY Timestamp DESC LIMIT 10;
               """
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

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

if __name__ == '__main__':
    app.run()
