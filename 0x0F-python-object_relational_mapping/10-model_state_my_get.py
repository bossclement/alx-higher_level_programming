#!/usr/bin/python3
"""
Prints state object with name passed as argument
"""

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=sys.argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")
