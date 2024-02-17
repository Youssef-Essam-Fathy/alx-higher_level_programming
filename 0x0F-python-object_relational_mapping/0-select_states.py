#!/usr/bin/python3
from sys import argv
import MySQLdb
if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = con.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    fetcher = cur.fetchall()
    for i in fetcher:
        print(i)
    cur.close()
    con.close()