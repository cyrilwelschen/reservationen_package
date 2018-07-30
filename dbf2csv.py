#!/usr/bin/python2

import csv
from dbfpy import dbf
import sys

filename = sys.argv[1]
if filename.endswith('.dbf'):
    print "Converting %s to csv" % filename
    csv_fn = filename[:-4]+ ".csv"
    with open(csv_fn,'wb') as csv_file:
        in_db = dbf.Dbf(filename)
        out_csv = csv.writer(csv_file)
        names = []
        for field in in_db.header.fields:
            names.append(field.name)
        out_csv.writerow(names)
        print "Here"
        print type(in_db)
        try:
            for rec in in_db:
                out_csv.writerow(rec.fieldData)
        except ValueError:
            print "caught error"
        in_db.close()
        print "Done..."
else:
  print "Filename does not end with .dbf"
