import mysql.connector
from mysql.connector import errorcode
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from pandas import DataFrame
import datetime as dt


def con(id):
    global data, fecha

    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="elchinodragonball", port="3307")
        mycursor = mydb.cursor()

        mycursor.execute("USE bearcareful")

        select = f"SELECT fec, res FROM mtest WHERE id_usu = {id}"
        mycursor.execute(select)

        myresult = mycursor.fetchall()

        data = []
        fecha = []

        for row in myresult:
            fecha.append(row[0])
            data.append(int(row[1]))

        #print(data)
        #print(year)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error con el usuario o password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)

    finally:
        print("Se cerró la conexión a la base de datos")
        mycursor.close()  # Cerrar el cursor
        mydb.close()  # Cerrar la conexión

    #return data, fecha

#def findUsuario():

def regresionTest():
    fechaDf = pd.to_datetime(fecha)
    print(fechaDf)
    fechaDf = fechaDf.map(dt.datetime.toordinal)
    X = np.array(fechaDf)
    y = np.array(DataFrame(data, columns=['puntuacion']))
    print(X)
    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
    X_train = X_train.reshape([X_train.shape[0], 1])
    X_test = X_test.reshape([X_test.shape[0], 1])

    lr = linear_model.LinearRegression()
    lr.fit(X_train, y_train)

    Y_pred = lr.predict(X_test)

    fechaDf = fechaDf.map(dt.datetime.fromordinal)
    X = np.array(fechaDf)

    fig = plt.figure(figsize=(9, 5.5))
    plt.title('Historico test')
    plt.ylabel('Puntuacion')
    plt.xlabel('Fecha')
    plt.scatter(X, y, c="#2EC5CE")
    #plt.plot(X_test, Y_pred, c="#8C30F5", linewidth=3)

    html_str = mpld3.fig_to_html(fig)
    Html_file = open("Usuario.html", "w")
    Html_file.write(html_str)
    Html_file.close()
    plt.show()


#print(list(con(1)))
con(1)
regresionTest()
#toDF(list(con(1)))
#print(data)
#print(fecha)
