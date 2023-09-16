#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)


if __name__ == "__main__":
    # Get database login details from command line arguments
    if len(argv) < 4:
        msg = "Usage: {:s} mysql username, mysql password, database name"
        msg.format(argv[0])
        print(msg)
        exit(1)

    db_login = {
            "host":     'localhost',
            "user":     str(argv[1]),
            "passwd":   str(argv[2]),
            "db_name":       str(argv[3]),
            "port":     3306}
    engine_url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engnie_url = engine_url.format(db_login['user'],
                                   db_login['passwd'],
                                   db_login['db_name'])

    engine = create_engine(engine_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
