#!/usr/bin/python3
"""a script that lists all states from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
             ORDER BY ID ASC".format(argv[4])
    cur.execute(query)
    fetcher = cur.fetchall()
    for i in fetcher:
        print(i)
    cur.close()
    db.close()
