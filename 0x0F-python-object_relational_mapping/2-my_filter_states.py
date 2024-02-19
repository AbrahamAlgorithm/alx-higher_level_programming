#!/usr/bin/python3
"""select all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE name='{:s}'\
            ORDER BY `id` ASC".format(sys.argv[4]))
    for i in cur.fetchall():
        print(i)
    cur.close()
    db.close()
