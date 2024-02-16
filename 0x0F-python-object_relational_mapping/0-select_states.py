#!/usr/bin/python3
"""Importing the MySQLdb module"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf-8")
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)
        fetcher = cursor.fetchall()
    except MySQLdb.Error:
        try:
            fetcher = ("MySQLdb Error")
        except IndexError:
            fetcher = ("MySQLdb Error - IndexError")

    for i in fetcher:
        print(i)
    cursor.close()
    connection.close()
