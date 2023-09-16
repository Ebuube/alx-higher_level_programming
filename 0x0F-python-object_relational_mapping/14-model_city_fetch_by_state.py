#!/usr/bin/python3
"""
Cities in state
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Get database login details from command line arguments
    if len(argv) < 4:
        msg = "Usage: {:s} mysql username, mysql password, database name"
        msg.format(argv[0])
        print(msg)
        exit(1)

    # Global scope -> Application starts
    Session = sessionmaker()

    db_login = {
            "host":     'localhost',
            "user":     str(argv[1]),
            "passwd":   str(argv[2]),
            "db_name":       str(argv[3]),
            "port":     3306}

    engine_url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine_url = engine_url.format(db_login['user'],
                                   db_login['passwd'],
                                   db_login['db_name'])

    # later, in a local scope, create and use a session:
    engine = create_engine(engine_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)

    sess = Session()

    # Get objects of the state
    city_objs = sess.query(City).order_by(City.id).all()

    # Delete state objects with a name containing the letter 'a'
    if city_objs is not None:
        for city in city_objs:
            print("{:s}: ({:d}) {:s}".format(city.state.name,
                  city.id, city.name))
