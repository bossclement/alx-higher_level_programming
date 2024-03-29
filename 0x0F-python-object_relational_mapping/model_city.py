#!/usr/bin/python3

"""
Module contains city class which defines the schema of
cities table of my database
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    class that defines schema of cities table.
    Attributes:
        id (int): id of the city
        name (str): city name
        __tablename__ (str): name of the table in database
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
