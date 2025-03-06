#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Main function that will not execute when imported.
    Creates State "California" with City "San Francisco" using relationship.
    """
    # Get MySQL connection parameters from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Create a new State "California" with City "San Francisco"
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add both objects to the session
    session.add(new_state)
    session.add(new_city)
    session.commit()

    # Close the session
    session.close()
