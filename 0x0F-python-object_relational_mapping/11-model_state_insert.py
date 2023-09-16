#!/usr/bin/python3
"""
Add a new state
"""
from sys import argv
from model_state import Base, State
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

    # Operation on database
    state_name = "Louisiana"
    new = State(name=state_name)

    # Save changes
    sess.add(new)
    sess.commit()

    # Get id of the state
    instance = sess.query(State).filter_by(name=state_name).first()
    if instance is not None:
        print("{:d}".format(instance.id))
