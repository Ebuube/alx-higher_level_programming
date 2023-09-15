#!/usr/bin/python3
"""
Get all states from a database
"""
import MySQLdb
from utility import execsafe
from sys import argv


if __name__ == '__main__':
    # Get database login details from command line arguments
    if len(argv) < 4:
        msg = "Usage: {:s} mysql username, mysql password, database name"
        msg.format(argv[0])
        print(msg)
        exit(1)

    db_login = {
            "host":     'localhost',
            "user":     str(argv[1]),
            "passwd":   str(argv[2]),
            "db":       str(argv[3]),
            "port":     3306}

    # Connection to database
    db = MySQLdb.connect(**db_login)

    # Put a connection to good use
    cur = db.cursor()

    # Execute query
    execsafe(cur, "SELECT * FROM states ORDER BY states.id ASC")

    # Print details
    rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print("{}".format(row))

    # Clean up
    cur.close()
    db.close()
