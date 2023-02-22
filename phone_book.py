
import csv

#with csv.reader
'''with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            print(row[1], row[-1])
        line_count += 1'''

#with csv.DictReader
with open('data/phone_book.csv', mode='r') as pupsi_file:
    pupsi_reader = csv.DictReader(pupsi_file)
    for row in pupsi_reader:
        print(row['first_name'], row['phone_number'])
