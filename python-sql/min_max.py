import mysql.connector
from scripts.mysql_parameters import config_ness

mydb = mysql.connector.connect(**config_ness)

mycursor = mydb.cursor()

sql_rec = "SELECT d.recipientvat, COUNT(d.recipientvat), MIN(d.payableamount), MAX(d.payableamount)\
    FROM nesshub.documents AS d\
    GROUP BY d.recipientvat limit 10"

mycursor.execute(sql_rec)

myresult = mycursor.fetchall()
print("Min and max payment per recipientvat")
for x in myresult:
    print(x)


sql_sen = "SELECT d.sendervat, COUNT(d.sendervat), MIN(d.payableamount), MAX(d.payableamount)\
    FROM nesshub.documents AS d\
    GROUP BY d.sendervat limit 10"

mycursor.execute(sql_sen)

myresult = mycursor.fetchall()
print("\n Min and max payment per sendervat")
for x in myresult:
    print(x)