#!/usr/bin/python3
"""filters states from a table of a user in a database by name"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, name FROM states WHERE states.name LIKE BINARY 'N%'")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
