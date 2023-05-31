#!/usr/bin/python3
"""
This script lists all `cities` from the database `hbtn_0e_4_usa`

It takes 3 arguments `mysql username`, `mysql password` and `database name`
Results are sorted in ascending order by `cities.id`
"""

import MySQLdb
import sys


"""
IMPORTANT FUNCTIONS AND DECLARATIONS
"""


def Run(command=None, statement='', params=()):
    """
    Run - execute a MySQLdb command
    command: the command to run on a cursor object example
        `cur.execute`

    If there is no statement, pass command as it is, example
        `cur.fetchall`
        where it actually means `cur.fetchall()`

    statement: The statement to run
    params (tuple): the parameters to substitute in the statement
    """
    return_value = None
    try:
        if (len(statement) == 0):
            return_value = command()
        else:
            return_value = command(statement, params)
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{:d}]: {:s}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {:s}".format(str(e)))

    return return_value


"""
End of important functions
"""

# Script should only execute if not imported
if __name__ == "__main__":
    if (len(sys.argv) < 4):
        print("\nUsage: {} <mysql username> <mysql password> \
<database name>".format(
            sys.argv[0]))
        exit()

    """
    IMPORTANT DECLARATIONS
    """

    MY_HOST = 'localhost'
    MY_PORT = 3306
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_TABLES = {'states': 'states'}

    # Create a connection with the database
    db = MySQLdb.connect(
            host=MY_HOST,
            port=MY_PORT,
            user=MY_USER,
            passwd=MY_PASS,
            database=MY_DB)

    # Create a cursor object for interacting with the database
    cur = db.cursor()

    Run(cur.execute, """SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    COMMIT""", ())

    # Fetch all results
    rows = Run(cur.fetchall)

    if rows is not None:
        for row in rows:
            print("({}, '{}', '{}')".format(row[0], row[1], row[2]))

    """
    CLEAN UP ACTIONS
    """

    # Close all instances of cursor
    cur.close()

    # Close all instances of database connection
    db.close()
