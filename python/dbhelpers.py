import sqlite3

INSERT_QUERY = """ INSERT INTO reddit_images (uuid, title, author, image_url, permalink,
                   score) VALUES (?, ?, ?, ?, ?, ?);
               """

def submit_posts(posts):
    conn = sqlite3.connect("reddit_images.db")
    cursor = conn.cursor()

    for post in posts:
        cursor.execute(INSERT_QUERY, tuple(post))
        conn.commit()
    
    conn.close()
