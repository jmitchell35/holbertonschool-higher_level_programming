#!/usr/bin/python3
"""Creates State with City"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")

    san_francisco = City(name="San Francisco")
    san_francisco.state = california

    session.add(california)
    session.add(san_francisco)
    session.commit()

    session.close()
