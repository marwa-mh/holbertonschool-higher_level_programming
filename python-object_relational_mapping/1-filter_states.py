#!/usr/bin/python3
"""
script that lists all states with a name statring with N
"""


import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8")
    cur = conn.cursor()
    qstr = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cur.execute(qstr)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
