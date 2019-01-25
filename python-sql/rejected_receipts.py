import mysql.connector
from scripts.mysql_parameters import config_ness

mydb = mysql.connector.connect(**config_ness)
mycursor = mydb.cursor()

sql = "SELECT d.*, r.status \
    FROM nesshub.documents AS d \
    JOIN nesshub.processingrequests AS r ON d.uuid = r.uuid \
    WHERE d.status = 'NotificaScarto' OR r.status = 'NotificaScarto'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print("Rejected receipts: STATUS = NotificaScarto\n")

for x in myresult:
    print(x)

print("\nThe number of rejected receipts is", mycursor.rowcount)