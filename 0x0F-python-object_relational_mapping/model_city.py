#!/usr/bin/python3
"""
Cities in state
"""
from sqlalchemy import (Column, Integer, String, MetaData,
                        ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    A City model

    table: cities
    id: primary key
    name: name of city
    """
    __tablename__ = 'cities'
    id = Column("id", Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', backref='cities')
