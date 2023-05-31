#!/usr/bin/python3
"""
This script lists all `states` from the database `hbtn_0e_0_usa`
"""

import MySQLdb
import sys


if (len(sys.argv) < 4):
    print("\nUsage: {} <mysql username> <mysql password> \
<database name>".format(
        sys.argv))
    exit()


"""
IMPORTANT FUNCTIONS AND DECLARATIONS
"""

MY_HOST = 'localhost'
MY_PORT = 3306
MY_USER = sys.argv[1]
MY_PASS = sys.argv[2]
MY_DB = sys.argv[3]
MY_TABLES = {'states': 'states'}


def Run(command=None, statement=''):
    """
    Run - execute a MySQLdb command
    command: the command to run on a cursor object example
        `cur.execute`

    If there is no statement, pass command as it is, example
        `cur.fetchall`
        where it actually means `cur.fetchall()`

    statement: The statement to run
    """
    return_value = None
    try:
        if (len(statement) == 0):
            return_value = command()
        else:
            return_value = command(statement)
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{:d}]: {:s}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {:s}".format(str(e)))

    return return_value


"""
End of important functions
"""


# Create a connection with the database
db = MySQLdb.connect(
        host=MY_HOST,
        port=MY_PORT,
        user=MY_USER,
        passwd=MY_PASS,
        database=MY_DB)

# Create a cursor object for interacting with the database
cur = db.cursor()

Run(cur.execute, """SELECT id, name FROM {}
        WHERE BINARY name LIKE 'N%'
        ORDER BY states.id;
        COMMIT""".format(MY_TABLES['states']))

# Fetch all results
rows = Run(cur.fetchall)

for row in rows:
    print("({}, '{}')".format(row[0], row[1]))
