#sqlite come with python 
import sqlite3
#connect to a database
db = sqlite3.connect('sajth.db')

c = db.cursor()

#c.execute("""CREATE TABLE sajith(firstname text,lastname text,age int) """)
#c.execute("INSERT INTO sajith VALUES('vishnu', 'mohan','20')")
rows = c.execute("SELECT * FROM sajith")
db.commit()
#close the cursor
for row in rows:
    print(row)


db.close()