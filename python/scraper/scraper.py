''' 
Scraper which uses PRAW to retrieve posts from the r/art
subreddit and submit it to speciifed database
'''
import os
import re
import sys

import praw

from dal import submit_to_rds
from collections import namedtuple
from pprint import pprint

# Some globals
POSTS = list()
REDDIT_STR = "https://www.reddit.com"
IMAGE = namedtuple('Image', ['id', 'title', 'author', 'image_url', 'permalink', 'score'])

def make_submission_obj(submission):
    ''' returns namedtuple of submission '''
    return IMAGE(submission.id, submission.title, submission.author.name,
                 submission.url, REDDIT_STR + submission.permalink,
                 submission.score)
    # Bottom code is here for reference
    # return {
    #         "uuid": submission.id,
    #         "title": submission.title,
    #         "author": submission.author.name,
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

def main(*args):
    try:
        client = praw.Reddit(client_id=os.environ['CLIENT_ID'],
                             client_secret=os.environ['CLIENT_SECRET'],
                             user_agent='reddit_app')
    except KeyError as e:
        print("Missing environment variable for reddit authentication: ", e)
        print("Terminating...")
        sys.exit(1)

    for submission in client.subreddit('art').top('day', limit=100):
        try:
            if (filter_submission(submission.title) and filter_url(submission.url) and not submission.over_18):
                POSTS.append(make_submission_obj(submission))
        except KeyError:
            print("Skipping post with id: {}".format(submission.id))
        except IndexError as e:
            print("An error occured while indexing a field within the post with this URL:  ", str(submission.url), e)
        except Exception as e:
            print("An unhandled exception has occured: ", e)
    
    submit_to_rds(POSTS)  # Submit all scraped images to AWS RDS
