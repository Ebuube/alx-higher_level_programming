#!/usr/bin/python3
"""
This script lists all `State` objects, and corresponding `City` objects,
contained in the database `hbtn_0e_101_usa`

Format:

<state id>: <state name>
<tabulation><city id>: <city name>

The script takes 3 arguments: `mysql username`, `mysql password` and
`database name`
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

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # clean up action
    session.commit()
    session.close()
    engine.dispose()
