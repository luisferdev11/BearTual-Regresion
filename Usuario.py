import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import mysql.connector

class Usuario:
    def __init__(self, fecha, puntuacion):
        self._fecha = fecha
        self._puntuacion = puntuacion

mydb = mysql.connector.connect(host="localhost", user="root", passwd="elchinodragonball", port="3307")
mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)