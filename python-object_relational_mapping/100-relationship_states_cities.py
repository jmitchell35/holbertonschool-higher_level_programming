#!/usr/bin/python3
"""Script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    california = State(name="California")
    california.cities.append(City(name="San Francisco"))

    session.add(california)
    session.commit()

    session.close()
