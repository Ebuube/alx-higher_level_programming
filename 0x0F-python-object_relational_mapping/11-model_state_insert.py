#!/usr/bin/python3
"""
This script adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # Verify correct number of arguments
    if (len(sys.argv) < 4):
        print("\nUsage: {} <mysql username> <mysql password>\
<database name>".format(sys.argv[0]))
        exit(1)

    # Assign arguments
    MY_USER = sys.argv[1]           # User name
    MY_PASS = sys.argv[2]           # User password
    MY_DB = sys.argv[3]             # Database name

    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        MY_USER, MY_PASS, MY_DB), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()     # instance of a session for conversing

    """
    Create a new state object
    """
    STATE_NAME = "Louisiana"
    new_state = State(name=STATE_NAME)

    """
    Add a new state object with name "Louisiana"
    """
    session.add(new_state)
    session.commit()        # commit the change to the database

    """
    Print the id of the newly created state record
    """
    result = session.query(State).filter_by(
            name=STATE_NAME).order_by(State.id).one()

    if result is None:
        print("Not found")
    else:
        print("{:d}".format(result.id))
