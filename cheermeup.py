#! /usr/local/bin/python3.4
import random
import webbrowser
from argparse import ArgumentParser
from os import environ
import sqlite3


conn = sqlite3.connect('funny.db')
c = conn.cursor()

def get_funny():
    videos = c.execute("Select * from videos").fetchall()
    return random.choice(videos)


def add(title, url):
   c.execute("INSERT INTO videos values(?,?)", (title, url))


if __name__ == "__main__":
    parser = ArgumentParser()
    group = parser.add_subparsers(dest='add')
    # get = group.add_parser('get')
    add_command = group.add_parser('add')
    add_command.add_argument('-t')
    add_command.add_argument('-u')
    args = parser.parse_args()
    if args.add:
        import IPython; IPython.embed()
    else:
        cheerup = get_funny()
        print(cheerup[0])
        webbrowser.open(cheerup[1])
