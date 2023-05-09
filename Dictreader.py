import csv
with open("file.csv","r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        favorite = row["Segment"]
        print(favorite)
        
