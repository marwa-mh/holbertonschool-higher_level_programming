#!/usr/bin/python3
"""
displays all values in the states
depend on name parameter
"""


import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8")
    cur = conn.cursor()
    qstr = "SELECT * FROM states"
    qstr += f" WHERE BINARY name LIKE '{state_name}' ORDER BY id ASC".format()
    cur.execute(qstr)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
