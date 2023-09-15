#!/usr/bin/python3
"""
Function to safely execute a query in MySQLdb
"""
import MySQLdb


def execsafe(cur, query):
    """
    Safely execute a query on a cursor
    """
    if cur is None or query is None:
        return

    try:
        cur.execute(query)
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{:d}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(str(e)))
