import csv

def load_course_database(db_name, csv_filename):
    f = open(csv_filename)
    csv_f = csv.reader(f)
    for row in csv_f: #every row is a list
        print(row)

load_course_database("hi", "seas-courses-5years.csv")