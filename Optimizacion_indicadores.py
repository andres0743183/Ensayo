# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:30:56 2018

@author: andre
"""


#♦import functools

import Modelos
#import matplotlib.pyplot as plt
#import Indicadores
import pandas as pd
import pickle 
import numpy as np
#import sklearn as sk
#from sklearn.linear_model import LogisticRegression
#from sklearn import metrics
#from sklearn import datasets, svm
#from sklearn.cross_validation import StratifiedKFold
from time import time
#from sklearn import preprocessing


with open('D:/Repositorio/Python/Coin TFM/ChartData/coin.pkl', 'rb') as input:
    coin = pickle.load(input)
     

Resultado=pd.DataFrame()
Resultado1=pd.DataFrame()
Resultado2=pd.DataFrame()
Resultado3=pd.DataFrame()
Resultado4=pd.DataFrame()
Resultado5=pd.DataFrame()

for i in range(0,1):
      
    Indicador=''
    for h in range(0,131):
        #Indicador=Indicador+np.random.choice(['0','1'])
        Indicador=Indicador+np.random.choice(['1'])
    #print(h)
    
    tiempo_inicial = time()  
    Resultado1=Resultado1.append(Modelos.Modelo1(Indicador,coin[2]))
    tiempo_final = time() 
    print('El tiempo del modelo 1 en ejecucion fue: ',str(tiempo_final-tiempo_inicial))
    tiempo_inicial = time() 
    Resultado2=Resultado2.append(Modelos.Modelo2(Indicador,coin[2]))
    tiempo_final = time() 
    print('El tiempo del modelo 2 en ejecucion fue: ',str(tiempo_final-tiempo_inicial))
    tiempo_inicial = time() 
    Resultado3=Resultado3.append(Modelos.Modelo3(Indicador,coin[2]))
    tiempo_final = time() 
    print('El tiempo del modelo 3 en ejecucion fue: ',str(tiempo_final-tiempo_inicial))
    tiempo_inicial = time() 
    Resultado4=Resultado4.append(Modelos.Modelo4(Indicador,coin[2]))
    tiempo_final = time() 
    print('El tiempo del modelo 4 en ejecucion fue: ',str(tiempo_final-tiempo_inicial))
    tiempo_inicial = time() 
    Resultado5=Resultado5.append(Modelos.Modelo5(Indicador,coin[2]))
    tiempo_final = time() 
    print('El tiempo del modelo 5 en ejecucion fue: ',str(tiempo_final-tiempo_inicial))

Resultado=Resultado.append(Resultado1)
Resultado=Resultado.append(Resultado2)
Resultado=Resultado.append(Resultado3)
Resultado=Resultado.append(Resultado4)
Resultado=Resultado.append(Resultado5)
Resultado["Exito"]=(Resultado['BB']+Resultado['SS'])/(Resultado['SB']+Resultado['BB']+Resultado['SS']+Resultado['BS'])

Resultado.boxplot(column="Exito",by=['Modelo','COIN'])
Resultado.to_csv("D:/Repositorio/Python/Coin TFM/Todos_Modelos.csv")
#plt.boxplot(Resultado["Exito"],by=Resultado['Modelo'])    


