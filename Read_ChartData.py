# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 07:01:49 2018

@author: Andres
"""

import pandas as pd
import matplotlib.pyplot as plt



datos=pd.read_csv('D:/Repositorio/Python/Coin TFM/ChartData/BTC_DGB.csv')

rt=datos[datos['date']>=1483228800]



#variacion=datos['close'] / datos['close'].shift(1) - 1
#print(cierre.tail())
#print(rt.tail())
#print(variacion.tail())

#plt.plot(datos['close'])
#plt.show()

#datos.tal
#datos.asfreq('M', method='ffill')


