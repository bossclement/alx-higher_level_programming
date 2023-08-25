#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
