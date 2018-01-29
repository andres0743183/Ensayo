# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 02:08:47 2018

@author: andre
"""

import pandas as pd
import numpy as np
import sklearn as sk
import talib
import pickle 

#Funcion para guardar los  modelos creados 
def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#save_object(coin, 'ChartData/coin.pkl')

with open('D:/Repositorio/Python/Coin TFM/ChartData/coin.pkl', 'rb') as input:
    coin = pickle.load(input)
    print(coin) 


datos=pd.read_csv('D:/Repositorio/Python/Coin TFM/ChartData/'+coin[1]+'.csv')

rt=datos[datos['date']>=1483228800]['close'].pct_change()


X=datos.iloc[(len(datos)-10):len(datos),:]['close'].as_matrix()

talib.MA(X,timeperiod=7)









