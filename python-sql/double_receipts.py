import mysql.connector
from scripts.mysql_parameters import config_ness

mydb = mysql.connector.connect(**config_ness)
mycursor = mydb.cursor()
mycursor.execute("SET sql_mode = (SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))")

sql = "SELECT uuid, COUNT(uuid), issuedate, sendername, sendervat, recipientname, recipientvat, payableamount \
    FROM nesshub.documents\
    GROUP BY sendername, sendervat, recipientname, recipientvat, payableamount\
    HAVING COUNT(uuid) > 1"

mycursor.execute(sql)
myresult = mycursor.fetchall()

print("Double receipt: same sender, recipient and payable ampunt but different uuid and issuedate \n")
for x in myresult:
    print(x)
print("\n Number of double receipts:", mycursor.rowcount)
