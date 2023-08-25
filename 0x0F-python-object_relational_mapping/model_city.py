#!/usr/bin/python3

"""
Module contains city class which defines the schema of
cities table of my database
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """
    class that defines schema of city table.
    Attributes:
        id (int): id of the city
        name (str): city name
        __tablename__ (str): name of the table in database
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
