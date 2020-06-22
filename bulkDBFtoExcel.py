import arcpy
from dbfpy import dbf
from arcpy import env
import csv
import os
import sys
import time

'''Convert every DBF table into CSV table.
'''

t0 = time.time()

pathlist = []
pathlist.append("")
pathlist.append("C:\\Users\\kpagilla2\\Desktop\\India_Clipped\\DBF\\2019_Output")
pathlist.append("C:\\Users\\kpagilla2\\Desktop\\India_Clipped\\DBF\\2019_Output\\Excel")

env.workspace = pathlist[1] # Set new workplace where tables are located
tablelist = arcpy.ListTables() # list tables in file

required = ["ID_2", "SUM"]

for table in tablelist: # iterate through every table

    newList = []
    #make sure you are just working with .dbf tables
    if table.endswith('.dbf'):
        #name csv the same as the .dbf table just with .csv at the end
        csv_fn = table[:-4]+ ".csv"
        with open(pathlist[2]+"\\"+csv_fn,'wb') as csvfile: # name output path

            in_db = dbf.Dbf(pathlist[1]+"\\"+table)
            out_csv = csv.writer(csvfile)
            #copy row names and items in rows from dbf to csv
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
    #keep track of processing
    print "Processing ",table[:-4]+".csv table complete."

t1 = time.time()

print("Time elapsed: %.2f minutes" % ((t1 - t0)/60))

print("===================Done===========================")
