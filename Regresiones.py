import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

#lr = linear_model.LinearRegression()

df_main = pd.read_csv("datadepression.csv", header=0)
df_main.columns = ["pais", "year", "depr"]
print(df_main)

#Canadá
df_CAN = df_main.query("pais=='CAN'")
X = df_CAN.year
Y_CAN = df_CAN.depr
Y_CAN_pred = 20.40 - (0.008171*X)
plt.scatter(X, Y_CAN)
plt.plot(X, Y_CAN_pred, color="red", linewidth=3)
plt.show()
print(df_CAN)

#USA
df_USA = df_main.query("pais=='USA'")
Y_USA = df_USA.depr
Y_USA_pred = -7.54 + (0.00613*X)
plt.scatter(X, Y_USA)
plt.plot(X, Y_USA_pred, color="red", linewidth=3)
plt.show()
print(df_USA)

#MEXICO
df_MEX = df_main.query("pais=='MEX'")
Y_MEX = df_MEX.depr
Y_MEX_pred = -5.30 + (0.004014*X)
plt.scatter(X, Y_MEX)
plt.plot(X, Y_MEX_pred, color="red", linewidth=3)
plt.show()
print(df_MEX)
