#!/usr/bin/python3
"""list staates in database"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                               db=sys.argv[3], port=3306, host='localhost()')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC;')
    states = cursor.fetchall()
    for st in states:
        print(st)
    cursor.close()
    db.close()
