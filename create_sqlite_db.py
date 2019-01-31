"""Function to create sqlite database for testing"""

import sqlite3
from sqlite3 import Error

import os


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    create_connection(os.path.join(os.getcwd(), "ezpo.sqlite"))
