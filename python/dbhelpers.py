from pprint import pprint
import sqlite3

INSERT_QUERY = """ INSERT OR IGNORE INTO reddit_images (uuid, title, author, image_url, permalink,
                   score) VALUES (?, ?, ?, ?, ?, ?);
               """

def submit_posts(posts):
    conn = sqlite3.connect("reddit_images.db")
    cursor = conn.cursor()

    for post in posts:
        pprint(post)
        cursor.execute(INSERT_QUERY, tuple(post))
        conn.commit()
    
    conn.close()
