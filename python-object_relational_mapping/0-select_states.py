#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
Takes 3 arguments: mysql username, mysql password and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Main function that will not execute when imported.
    Lists all states from the database hbtn_0e_0_usa.
    """
    # Get MySQL connection parameters from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to get all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
