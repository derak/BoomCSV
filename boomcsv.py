#!/usr/bin/python

"""Basic module for interacting with CSV files.

Copyright (c) 2014 Derak Berreyesa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__ = "Derak Berreyesa (github.com/derak)"
__version__ = "1.0"


import sys
import csv
import operator

class BoomCSV(object):

    def __init__(self, csv_filename):
        self.csv_file = csv_filename

    def check_csv(self, check_field):
        found = False

        with open(self.csv_file, 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row[1] == check_field:
                    found = True
                    break
        return found

    def add_line(self, name, email):
        line = [name, email]

        writer = csv.writer(open(self.csv_file, "ab"), delimiter=',', lineterminator='\n')
        writer.writerow(line)
        return True

    def sort(self, in_file, out_file):
        """in_file and out_file can be the same"""

        data = csv.reader(open(in_file),delimiter=',')
        sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort

        # now write the sorted result into a new CSV file
        with open(out_file, "wb") as f:
            fileWriter = csv.writer(f, delimiter=',')
            for row in sortedlist:
                fileWriter.writerow(row)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "ERROR - You must provide some parameters\n"
        sys.exit(1)

    csv_file = 'some_file.csv'
    bcsv = BoomCSV(csv_file)

    if sys.argv[1] == 'check':
        if len(sys.argv) != 3:
            print "ERROR - You must provide a check parameter\n"
            print "python boomcsv.py check \"joe@bob.com\""
            sys.exit(1)
        
        check_field = sys.argv[2]
        print bcsv.check_csv(check_field)

    if sys.argv[1] == 'add':
        if len(sys.argv) != 4:
            print "ERROR - To add you must also provide name and email"
            print "python boomcsv.py add \"Joe Bob\" \"joe@bob.com\""
            sys.exit(1)

        name = sys.argv[2]
        email = sys.argv[3]
        bcsv.add_line(name,email)
        bcsv.sort(csv_file, csv_file)

