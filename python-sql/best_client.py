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

mycursor.execute("SELECT sendervat, COUNT(sendervat)\
                 FROM nesshub.documents\
                 GROUP BY sendervat \
                 ORDER BY COUNT(uuid) DESC ")
sendervat = mycursor.fetchall()

mycursor.execute("""SELECT recipientvat, COUNT(uuid)
                FROM nesshub.documents
                GROUP BY recipientvat
                ORDER BY COUNT(uuid) DESC""")

recipientvat = mycursor.fetchall()

# for x in sendervat:
#     print(x)
# print("\n")
# for x in recipientvat:
#     print(x)
# "ciao{obj.a}a{obj.b}d{obj.a}".format(obj={'a':1,'b':2})

for x in sendervat:
    for y in recipientvat:
        if x[0] == y[0]:
           # print(x)
            x = (x[0],x[1]+y[1],"sent {}+ received {}".format(x[1],y[1]))
            #x[1] += y[1]
    print(x)
        # else:
        #     print(x)
