import mysql.connector
from scripts.mysql_parameters import config_ness

mydb = mysql.connector.connect(**config_ness)
mycursor = mydb.cursor()
mycursor.execute("SET sql_mode = (SELECT REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY',''))")


print("Number of receipts for each senderVAT \n")
sql_sen = "SELECT sendervat, COUNT(sendervat), SUM(payableamount) \
    FROM nesshub.documents \
    GROUP BY sendervat \
    ORDER BY SUM(payableamount) DESC limit 20"
mycursor.execute(sql_sen)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\n Number of receipts for each recipientVAT \n")
sql_rec = " SELECT recipientvat, COUNT(recipientvat), SUM(payableamount)\
    FROM nesshub.documents\
    GROUP BY recipientvat\
    ORDER BY SUM(payableamount) DESC limit 20"
mycursor.execute(sql_rec)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\n Number of passive receipts (ricevute?)\n")
sql_pas = "SELECT r.documenttype, COUNT(r.documenttype), SUM(payableamount)\
          FROM nesshub.documents AS d\
          JOIN nesshub.processingrequests AS r ON d.uuid = r.uuid\
          WHERE r.documenttype = 'CICLO_PASSIVO' OR r.documenttype = 'NOTIFICHE'\
          GROUP BY r.documenttype" # OUT
mycursor.execute(sql_pas)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\nNumber of active receipts (inviate?)\n")
sql_act = "SELECT r.documenttype, COUNT(r.documenttype), SUM(payableamount)\
    FROM nesshub.documents AS d\
    JOIN nesshub.processingrequests AS r ON d.uuid = r.uuid\
    WHERE r.documenttype <> 'CICLO_PASSIVO' AND r.documenttype <> 'NOTIFICHE'\
    GROUP BY r.documenttype" #IN
mycursor.execute(sql_act)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\n Number of receipts per day of the week\n")
sql_day = "SELECT DAYNAME(issuedate), COUNT(DAYOFWEEK(issuedate)), SUM(payableamount)\
        FROM nesshub.documents\
        GROUP BY DAYOFWEEK(issuedate)"
mycursor.execute(sql_day)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
