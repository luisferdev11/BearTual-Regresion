import pandas as pd
import matplotlib.pyplot as plt

historico = pd.read_csv('historico.csv')

resultados = historico["Resultado"].tolist()
fechas = historico["Fecha"].tolist()
plt.plot(fechas, resultados, 'o-')
plt.xticks(fechas, rotation='vertical')
plt.ylim(0, 64)
plt.xlabel("Fecha")
plt.ylabel("Resultado")
plt.show()