from collections import namedtuple
from os import environ
from pprint import pprint
import re
from sys import exit

import loguru
import praw

from dbhelpers import submit_posts, submit_to_dynamo, submit_to_rds

POSTS = list()
REDDIT_STR = "https://www.reddit.com"
IMAGE = namedtuple('Image', ['id', 'title', 'author', 'image_url', 'permalink', 'score'])

def make_submission_obj(submission):
    ''' returns namedtuple of submission '''
    return IMAGE(submission.id, submission.title, submission.author.name,
                 submission.url, REDDIT_STR + submission.permalink,
                 submission.score)
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
        client = praw.Reddit(client_id=environ['CLIENT_ID'],
                             client_secret=environ['CLIENT_SECRET'],
                             user_agent='reddit_app')
    except KeyError as e:
        print("Missing environment variable for reddit authentication: ", e)
        print("Terminating...")
        exit(1)

    for submission in client.subreddit('art').new(limit=100):
        try:
            if filter_submission(submission.title) and filter_url(submission.url):
                POSTS.append(make_submission_obj(submission))
        except KeyError:
            print("Skipping post with id: {}".format(submission.id))
        except IndexError as e:
            print("An error occured while indexing a field within the post with this URL:  ", str(submission.url), e)
        except Exception as e:
            print("An unhandled exception has occured: ", e)
    
    # submit_posts(POSTS)
    # submit_to_dynamo(POSTS)
    submit_to_rds(POSTS)


if __name__ == '__main__':
# 
    main()
    # try:
    #     client = praw.Reddit(client_id=environ['CLIENT_ID'],
    #                          client_secret=environ['CLIENT_SECRET'],
    #                          user_agent='reddit_app')
    # except KeyError as e:
    #     print("Missing environment variable for reddit authentication: ", e)
    #     print("Terminating...")
    #     exit(1)

    # for submission in client.subreddit('art').top(limit=100):
    #     try:
    #         if filter_submission(submission.title) and filter_url(submission.url):
    #             POSTS.append(make_submission_obj(submission))
    #     except KeyError:
    #         print("Skipping post with id: {}".format(submission.id))
    #     except IndexError as e:
    #         print("An error occured while indexing a field within the post with this URL:  ", str(submission.url), e)
    #     except Exception as e:
    #         print("An unhandled exception has occured: ", e)
    # 
    # # submit_posts(POSTS)
    # # submit_to_dynamo(POSTS)
    # submit_to_rds(POSTS)
