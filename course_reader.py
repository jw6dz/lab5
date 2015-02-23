import sqlite3 as lite
import csv
import sys

def load_course_database(db_name, csv_filename):
    f = open(csv_filename)
    csv_f = csv.reader(f)
    con = lite.connect(db_name)
    with con:
         cur = con.cursor()
         cur.execute("CREATE TABLE coursedata(deptID TEXT, courseNum INT, semester INT, meetingType TEXT, seatsTaken INT, seatsOffered INT, instructor TEXT)")
    #for row in csv_f: #every row is a list
    #    print(row)
    for row in csv_f:
        IDtup = (row[0], row[1])
        with con:
            cur = con.cursor()
            sql_cmd = "INSERT INTO coursedata values(?. ?. row[2], row[3], row[4]. row[5]. row[6])"
            cur.execute(sql_cmd, IDtup)

load_course_database("hi", "seas-courses-5years.csv")
