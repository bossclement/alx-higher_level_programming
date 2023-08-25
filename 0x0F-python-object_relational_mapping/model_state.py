#!/usr/bin/python3

"""
Module contains state class which defines the schema of
states table of my database
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
        __tablename__ (str): name of the table in database
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
