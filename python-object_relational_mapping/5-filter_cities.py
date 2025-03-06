#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
Takes 4 arguments: mysql username, mysql password, database name,
and state name (SQL injection free!).
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Main function that will not execute when imported.
    Lists all cities of a given state from the database.
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

    # Execute the query to get all cities of the given state
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cursor.execute(query, (state_name,))

    # Fetch all the results
    cities = cursor.fetchall()

    # Format the results as a comma-separated string
    cities_list = [city[0] for city in cities]
    print(", ".join(cities_list))

    # Close cursor and database connection
    cursor.close()
    db.close()
