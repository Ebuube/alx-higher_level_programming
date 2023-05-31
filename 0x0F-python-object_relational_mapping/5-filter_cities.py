#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all `cities` of that state, using the database `hbtn_0e_4_usa`

Results are sorted in ascending order by cities.id

The queries are SQL Injection Free!
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
    if (len(sys.argv) < 5):
        print("\nUsage: {} <mysql username> <mysql password> \
<database name> <state name>".format(
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
    STATE_MATCH = sys.argv[4]

    # Create a connection with the database
    db = MySQLdb.connect(
            host=MY_HOST,
            port=MY_PORT,
            user=MY_USER,
            passwd=MY_PASS,
            database=MY_DB)

    # Create a cursor object for interacting with the database
    cur = db.cursor()

    Run(cur.execute, """SELECT cities.name FROM cities
    WHERE state_id = (
        SELECT states.id FROM states
        WHERE states.name = %s)
    ORDER BY cities.id ASC;
    COMMIT""", (STATE_MATCH,))

    # Fetch all results
    rows = Run(cur.fetchall)

    # Display results
    if rows != ():
        print(", ".join([row[0] for row in rows]))
    else:
        print()

    """
    CLEAN UP ACTIONS
    """

    # Close all instances of cursor
    cur.close()

    # Close all instances of database connection
    db.commit()
    db.close()
