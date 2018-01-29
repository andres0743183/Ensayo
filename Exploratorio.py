#########################
##Analisis descriptivo
########################


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import zigzag 
import pickle 
import sklearn as sk
import talib

## Creacion de grafico pivote

def plot_pivots(X, pivots):
    plt.xlim(0, len(X))
    plt.ylim(X.min()*0.99, X.max()*1.01)
    plt.plot(np.arange(len(X)), X, 'k:', alpha=0.5)
    plt.plot(np.arange(len(X))[pivots != 0], X[pivots != 0], 'k-')
    plt.scatter(np.arange(len(X))[pivots == 1], X[pivots == 1], color='g')
    plt.scatter(np.arange(len(X))[pivots == -1], X[pivots == -1], color='r')

## Lectura de archivo de coins

with open('D:/Repositorio/Python/Coin TFM/ChartData/coin.pkl', 'rb') as input:
    coin = pickle.load(input)
    print(coin) 

## Grafico  de pivotes para identificar los objetivos
datos=pd.read_csv('D:/Repositorio/Python/Coin TFM/ChartData/'+coin[5]+'.csv')
#rt=datos[datos['date']>=1483228800]['close'].pct_change()
#movimiento=(rt>0)*1

X=datos.iloc[(len(datos)-200):len(datos),:]['close'].as_matrix()
pivots=zigzag.peak_valley_pivots(X, 0.03, -0.03)
plot_pivots(X,pivots)


