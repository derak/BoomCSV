#!/usr/bin/python

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

    if len(sys.argv) != 2:
        print "ERROR - You must provide a check parameter\n"
        sys.exit(1)

    csv_file = 'some_file.csv'
    check_field = sys.argv[1]

    bcsv = BoomCSV(csv_file)
    print bcsv.check_csv(check_field)

    # how to add a line
    #bcsv.add_line('Joe Bob','joebob12@mycompany.com')

    # how to sort
    #bcsv.sort(csv_file, 'some_file.csv')

