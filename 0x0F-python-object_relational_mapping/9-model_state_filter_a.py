#!/usr/bin/python3
"""
This script prints the `State` objects that contain the letter `a` from the
database `hbtn_0e_6_usa
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
    MY_USER = sys.argv[1]   # User name
    MY_PASS = sys.argv[2]   # User password
    MY_DB = sys.argv[3]     # Database name

    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        MY_USER, MY_PASS, MY_DB), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()     # instance of a session for conversing

    """
    Print all `State` objects that contain the letter `a`
    """
    result = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

    if (result is None) or (len(result) == 0):
        pass    # do nothing
    else:
        for instance in result:
            print("{:d}: {:s}".format(instance.id, instance.name))
