#!/usr/bin/python3
"""take the name of a state as an argument and lists
   all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cur = db.cursor()

    cur.execute("""
        SELECT
            cities.name FROM cities
        INNER JOIN
            states ON cities.state_id=states.id
        WHERE
            states.name= %(states.name)s
        ORDER BY cities.id ASC
    """, {
        'states.name': sys.argv[4]
    })

    result = cur.fetchall()
    i = 0
    for x in result:
        print(x[0], end="")
        if i < (len(result) - 1):
            print(", ", end="")
            i += 1
    print()

    db.close()
