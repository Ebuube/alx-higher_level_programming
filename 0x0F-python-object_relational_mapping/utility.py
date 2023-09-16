#!/usr/bin/python3
"""
Function to safely execute a query in MySQLdb
"""
import MySQLdb


def execsafe(cur, query, params):
    """
    Safely execute a query on a cursor
    """
    if cur is None or query is None:
        return

    try:
        cur.execute(query, params)
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{:d}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(str(e)))


def run(command=None, statement='', params=()):
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
