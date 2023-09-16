#!/usr/bin/python3
"""
First state model
"""
from sqlalchemy import (Column, Integer, String, MetaData)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


my_metadata = MetaData()
Base = declarative_base(metadata=my_metadata)


class State(Base):
    """
    A state model

    table: states
    id: primary key
    name: name of state
    cities: all city objects connected to this state object
    """
    __tablename__ = 'states'
    id = Column("id", Integer, nullable=False, autoincrement=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    # cities = relationship("City", cascade="all, delete")
    cities = relationship("City", backref="state", cascade="all, delete")
