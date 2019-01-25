import mysql.connector
import scripts.mysql_parameters as p

mydb = mysql.connector.connect(
    host = p.DB_HOST,
    port = p.DB_PORT,
    user = p.DB_USER,
    passwd = p.DB_PASSWORD,
    database = p.DB_DATABASE
)

mycursor = mydb.cursor()

mycursor.execute("SELECT HOUR(receiveddate) , COUNT(HOUR(receiveddate)) FROM nesshub.documents GROUP BY HOUR(receiveddate)")
myresult = mycursor.fetchall()

print("Number of receipts received per hour")
for x in myresult:
    print(x)
    #print("at", x[0], "number of receipts", x[1])

print("\n")
MAX = 0
HOUR_MAX = 0
for x in myresult:
    if x[1] > MAX:
        MAX = x[1]
        HOUR_MAX = x[0]
MIN = MAX
HOUR_MIN = 0
for x in myresult:
    if x[1] < MIN:
        MIN = x[1]
        HOUR_MIN = x[0]

print("The hour when more receipts (", MAX, ") are received is ", HOUR_MAX,". \nThe hour when the fewest receipts are received (", MIN, ") is", HOUR_MIN, ".\n")

# print("\n Hours in descending order according to the number of received receipts")
# mycursor.execute("SELECT HOUR(receiveddate) , COUNT(HOUR(receiveddate))\
#     FROM nesshub.documents\
#     GROUP BY HOUR(receiveddate)\
#     ORDER BY COUNT(HOUR(receiveddate)) DESC")
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)
#
# print("\n Hours in descending order according to the number of received receipts")
# mycursor.execute("SELECT HOUR(receiveddate) , COUNT(HOUR(receiveddate))\
#     FROM nesshub.documents\
#     GROUP BY HOUR(receiveddate)\
#     ORDER BY COUNT(HOUR(receiveddate)) DESC")
# myresult = mycursor.fetchone()
# print(myresult)
# -- Best hour
# SELECT HOUR(receiveddate) , COUNT(HOUR(receiveddate))
# FROM nesshub.documents
# GROUP BY HOUR(receiveddate)
# ORDER BY COUNT(HOUR(receiveddate)) DESC
# LIMIT 1;
#
# -- Worst hour
# SELECT HOUR(receiveddate) , COUNT(HOUR(receiveddate))
# FROM nesshub.documents
# GROUP BY HOUR(receiveddate)
# ORDER BY COUNT(HOUR(receiveddate)) ASC
# LIMIT 1;
