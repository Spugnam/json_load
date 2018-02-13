#!/usr/bin/python

"""
Convert JM's JSON (with return carriage) into csv format for psql copy command
"""

import csv
import datetime


def parseLine2(line):
    try:
        line = line.replace(',', '').strip().split('"')
        line = [x for x in line if x != '']

        # case "lastOpenedAt": {
        if line[1] == ': {':
            return(line[0], '{')

        # case "longitude": 39.3002585 -> ': 39.3002585'
        try:
            val = line[1].split(' ')[1]
            val = float(val)
            return(line[0], val)
        except Exception:
            pass

        # Main case "appVersion": "3.6.2",
        key, val = line[0], line[-1]
    except Exception as mess:
        print("Unable to parse")
        print(mess)
        return(None)
    return(key, val)


time = '{:%Y-%m-%d_%H-%M-%s}'.format(datetime.datetime.now())
logfile = time + "_log"

cols = ['lastopenedat', 'objectid', 'appname', 'email', 'localeidentifier',
        'devicetype', 'timezone', 'installationid', 'devicetoken', 'latitude',
        'longitude']

outputfile = '/Volumes/G-DRIVE mobile USB-C/JM_Truelle/Files/_Installation.csv'
inputfile = '/Volumes/G-DRIVE mobile USB-C/JM_Truelle/Files/_Installation.json'

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
    #     csv_w.writerow(cols)
        for b in f:
            # new highest-level node
            if b.strip() == '{' or b.strip() == '{ "results": [':
                depth.append('{')
        #         print("depth", len(depth))
            # closing of parent or sub-node
            elif b.strip() in ['}', '},']:
                _ = depth.pop()
        #         print("depth", len(depth))
                if len(depth) == 1:
                    counter += 1
                    if counter % 1e5 == 0:
                        print(counter)
                    # print("****Insertion****", dico)
                    row = []
                    for col in cols:
                        if col in ['latitude', 'longitude']:
                            row.append(dico.get(col, 0))
                        elif col in ['lastopenedat']:
                            row.append(dico.get(col, '-infinity'))
                        else:
                            row.append(dico.get(col, ""))
                    try:
                        csv_w.writerow(row)
                    except Exception as error:
                        print(error)
                    dico = dict()
                if len(depth) == 0:
                    print("Completed file")
                    break
            else:
                key, val = parseLine2(b)
        #             print("Key/ Val: ", key, val)
                if val == '{':
                    depth.append('{')
        #             print("depth", len(depth))
                if key == 'lastOpenedAt':
                    lastOpenedAt = True
                elif key == 'iso':
                    if lastOpenedAt:
                        dico['lastopenedat'] = val
                        lastOpenedAt = False
                elif key.lower() in cols:
                    dico[key.lower()] = val
    csv_file.close()
