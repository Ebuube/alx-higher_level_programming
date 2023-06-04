#!/usr/bin/python3
"""
This module defines the First State model
"""

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)

my_metadata = MetaData()

Base = declarative_base(metadata=my_metadata)


class State(Base):
    """
    Define the State model which represents an entity in the database.
    It defines a column named `states`.

    id (sqlalchemy.Integer):    a column of an auto-generated, unique,
        integer, can't be null and is a primary key
    name (sqlalchemy.String):   a column of a string with maximum 128
        characters and can't be null
    cities (list of City objects):    a relationsip with the class `City`
        If the `State` object is deleted, all linked `City` objects must be
        automatically deleted.
    """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
