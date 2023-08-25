#!/usr/bin/python3
"""
Module contains state class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class that defines schema of state table.
    """
    __table_name__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
