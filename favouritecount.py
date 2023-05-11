import csv
with open ("file.csv","r") as file:
    reader = csv.DictReader(file)
    Government,Midmarket = 0,0
    for row in reader:
      favorite = row["Segment"]
      print(favorite)
      if favorite == "Government":
       Government += 1
      elif favorite == "Midmarket":
       Midmarket += 1
      #elif favorite == Channel:
       #Channel += 1
       # 
print(f"Goverment:{Government}")
print(f"Midmarket:{Midmarket}")
    #print(f"channel:{Channel}")

