#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
   where name matches the argument.
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
    ORDER BY id ASC".format(sys.argv[4]))

    result = cur.fetchall()
    for x in result:
        print(x)

    db.close()
