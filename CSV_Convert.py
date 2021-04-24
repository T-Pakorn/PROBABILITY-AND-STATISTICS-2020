import Converter
import os
import csv

csv_in = open('August_2018_Nationwide_Airplane_Delay_Statistic_BackUp.csv', 'rt')
csv_out = open('August_2018_Nationwide_Airplane_Delay_Statistic.csv', 'wt')

writer = csv.writer(csv_out, delimiter=',',lineterminator='\n')
counter = 0
for row in csv.reader(csv_in):
    if counter > 0:  # skips the header
        row[3] = int(Converter.convertToMin(row[3]))
        row[4] = int(Converter.convertToMin(row[4]))
    else:
        row = ["FL_DATE","ORIGIN","DEST","DEP_DELAY","ARR_DELAY"]
    print(row)
    writer.writerow(row)
    counter+=1