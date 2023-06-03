#!/usr/bin/python3
"""
This script prints all `City` objects from the datbase `hbtn_0e_14_usa`
"""

import sys
from model_state import Base, State
from model_city import City
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

    for city in session.query(City).order_by(City.id).all():
        print("{}: ({}) {}".format(
            city.state.name, city.id, city.name))

    # clean up action
    session.close()
    engine.dispose()
