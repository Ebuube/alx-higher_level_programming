#!/usr/bin/python3
"""
This script prints the `State` object with the `name` passed as argument
from the database `hbtn_0e_6_usa`
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # Verify correct number of arguments
    if (len(sys.argv) < 5):
        print("\nUsage: {} <mysql username> <mysql password>\
<database name> <state name to search>".format(sys.argv[0]))
        exit(1)

    # Assign arguments
    MY_USER = sys.argv[1]           # User name
    MY_PASS = sys.argv[2]           # User password
    MY_DB = sys.argv[3]             # Database name
    STATE_TO_MATCH = sys.argv[4]    # State name to match

    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        MY_USER, MY_PASS, MY_DB), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()     # instance of a session for conversing

    """
    Print all `State` objects that contain the letter `a`
    """
    result = session.query(State).filter_by(
            name=STATE_TO_MATCH).order_by(State.id).all()

    if (result is None) or (len(result) == 0):
        print("Not found")
    else:
        for instance in result:
            print("{:d}".format(instance.id))
