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
    curr = connection.cursor()
    try:
        query = "SELECT * from states ORDER BY id ASC"
        curr.execute(query)
        fetcher = curr.fetchall()
    except MySQLdb.Error:
        try:
            fetcher = ("MySQLdb Error")
        except IndexError:
            fetcher = ("MySQLdb Error - IndexError")

    for i in fetcher:
        print(i)
    curr.close()
    connection.close()
