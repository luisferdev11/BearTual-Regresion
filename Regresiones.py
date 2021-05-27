import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
#from Usuario import *

df_main = pd.read_csv("datadepression.csv", header=0)
df_main.columns = ["pais", "year", "depr"]

print(df_main)

def regresion(df_main, pais):
    df = df_main.query(f"pais=='{pais}'")
    X = np.array(df.year.values)
    y = np.array(df.depr)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
    X_train = X_train.reshape([X_train.shape[0], 1])
    X_test = X_test.reshape([X_test.shape[0], 1])

    lr = linear_model.LinearRegression()
    lr.fit(X_train, y_train)

    Y_pred = lr.predict(X_test)

    plt.scatter(X, y)
    plt.plot(X_test, Y_pred, color="red", linewidth=3)
    plt.show()
    print(df)

regresion(df_main, "CAN")
regresion(df_main, "USA")
regresion(df_main, "MEX")

"""
#CANADA
df_CAN = df_main.query("pais=='CAN'")
X = np.array(df_CAN.year.values)
Y_CAN = np.array(df_CAN.depr)

# Y_CAN_pred = 20.40 - (0.008171*X)
X_train, X_test, y_train, y_test = train_test_split(X, Y_CAN, test_size=0.4, random_state=42)

X_train = X_train.reshape([X_train.shape[0],1])
X_test = X_test.reshape([X_test.shape[0],1])

#Entrenar el modelo
lr_CAN = linear_model.LinearRegression()
lr_CAN.fit(X_train, y_train)

#Prediccion
Y_CAN_pred = lr_CAN.predict(X_test)

plt.scatter(X, Y_CAN)
plt.plot(X_test, Y_CAN_pred, color="red", linewidth=3)
plt.show()



#USA
df_USA = df_main.query("pais=='USA'")
Y_USA = np.array(df_USA.depr)

X_train, X_test, y_train, y_test = train_test_split(X, Y_USA, test_size=0.4, random_state=42)

X_train = X_train.reshape([X_train.shape[0],1])
X_test = X_test.reshape([X_test.shape[0],1])

#Y_USA_pred = -7.54 + (0.00613*X)
lr_USA = linear_model.LinearRegression()
lr_USA.fit(X_train, y_train)

Y_USA_pred = lr_USA.predict(X_test)
plt.scatter(X, Y_USA)
plt.plot(X_test, Y_USA_pred, color="red", linewidth=3)
plt.show()
print(df_USA)



#MEXICO
df_MEX = df_main.query("pais=='MEX'")
Y_MEX = np.array(df_MEX.depr)

X_train, X_test, y_train, y_test = train_test_split(X, Y_MEX, test_size=0.4, random_state=42)

X_train = X_train.reshape([X_train.shape[0],1])
X_test = X_test.reshape([X_test.shape[0],1])

#Y_MEX_pred = -5.30 + (0.004014*X)
lr_MEX = linear_model.LinearRegression()
lr_MEX.fit(X_train, y_train)

Y_MEX_pred = lr_MEX.predict(X_test)

plt.scatter(X, Y_MEX)
plt.plot(X_test, Y_MEX_pred, color="red", linewidth=3)
plt.show()
print(df_MEX)
"""


