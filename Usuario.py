
import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="elchinodragonball", port="3307")
    mycursor = mydb.cursor()

    mycursor.execute("USE bearcareful")
    mycursor.execute("SHOW TABLES")

    for i in mycursor:
        print(i)

    mycursor.execute("SELECT ")
except:
    print("No se pudo conectar con la base de datos")