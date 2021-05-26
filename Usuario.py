
import mysql.connector

class Usuario:
    def __init__(self, fecha, puntuacion):
        self.__fecha = fecha
        self.__puntuacion = puntuacion


class ConexionBD:
    def conectar(self):
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="elchinodragonball", port="3307")
            mycursor = mydb.cursor()

            mycursor.execute("show databases")

            for i in mycursor:
                print(i)
        except:
            print("No se pudo conectar con la base de datos")


class AccionesUsuario:
    #Obtener nivel de depre
    #Insertar esos datos en la BD
    #Regresion con los datos
    #Plot graficas

    pass