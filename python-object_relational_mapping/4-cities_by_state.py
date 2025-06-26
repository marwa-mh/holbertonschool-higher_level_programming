#!/usr/bin/python3
"""
displays all cities
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
    qstr = "SELECT c.id, c.name, s.name FROM cities c JOIN states s"
    qstr += " ON c.state_id =s.id ORDER BY c.id"
    cur.execute(qstr)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
