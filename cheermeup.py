#! /usr/local/bin/python
import pymongo
import random
import webbrowser


SERVER = 'ds025792.mlab.com'
PORT = 25792
DB_NAME = 'funny_videos'
USERNAME = 'guest'
PASSWORD = '123456'


def get_funny(mongodb):
    videos = list(mongodb.videos.find())
    return random.choice(videos)


if __name__ == "__main__":
    # connect to instance
    client = pymongo.MongoClient(host=SERVER, port=PORT)
    # connect to database
    db = client[DB_NAME]
    # sign in
    db.authenticate(USERNAME, password=PASSWORD)
    cheerup = get_funny(db)
    print(cheerup.get('title', "Nothing :("))
    webbrowser.open(cheerup.get("url",
                    "http://youtube.com/watch?v=dQw4w9WgXcQ"))
