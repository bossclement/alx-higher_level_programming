#!/usr/bin/python3
"""
Prints the first state from a database
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

    rows = session.query(State).all()
    if rows:
        row = rows[0]
        print("{}: {}".format(row.id, row.name))
