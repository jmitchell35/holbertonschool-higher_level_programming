#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Main function that will not execute when imported.
    Changes the name of the State where id = 2 to "New Mexico".
    """
    # Get MySQL connection parameters from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the name if the state was found
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
