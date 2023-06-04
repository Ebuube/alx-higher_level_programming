#!/usr/bin/python3
"""
This script creates the `State` "California" with the `City` "San Francisco"
from the database `hbtn_0e_100_usa`
"""

import sys
from relationship_state import Base, State
from relationship_city import City
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

    # Create State
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # add new state to the current transaction
    session.add(new_state)
    # session.add(new_city)

    """
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("{}: {}".format(city.id, city.name))
    """

    # clean up action
    session.commit()
    session.close()
    engine.dispose()