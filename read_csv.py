#!/usr/bin/python

"""Read csv to find error that crashes the load
Built to address
value out of range: underflow
CONTEXT:  COPY tmp_table, line 14037, column latitude: "1.023599842771339e-306"
"""

inputfile = '/Volumes/G-DRIVE mobile USB-C/JM_Truelle/Files/_Installation_cleaned.csv'  # noqa

# parsing initialization
dico = dict()
lastOpenedAt = False  # track if current note is lastOpenedAt
depth = list()
counter = 0


with open(inputfile) as f:
    # with open(outputfile, "w") as csv_file:
        # csv_w = csv.writer(csv_file)
    for line in f:
        counter += 1
        if counter == 14037:
            print(counter)
            print(line)
            break
        # linelist = line.split(',')
        # long = linelist.pop() # last element
        # lat = linelist.pop() # new last element
        # try:
        #     linelist.append(round(float(lat), 10))
        #     linelist.append(round(float(long), 10))
        # except Exception as message:
        #     print(message)
        #     linelist.append(0)
        #     linelist.append(0)
        # # print(linelist)
        # try:
        #     # csv_w.writerow(linelist)
        # except Exception as error:
        #     print(error)
# csv_file.close()
