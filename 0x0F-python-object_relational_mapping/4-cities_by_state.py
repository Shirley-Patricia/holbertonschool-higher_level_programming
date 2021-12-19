#!/usr/bin/python3
"""list all states from database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id=states.id ORDER BY id ASC")

    result = cur.fetchall()
    for x in result:
        print(x)

    db.close()
