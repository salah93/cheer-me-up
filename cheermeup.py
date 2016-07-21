#! /usr/local/bin/python3.4
import random
import sqlite3
import webbrowser
from argparse import ArgumentParser
from os import environ, path


DB_FOLDER = environ['DB_FOLDER']
conn = sqlite3.connect(path.join(DB_FOLDER, 'funny.db'))
c = conn.cursor()


def get_funny():
    videos = c.execute("Select * from videos").fetchall()
    return random.choice(videos)


def add(title, url):
    c.execute("INSERT INTO videos values(?,?)", (title, url))


if __name__ == "__main__":
    parser = ArgumentParser()
    group = parser.add_subparsers(dest='add')
    add_command = group.add_parser('add')
    add_command.add_argument('-t', required=True)
    add_command.add_argument('-u', required=True)
    args = parser.parse_args()
    if args.add:
        add(args.t, args.u)
    else:
        cheerup = get_funny()
        print(cheerup[0])
        webbrowser.open(cheerup[1])
