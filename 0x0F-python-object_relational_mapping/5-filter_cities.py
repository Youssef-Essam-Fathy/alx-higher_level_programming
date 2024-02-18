#!/usr/bin/python3
"""
Script that lists all cities from the database
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
             INNER JOIN states ON cities.state_id = states.id\
             WHERE states.name = %s\
             ORDER BY cities.id ASC"
    cur.execute(query, [argv[4]])
    fetcher = cur.fetchall()
    for i in fetcher:
        print(i)
    # Clean up process
    cur.close()
    db.close()
