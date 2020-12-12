#!/usr/bin/python3
'''
list staates in database
'''
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(user=sys.argv[1], pass=sys.argv[2],
                               db=sys.argv[3], host='localhost()',
                               port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    states = cursor.fetchall()
    for st in states:
        print(state)
    cursor.close()
    db.close()
