import csv
with open("file.csv", "r" ) as file: # this just open the file and name as file  now in next we have to add to the library
    reader = csv.reader(file)
    for row in reader:
        print(row[1])