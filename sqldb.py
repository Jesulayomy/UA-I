#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(host='localhost', user='vagrant', passwd='1be36f1AINA', db='ua_high')
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students2 (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, full_name VARCHAR(40), quirk VARCHAR(35)) ")
db.commit()

cur.execute("SELECT * FROM students2")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print("{}\t".format(col), end="")
    print("");

names = ('Izuku Midoriya', 'Bakugo Kaachan', 'Himawari Toga')
quirks = ('One For All', 'Explosion', 'Blood Lust')


for i in range(0, 3):
    cur.execute("INSERT INTO students2 (full_name, quirk) VALUES ('{}', '{}')".format(names[i], quirks[i]))
    db.commit()
    print(f"Auto Increment ID: {cur.lastrowid}")

cur.execute("SELECT * FROM students2")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print("|{}\t".format(col), end="")
    print("|")

cur.close()
db.close()

