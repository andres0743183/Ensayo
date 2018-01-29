# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 03:18:17 2018

@author: Andres
"""
import pandas as pd
import numpy as np
import sklearn as sk
import pickle 

#Funcion para guardar los  modelos creados 
def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#save_object(coin, 'ChartData/coin.pkl')

with open('D:/Repositorio/Python/Coin TFM/ChartData/coin.pkl', 'rb') as input:
    coin = pickle.load(input)
    print(coin) 

#import talib
#from zigzag import *

for i in coin:
    print(i)

np.random.randint(0,2,100)

datos=pd.read_csv('D:/Repositorio/Python/Coin TFM/ChartData/BTC_DGB.csv')
rt=datos[datos['date']>=1483228800]['close'].pct_change()
movimiento=(rt>0)*1
#shift(1)
analisis=pd.DataFrame({'movimiento':movimiento,
                       'rt1':rt.shift(1),'rt2':rt.shift(2),'rt3':rt.shift(3),'rt4':rt.shift(4),'rt5':rt.shift(5)})
print(rt.tail())
print(analisis.tail())
analisis=analisis.dropna(how='any')
analisis=analisis.as_matrix()
data = np.matrix(analisis)

# CREA dataset TRAIN y TEST
#---------------------------------------------------------------------------------------------
np.random.seed(123)
m_train    = np.random.rand(len(data)) < 0.5
data_train = data[m_train,]
data_test  = data[~m_train,]


# CLASE
#---------------------------------------------------------------------------------------------
clase_train = data_train[:,0]
clase_train = clase_train.A1 #convierte de matriz a vector 
clase_test  = data_test[:,0]
clase_test  = clase_test.A1 #convierte de matriz a vector 

##Normalizacion

#Normalizacion=sk.preprocessing.scale(data_train[:,1:])

# MODELO
#---------------------------------------------------------------------------------------------
modelo_lr = sk.linear_model.LogisticRegression()
modelo_lr.fit(X=data_train[:,1:],y=clase_train)


# PREDICCION
#---------------------------------------------------------------------------------------------
predicion = modelo_lr.predict(data_test[:,1:])
pre_prob = modelo_lr.predict_proba(data_test[:,1:])


# METRICAS
#---------------------------------------------------------------------------------------------
print(sk.metrics.classification_report(y_true=clase_test, y_pred=predicion))
print(pd.crosstab(data_test[:,0].A1, predicion, rownames=['REAL'], colnames=['PREDICCION']))


'Model/'+coin[1]+'_M.model'


# sample usage
#save_object(modelo_lr, 'Model/company1.pkl')
#pickle.load('company1.pkl')


#with open('company1.pkl', 'rb') as input:
#    modelo_lr = pickle.load(input)
 #   print(modelo_lr) 





