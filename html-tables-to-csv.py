#!/usr/bin/python

from bs4 import BeautifulSoup
import csv
import sys
import os

filename = sys.argv[1]
fin      = open(filename,'r')

filename_no_ext = os.path.splitext(filename)[0]

print("Opening file")
fin  = fin.read()

print("Parsing file")
soup = BeautifulSoup(fin)

print("Preemptively removing unnecessary tags")
[s.extract() for s in soup('script')]

print("CSVing file")
tablecount = -1
for table in soup.findAll("table"):
  tablecount += 1
  print("Processing Table #%d" % (tablecount))
  with open(filename_no_ext+'_'+str(tablecount)+'.csv', 'w') as csvfile:
    fout = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in table.findAll('tr'):
      cols = row.findAll(['td','th'])
      if cols:
        cols = [x.text for x in cols]
        fout.writerow(cols)
