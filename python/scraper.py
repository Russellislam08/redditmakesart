from collections import namedtuple
from pprint import pprint
import re

import loguru
import praw

from dbhelpers import submit_posts

POSTS = list()
REDDIT_STR = "https://www.reddit.com"
IMAGE = namedtuple('Image', ['id', 'title', 'author', 'image_url', 'permalink', 'score'])

def make_submission_obj(submission):
    ''' returns namedtuple of submission '''
    return IMAGE(submission.id, submission.title, submission.author.name,
                 submission.url, REDDIT_STR + submission.permalink,
                 submission.score)
    # return {
    #         "id": submission.id,
    #         "title": submission.title,
    #         "author": submission.author,
    #         "image_url": submission.url,
    #         "permalink": REDDIT_STR + submission.permalink,
    #         "score": submission.score
    #        }

def filter_submission(title):
    '''
    By reddit standards, the title will have the format:
    name, author, technique, date
    So we know that the second key will always be the author name
    If that evalutes to 'me', then it is original content
    '''
    author_name = title.split(',')[1].strip().lower()
    # return re.match('me', author_name, re.IGNORECASE)
    return author_name == 'me'

def filter_url(url):
    '''
    make sure that the image source is a .png or .jgp link
    If it's something on gfycat or imgur, ignore it
    Might add support for this later on
    '''
    string_to_match = "i.redd.it"
    return re.search(string_to_match, url)


if __name__ == '__main__':

    client = praw.Reddit(client_id='',
                         client_secret='',
                         user_agent='')

    for submission in client.subreddit('art').hot(limit=10):
        try:
            if filter_submission(submission.title) and filter_url(submission.url):
                POSTS.append(make_submission_obj(submission))
        except KeyError:
            print("Skipping post with id: {}".format(submission.id))
            continue
    
    submit_posts(POSTS)
