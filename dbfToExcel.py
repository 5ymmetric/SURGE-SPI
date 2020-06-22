#!/usr/bin/python

import csv
from dbfpy import dbf
import os
import sys

filename = sys.argv[1]
required = ["ID_2", "SUM"]
newList = []
if filename.endswith('.dbf'):
    print "Converting %s to csv" % filename
    csv_fn = filename[:-4]+ ".csv"
    with open(csv_fn,'wb') as csvfile:
        in_db = dbf.Dbf(filename)
        out_csv = csv.writer(csvfile)
        names = []
        for field in in_db.header.fields:
            if field.name in required:
                names.append(field.name)
        out_csv.writerow(names)

        for k in range(0, len(in_db)):
            temp = []
            temp.append(in_db[k]["ID_2"])
            temp.append(in_db[k]["SUM"])
            newList.append(temp)

        for p in newList:
            out_csv.writerow(p)

        in_db.close()
        print "Done..."
else:
  print "Filename does not end with .dbf"
