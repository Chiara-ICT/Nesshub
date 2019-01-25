import mysql.connector
import scripts.mysql_parameters as p

mydb = mysql.connector.connect(
    host = p.DB_HOST,
    port = p.DB_PORT,
    user = p.DB_USER,
    passwd = p.DB_PASSWORD,
    database = p.DB_PUBLIC
)

mycursor = mydb.cursor()
mycursor.execute("set sql_mode = (select replace (@@sql_mode, 'ONLY_FULL_GROUP_BY', ''))")

sql = """SELECT id, numerofattura,  stato_sdi
         FROM fatture_ripetute order by numerofattura"""
mycursor.execute(sql)
myresult = mycursor.fetchall()
print('affected rows', len(myresult),'\n')

result = list()
for index, x in enumerate(myresult):
    if x[2] != 'NOTIFICA_SCARTO':
        result.append(x)
        print(x)
    elif index+1 < len(myresult):
        if myresult[index + 1][1] == myresult[index][1]:
            continue
    elif  myresult[index - 1][1] == myresult[index][1]:
        if  myresult[index - 1][2] != 'NOTIFICA_SCARTO':
            continue
        print(x)
        result.append(x)
print('\n', result,'\n', len(result))

# We selected the good receipts, now we need to create a .csv file to write them down.
# Let's start opening the file in which we will insert the result.

with open('output.csv', 'w') as f:      # open creates a file (f is the name of it, the parameter "w" stands for write)
    lines =[]
    lines.append("id,numerofattura,stato_sdi\n")
    lines.append( ','.join([str(x) for x in result]))
    print(lines)
    f.writelines(lines)

