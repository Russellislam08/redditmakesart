''' Flask App to communicate with RDS and fetch scraped images from reddit '''
import argparse
import os

from dal import get_images, get_offset_images
from flask import Flask, jsonify, request
from pprint import pprint

app = Flask(__name__)

@app.route("/top10")
def hello():
    return jsonify(get_images())

@app.route("/images")
def img():
    offset = int(request.args.get('offset'))
    return jsonify(get_offset_images(offset))

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', help="Enable debug mode",
                        action='store_true')
    args = parser.parse_args()

    app.run(debug=args.debug)  # Run App
