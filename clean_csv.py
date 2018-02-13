#!/usr/bin/python

"""Remove small values from csv
Built to address
value out of range: underflow
CONTEXT:  COPY tmp_table, line 14037, column latitude: "1.0235998427713398e-306"  # noqa
"""

import csv


inputfile =  # input file
outputfile =  # output file

counter = 0

# parsing initialization
dico = dict()
lastOpenedAt = False  # track if current note is lastOpenedAt
depth = list()


# TODO
# make function (with counter from/ to as argument) + try/ except

with open(inputfile) as f:
    with open(outputfile, "w") as csv_file:
        csv_w = csv.writer(csv_file)
        for line in f:
            counter += 1
            if counter % 1e5 == 0:
                print(counter)
            linelist = line.split(',')
            long = linelist.pop()  # last element
            lat = linelist.pop()  # new last element
            try:
                linelist.append(round(float(lat), 10))
                linelist.append(round(float(long), 10))
            except Exception as message:
                print(message)
                linelist.append(0)
                linelist.append(0)
            # print(linelist)
            try:
                csv_w.writerow(linelist)
            except Exception as error:
                print(error)
csv_file.close()
