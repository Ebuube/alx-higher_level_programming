#!/usr/bin/python3
"""
List all cities by state
"""
import MySQLdb
from utility import execsafe
from sys import argv


if __name__ == '__main__':
    # Get database login details from command line arguments
    if len(argv) < 5:
        msg = "Usage: {} mysql username, password, database name, state name"
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
    query = """SELECT cities.name FROM cities
                JOIN states
                WHERE cities.state_id = states.id
                    AND states.name = %s
                ORDER BY cities.id"""

    params = str(argv[4])

    # cur.execute(query, (params,))
    execsafe(cur, query, (params,))

    # Print details
    rows = cur.fetchall()

    first = False
    if rows is not None:
        for row in rows:
            if first is False:
                print("{}".format(row[0]), end='')
                first = True
            else:
                print(", {}".format(row[0]), end='')
    print()

    # Clean up
    cur.close()
    db.close()
