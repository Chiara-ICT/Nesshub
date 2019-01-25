import mysql.connector
from scripts.mysql_parameters import config_ness

mydb = mysql.connector.connect(**config_ness)
mycursor = mydb.cursor()

mycursor.execute("SET sql_mode = (SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))")


sql_day = " SELECT receiveddate, COUNT(uuid), documenttype, SUM(payableamount) FROM nesshub.documents \
    GROUP BY documenttype, DAY(receiveddate)\
    ORDER BY receiveddate ASC limit 10"

sql_month = " SELECT receiveddate, COUNT(uuid), documenttype, SUM(payableamount), receiveddate FROM nesshub.documents\
    GROUP BY documenttype, MONTH(receiveddate)\
    ORDER BY receiveddate ASC limit 10"

sql_year = " SELECT receiveddate, COUNT(uuid), documenttype, SUM(payableamount), receiveddate FROM nesshub.documents\
    GROUP BY documenttype, YEAR(receiveddate)\
    ORDER BY YEAR(receiveddate) limit 10"

mycursor.execute(sql_day)
myresult = mycursor.fetchall()
print("Sum of receipts per day")
for x in myresult:
    print(x)


mycursor.execute(sql_month)
myresult = mycursor.fetchall()
print("\n Sum of receipts per month")
for x in myresult:
    print(x)


mycursor.execute(sql_year)
myresult = mycursor.fetchall()
print("\n Sum of receipts per year")
for x in myresult:
    print(x)