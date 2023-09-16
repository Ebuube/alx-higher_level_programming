#!/usr/bin/python3
"""
Update a state
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

    # Get object of the state
    state_id = 2
    instance = sess.query(State).filter_by(id=state_id).first()

    # Update the name of the instance
    instance.name = "New Mexico"

    # Save changes
    sess.commit()
