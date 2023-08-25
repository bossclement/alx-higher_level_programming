#!/usr/bin/python3
"""
Prints states that contains letter a 
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    objects = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    for obj in objects:
        print("{}: {}".format(obj.id, obj.name))
