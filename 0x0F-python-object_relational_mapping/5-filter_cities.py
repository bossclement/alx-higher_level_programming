#!/usr/bin/python3
"""
fetchs all rows that matches specified state name
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state name>".format(
            sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute(
        """SELECT cities.name
        FROM states INNER JOIN cities
        ON states.id = cities.state_id
        WHERE states.name LIKE BINARY %(name)s
        """, {"name": state_name})
    rows = cursor.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
