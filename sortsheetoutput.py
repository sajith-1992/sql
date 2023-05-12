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
def get_value(segment):
   return counts[segment]
for favorite in sorted(counts ,key =get_value, reverse =True):
   print(f"{favorite}:{counts[favorite]}")