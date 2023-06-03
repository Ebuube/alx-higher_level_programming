#!/usr/bin/python3
"""
This module defines the First City model
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    Define the City model which represents an entity in the database.
    It defines a table named `cities`

    id (sqlalchemy.Integer):    a column of an auto-generated, unique
        integer, can't be null and is a primary key
    name (sqlalchemy.String):   a column of a string with maximum of 128
        characters and can't be null
    state_id (sqlalchemy.Integer):    a column of an integer, can't be null
        and is a foreign key to `states.id`
    state (relationship with State object): this links the state object
        that has this city
    """

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
