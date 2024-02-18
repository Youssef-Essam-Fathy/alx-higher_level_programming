#!/usr/bin/python3
"""a script that lists all cities from the database """
import MySQLdb
from sys import argv

if __name__ == "__main":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    fetcher = cur.fetchall()
    for i in fetcher:
        print(i)
    cur.close()
    conn.close()
