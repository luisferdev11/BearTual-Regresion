import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import mpld3
# from Usuario import *

def regresion(df_main, pais):
    df = df_main.query(f"pais=='{pais}'")
    X = np.array(df.year)
    y = np.array(df.depr)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=42)
    X_train = X_train.reshape([X_train.shape[0], 1])
    X_test = X_test.reshape([X_test.shape[0], 1])

    lr = linear_model.LinearRegression()
    lr.fit(X_train, y_train)

    Y_pred = lr.predict(X_test)

    #esta linea se sustituira por elementos del html
    graf = str(input(f"Desea graficar para {pais}?: "))
    if graf in ("S, s"):
        graficar(X,y, X_test, Y_pred, lr, pais)
    else:
        predecir(lr)

def graficar(X, y, X_test, Y_pred, lr, pais):
    fig = plt.figure(figsize=(6.4, 4.8))
    plt.title(f'Porcentaje de personas con depresión en {pais}')
    plt.ylabel('Porcentaje')
    plt.xlabel('Año')
    plt.scatter(X, y, c="#2EC5CE")
    plt.plot(X_test, Y_pred, c="#8C30F5", linewidth=3)

    # esta linea se sustituira por elementos del html
    pred = str(input(f"Desea predecir para {pais}?: "))
    if pred in ("S, s"):
        predecir(lr)
        plt.scatter(entrada, prediccion, c="#FE9A22")

        html_str = mpld3.fig_to_html(fig)
        Html_file = open(f"{pais}_pred.html", "w")
        Html_file.write(html_str)
        Html_file.close()
        plt.show()
    else:
        html_str = mpld3.fig_to_html(fig)
        Html_file = open(f"{pais}.html", "w")
        Html_file.write(html_str)
        Html_file.close()
        plt.show()

def predecir(lr):
    try:
        global entrada, prediccion
        entrada = np.array([0,])
        prediccion = None
        while (entrada[0] < 2021) or (entrada[0] > 2030):
            entrada[0] = input("Escriba el valor a predecir: ")
            entrada = entrada.reshape([entrada.shape[0], 1])
            prediccion = lr.predict(entrada)
        print(prediccion)
    except:
        print("Valor inválido")


columnas = ("pais", "year", "depr")

df_main = pd.read_csv("datadepression.csv", header=0)
df_main.columns = columnas
print(df_main)

paises = ("CAN", "USA", "MEX")

for pais in paises:
    regresion(df_main, pais)
