#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument, safe from MySQL injections.
Takes 4 arguments: mysql username, mysql password, database name, and state
name.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Main function that will not execute when imported.
    Displays values in states table where name matches the given argument,
    using parameterized queries to prevent SQL injection.
    """
    # Get MySQL connection parameters and state name from CLI arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute the query using parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
