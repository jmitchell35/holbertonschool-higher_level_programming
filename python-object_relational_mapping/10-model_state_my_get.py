#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Takes 4 arguments: mysql username, mysql password, database name,
and state name to search.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Main function that will not execute when imported.
    Prints the State object with the name passed as argument.
    """
    # Get MySQL connection parameters and state name from CLI arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Display the state id or "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
