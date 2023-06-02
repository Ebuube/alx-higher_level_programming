#!/usr/bin/python3
"""
This script changes the name of a `State` object from the database
`hbtn_0e_6_usa`
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
    Change the name of the `State` where `id = 2` to `New Mexico`
    """
    STATE_ID = 2
    STATE_NAME = 'New Mexico'
    session.query(State).filter(
            State.id == STATE_ID).update({'name': STATE_NAME})

    session.commit()    # commit the change to the database
