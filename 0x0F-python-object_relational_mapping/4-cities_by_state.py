#!/usr/bin/python3
"""a script that lists all cities from the database """
from sys import argv
import MySQLdb

if __name__ == "__main":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = conn.cursor()
    query = "SELECT * FROM cities\
             INNER JOIN states ON cities.state_id = states.id\
             ORDER BY cities.id ASC"
    cur.execute(query)
    fetcher = cur.fetchall()
    for i in fetcher:
        print(i)
    cur.close()
    conn.close()
