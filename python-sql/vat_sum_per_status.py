import mysql.connector
import os

mydb = mysql.connector.connect(
  host=os.getenv("DB_HOST","localhost"),
  port=os.getenv("DB_PORT",3307),
  user="root",
  passwd="chiara",
  database="nesshub"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SET sql_mode = (SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))")


sql_rec = "SELECT d.sendervat, d.recipientvat, SUM(d.payableamount), d.status\
        FROM nesshub.documents AS d GROUP BY d.status, d.recipientvat limit 10"
sql_sen =  "SELECT d.sendervat, d.recipientvat, SUM(d.payableamount), d.status\
        FROM nesshub.documents AS d GROUP BY d.status, d.sendervat limit 10"

print("Below the sum of the money per recipientvat and status")
mycursor.execute(sql_rec)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("\n")
print("Below the sum of the money per sebdervat and status")
mycursor.execute(sql_sen)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
