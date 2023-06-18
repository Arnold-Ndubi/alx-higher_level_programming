#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()

        # Execute the query to fetch all states
        cur.execute("SELECT * FROM states")
        
        # Fetch all the rows from the query result
        rows = cur.fetchall()
        
        # Print the states
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)
    finally:
        # Close the cursor and database connection
        if cur:
            cur.close()
        if db:
            db.close()

