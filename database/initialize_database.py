#!/usr/bin/env python

import json
import sqlite3
from sqlite3 import Error
from queries import *

PATH_TO_DB_FILE = "../HTN_2023_BE_Challenge_Data.json"

def insert_hackers_data(cursor):
    f = open(PATH_TO_DB_FILE)
    hackersInfo = json.load(f)
    for hacker in hackersInfo:
        hackerData = (hacker['name'], hacker['company'], hacker['email'], hacker['phone'])
        cursor.execute(INSERT_HACKER_INFO, hackerData)

        id = cursor.lastrowid

        for skill in hacker["skills"]:
            skillsData = (skill['skill'], skill['rating'], id)
            cursor.execute(INSERT_SKILLS_INFO, skillsData)
    f.close()

def init_database(db):
    conn = sqlite3.connect(db)
    conn.isolation_level = None
    conn.execute('''PRAGMA foreign_keys = ON;''')

    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS skills")
    cursor.execute("DROP TABLE IF EXISTS hackers")
    
    cursor.execute(CREATE_HACKERS_TABLE)
    cursor.execute(CREATE_SKILLS_TABLE)
    insert_hackers_data(cursor)

    conn.close()


init_database("hackers.db")
