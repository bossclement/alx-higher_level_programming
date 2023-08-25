#!/usr/bin/python3
"""
Module contains state class
which defines the schema of states table
of my database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class that defines schema of state table.
    Attributes:
        id (int): id of the state
        name (str): state name
    """
    __table_name__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
