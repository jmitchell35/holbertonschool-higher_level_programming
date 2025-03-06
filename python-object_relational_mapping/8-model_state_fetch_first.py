#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Main function that will not execute when imported.
    Prints the first State object from the database.
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

    # Query first State object
    first_state = session.query(State).order_by(State.id).first()

    # Display the result or "Nothing" if the table is empty
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
