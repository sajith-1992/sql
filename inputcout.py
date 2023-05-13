import csv
with open ("file.csv","r") as file:
    reader = csv.DictReader(file)
    counts = {}
    
    for row in reader:
      favorite = row["Segment"]
      if favorite in counts:
         counts[favorite] += 1
      else:
         counts[favorite] = 1
favorite = input("favorite:")
if favorite in counts:
   print(f"{favorite}:{counts[favorite]}")