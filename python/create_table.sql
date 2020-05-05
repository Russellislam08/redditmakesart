CREATE TABLE reddit_images (
  uuid TEXT UNIQUE PRIMARY KEY,
  title TEXT,
  author TEXT,
  image_url TEXT,
  permalink TEXT,
  score integer,
  Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
  );



INSERT INTO test2 (uuid, title, author, image_url, permalink, score)
VALUES ("asjdas23", "test_title", "test_author", "https://www.somewhere.png", "https://www.somewhere.com", 100);


CREATE TABLE testing_table (
  uuid TEXT UNIQUE,
  title TEXT,
  author TEXT,
  image_url TEXT,
  permalink TEXT,
  score integer,
  Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
  );


CREATE TABLE testing_table (
  uuid VARCHAR(30) UNIQUE PRIMARY KEY,
  title VARCHAR(255),
  author VARCHAR(50),
  image_url VARCHAR(255),
  permalink VARCHAR(255),
  score MEDIUMINT,
  Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
  );

