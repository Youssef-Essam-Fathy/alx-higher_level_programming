#!/usr/bin/python3
"""
a script that lists all cities from the database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1:4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        cur = db.cursor()
        query = "SELECT c.id, c.name, s.name AS state_name FROM cities c JOIN states s ON c.state_id = s.id ORDER BY c.id ASC"
        cur.execute(query)
        fetcher = cur.fetchall()
        for row in fetcher:
            print(f"({row[0]}, '{row[1]}', '{row[2]}')")
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")
