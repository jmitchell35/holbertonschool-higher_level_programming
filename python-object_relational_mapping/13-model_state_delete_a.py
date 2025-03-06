#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Main function that will not execute when imported.
    Deletes all State objects with a name containing the letter 'a'.
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

    # Delete all states with names containing the letter 'a'
    session.query(State).filter(State.name.like('%a%')).delete(
        synchronize_session=False)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
