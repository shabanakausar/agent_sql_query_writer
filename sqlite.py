#*zx~t*~q77AB$zu
import sqlite3

##connect to sqllite
connection = sqlite3.connect("student.db")

## create a cursor object to insert record, create table
cursor=connection.cursor()

# create the table

table_info="""
create table STUDENT(NAME VARCHAR(25),CLASSS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)
"""
cursor.execute("DROP TABLE IF EXISTS STUDENT")
cursor.execute(table_info)

# Insert some more records
cursor.execute("INSERT INTO STUDENT VALUES('Alice','Data Science','A',95)")
cursor.execute("INSERT INTO STUDENT VALUES('Bob','Data Science','B',88)")
cursor.execute("INSERT INTO STUDENT VALUES('Charlie','Data Science','A',72)")
cursor.execute("INSERT INTO STUDENT VALUES('Diana','Data Science','C',64)")
cursor.execute("INSERT INTO STUDENT VALUES('Ethan','Data Science','A',91)")

cursor.execute("INSERT INTO STUDENT VALUES('Fiona','DevOps','A',78)")
cursor.execute("INSERT INTO STUDENT VALUES('George','DevOps','B',83)")
cursor.execute("INSERT INTO STUDENT VALUES('Hannah','DevOps','A',99)")
cursor.execute("INSERT INTO STUDENT VALUES('Ian','DevOps','C',56)")
cursor.execute("INSERT INTO STUDENT VALUES('Jade','DevOps','B',81)")

cursor.execute("INSERT INTO STUDENT VALUES('Kevin','Marketing','A',92)")
cursor.execute("INSERT INTO STUDENT VALUES('Laura','Marketing','B',70)")
cursor.execute("INSERT INTO STUDENT VALUES('Martin','Marketing','C',66)")
cursor.execute("INSERT INTO STUDENT VALUES('Nina','Marketing','A',89)")
cursor.execute("INSERT INTO STUDENT VALUES('Oscar','Marketing','B',73)")


## Display all the records
print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)


## Commit your changes in the database
connection.commit()
connection.close()