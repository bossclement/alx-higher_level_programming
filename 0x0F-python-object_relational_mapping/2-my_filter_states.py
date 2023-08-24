#!/usr/bin/python3
"""fetchs all rows by matching column with a specific value"""

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
        "SELECT id, name FROM states WHERE states.name = '{}'".format(state_name))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
