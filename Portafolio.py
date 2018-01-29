#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 01:50:29 2018

@author: andres
"""

""
import pandas as pd
import numpy as np
#import sklearn as sk
import pickle 

#Funcion para guardar los  modelos creados 
def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#save_object(coin, 'ChartData/coin.pkl')

with open('ChartData/coin.pkl', 'rb') as input:
    coin = pickle.load(input)
    print(coin) 

#import talib
#from zigzag import *

for i in coin:
    np.random.randint(0,2,100)
    datos=pd.read_csv('ChartData/'+i+'.csv')
    rt=datos[datos['date']>=1483228800]['close'].pct_change()
    movimiento=(rt>0)*1
    #shift(1)
    analisis=pd.DataFrame({'movimiento':movimiento,
                       'rt1':rt.shift(1),'rt2':rt.shift(2),'rt3':rt.shift(3),'rt4':rt.shift(4),'rt5':rt.shift(5)})

#    print(rt.tail())
#    print(analisis.tail())
    analisis=analisis.dropna(how='any')
    analisis=analisis.as_matrix()
    data = np.matrix(analisis)
# CREA dataset TRAIN y TEST
#---------------------------------------------------------------------------------------------
# MODELO
#---------------------------------------------------------------------------------------------
# PREDICCION
#---------------------------------------------------------------------------------------------
    with open('Model/'+i+'_M.model', 'rb') as input:
        modelo_lr = pickle.load(input)
    print(coin) 
    
    predicion = modelo_lr.predict(data[:,1:])
    print(predicion.sum())
 

# METRICAS
#---------------------------------------------------------------------------------------------





# sample usage

#pickle.load('company1.pkl')


#with open('company1.pkl', 'rb') as input:
#    modelo_lr = pickle.load(input)
 #   print(modelo_lr) 





