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
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8")
    cur = conn.cursor()
    qstr = "SELECT c.name FROM cities c JOIN states s"
    qstr += " ON c.state_id =s.id"
    qstr += " WHERE BINARY s.name = %s ORDER BY c.id"
    cur.execute(qstr, (state_name,))
    query_rows = cur.fetchall()
    sep_chr = ''
    for row in query_rows:
        print(sep_chr, end='')
        print(row[0], end="")
        sep_chr = ', '
    print()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
