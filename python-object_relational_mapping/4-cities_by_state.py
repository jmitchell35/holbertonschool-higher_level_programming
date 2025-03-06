#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
Takes 3 arguments: mysql username, mysql password and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Main function that will not execute when imported.
    Lists all cities from the database with their corresponding state names.
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

    # Execute the query to get all cities with their state names
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    cursor.execute(query)

    # Fetch all the results
    cities = cursor.fetchall()

    # Print the results
    for city in cities:
        print(city)

    # Close cursor and database connection
    cursor.close()
    db.close()
