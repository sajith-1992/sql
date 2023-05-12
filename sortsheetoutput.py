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

for favorite in sorted(counts ,key = lambda segment:counts[segment],reverse= True):# this wil sort on the value it has not the key value hear will be the number 
   print(f"{favorite}:{counts[favorite]}")