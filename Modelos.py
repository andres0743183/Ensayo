# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 03:19:24 2018

@author: andre
"""


#♦import functools
#import matplotlib.pyplot as plt
import Indicadores
import pandas as pd
#import pickle 
#import numpy as np
import sklearn as sk
#from sklearn.linear_model import LogisticRegression
#from sklearn import metrics
from sklearn import svm
from sklearn.cross_validation import StratifiedKFold
#from time import time
from sklearn import preprocessing

N1=100000
N2=80000

def Modelo1(INDICA,coin):
    datos=pd.read_csv('D:/Repositorio/Python/Coin TFM/ChartData/'+coin+'.csv')
    datos=datos.iloc[(len(datos)-N1):(len(datos)-N2),:]
    Ind=Indicadores.Indicadores(datos=datos,IND=INDICA)
    Obj=Indicadores.Objetivo(datos)
    scaler = preprocessing.StandardScaler().fit(Ind)
    Ind=scaler.transform(Ind) 
    kpliegues = StratifiedKFold(y=Obj, n_folds=10)
    SS=[];BS=[];SB=[];BB=[];Salida=pd.DataFrame();S=[];B=[]
    for train_index, test_index in kpliegues:
        modelo_lr = sk.linear_model.LogisticRegression()
        modelo_lr.fit(X=Ind[train_index,],y=Obj[train_index])
        predicion = modelo_lr.predict(Ind[test_index,])
        #pre_prob = modelo_lr.predict_proba(Ind[test_index,])
        Tabla=pd.crosstab(Obj[test_index], predicion, rownames=['REAL'], colnames=['PREDICCION'])
        S.append(pd.value_counts(Obj).iloc[0])
        B.append(pd.value_counts(Obj).iloc[1])
        SS.append(Tabla.iloc[0,0])
        BS.append(Tabla.iloc[0,1])
        SB.append(Tabla.iloc[1,0])
        BB.append(Tabla.iloc[1,1])
        #print(pd.crosstab(Obj[test_index], predicion, rownames=['REAL'], colnames=['PREDICCION']))
    Salida=Salida.append(pd.DataFrame({"Modelo":1,"COIN":coin,
                                       "CLAVE":INDICA,
                                       "Sell":S,
                                       "Buy":B,
                                       "SS":SS,
                                       "SB":SB,
                                       "BS":BS,
                                       "BB":BB}))
    return Salida


def Modelo2(INDICA,coin):
    datos=pd.read_csv('D:/Repositorio/Python/Coin TFM/ChartData/'+coin+'.csv')
    datos=datos.iloc[(len(datos)-N1):(len(datos)-N2),:]
    Ind=Indicadores.Indicadores(datos=datos,IND=INDICA)
    Obj=Indicadores.Objetivo(datos)
    scaler = preprocessing.StandardScaler().fit(Ind)
    Ind=scaler.transform(Ind) 
    kpliegues = StratifiedKFold(y=Obj, n_folds=10)
    SS=[];BS=[];SB=[];BB=[];Salida=pd.DataFrame();S=[];B=[]
    for train_index, test_index in kpliegues:
        #☻modelo_lr = sk.linear_model.LogisticRegression()
        #modelo_lr.fit(X=Ind[train_index,],y=Obj[train_index])
        modelo_lr= svm.SVC(kernel='linear')
        modelo_lr.fit(X=Ind[train_index,],y=Obj[train_index])
        predicion = modelo_lr.predict(Ind[test_index,])
        #pre_prob = modelo_lr.predict_proba(Ind[test_index,])
        Tabla=pd.crosstab(Obj[test_index], predicion, rownames=['REAL'], colnames=['PREDICCION'])
        S.append(pd.value_counts(Obj).iloc[0])
        B.append(pd.value_counts(Obj).iloc[1])
        SS.append(Tabla.iloc[0,0])
        BS.append(Tabla.iloc[0,1])
        SB.append(Tabla.iloc[1,0])
        BB.append(Tabla.iloc[1,1])
        #print(pd.crosstab(Obj[test_index], predicion, rownames=['REAL'], colnames=['PREDICCION']))
    Salida=Salida.append(pd.DataFrame({"Modelo":2,"COIN":coin,
                                       "CLAVE":INDICA,
                                       "Sell":S,
                                       "Buy":B,
                                       "SS":SS,
                                       "SB":SB,
                                       "BS":BS,
                                       "BB":BB}))
    return Salida


def Modelo3(INDICA,coin):
    datos=pd.read_csv('D:/Repositorio/Python/Coin TFM/ChartData/'+coin+'.csv')
    datos=datos.iloc[(len(datos)-N1):(len(datos)-N2),:]
    Ind=Indicadores.Indicadores(datos=datos,IND=INDICA)
    Obj=Indicadores.Objetivo(datos)
    scaler = preprocessing.StandardScaler().fit(Ind)
    Ind=scaler.transform(Ind) 
    kpliegues = StratifiedKFold(y=Obj, n_folds=10)
    SS=[];BS=[];SB=[];BB=[];Salida=pd.DataFrame();S=[];B=[]
    for train_index, test_index in kpliegues:
        #☻modelo_lr = sk.linear_model.LogisticRegression()
        #modelo_lr.fit(X=Ind[train_index,],y=Obj[train_index])
        modelo_lr= svm.SVC(kernel='rbf')
        modelo_lr.fit(X=Ind[train_index,],y=Obj[train_index])
        predicion = modelo_lr.predict(Ind[test_index,])
        #pre_prob = modelo_lr.predict_proba(Ind[test_index,])
        Tabla=pd.crosstab(Obj[test_index], predicion, rownames=['REAL'], colnames=['PREDICCION'])
        S.append(pd.value_counts(Obj).iloc[0])
        B.append(pd.value_counts(Obj).iloc[1])
        SS.append(Tabla.iloc[0,0])
        BS.append(Tabla.iloc[0,1])
        SB.append(Tabla.iloc[1,0])
        BB.append(Tabla.iloc[1,1])
        #print(pd.crosstab(Obj[test_index], predicion, rownames=['REAL'], colnames=['PREDICCION']))
    Salida=Salida.append(pd.DataFrame({"Modelo":3,"COIN":coin,
                                       "CLAVE":INDICA,
                                       "Sell":S,
                                       "Buy":B,
                                       "SS":SS,
                                       "SB":SB,
                                       "BS":BS,
                                       "BB":BB}))
    return Salida



def Modelo4(INDICA,coin):
    datos=pd.read_csv('D:/Repositorio/Python/Coin TFM/ChartData/'+coin+'.csv')
    datos=datos.iloc[(len(datos)-N1):(len(datos)-N2):]
    Ind=Indicadores.Indicadores(datos=datos,IND=INDICA)
    Obj=Indicadores.Objetivo(datos)
    scaler = preprocessing.StandardScaler().fit(Ind)
    Ind=scaler.transform(Ind) 
    kpliegues = StratifiedKFold(y=Obj, n_folds=10)
    SS=[];BS=[];SB=[];BB=[];Salida=pd.DataFrame();S=[];B=[]
    for train_index, test_index in kpliegues:
        #☻modelo_lr = sk.linear_model.LogisticRegression()
        #modelo_lr.fit(X=Ind[train_index,],y=Obj[train_index])
        modelo_lr= svm.SVC(kernel='poly')
        modelo_lr.fit(X=Ind[train_index,],y=Obj[train_index])
        predicion = modelo_lr.predict(Ind[test_index,])
        #pre_prob = modelo_lr.predict_proba(Ind[test_index,])
        Tabla=pd.crosstab(Obj[test_index], predicion, rownames=['REAL'], colnames=['PREDICCION'])
        S.append(pd.value_counts(Obj).iloc[0])
        B.append(pd.value_counts(Obj).iloc[1])
        SS.append(Tabla.iloc[0,0])
        BS.append(Tabla.iloc[0,1])
        SB.append(Tabla.iloc[1,0])
        BB.append(Tabla.iloc[1,1])
        #print(pd.crosstab(Obj[test_index], predicion, rownames=['REAL'], colnames=['PREDICCION']))
    Salida=Salida.append(pd.DataFrame({"Modelo":4,
                                        "COIN":coin,
                                       "CLAVE":INDICA,
                                       "Sell":S,
                                       "Buy":B,
                                       "SS":SS,
                                       "SB":SB,
                                       "BS":BS,
                                       "BB":BB}))
    return Salida

from sklearn.ensemble import RandomForestClassifier

def Modelo5(INDICA,coin):
    datos=pd.read_csv('D:/Repositorio/Python/Coin TFM/ChartData/'+coin+'.csv')
    datos=datos.iloc[(len(datos)-N1):(len(datos)-N2):]
    Ind=Indicadores.Indicadores(datos=datos,IND=INDICA)
    Obj=Indicadores.Objetivo(datos)
    scaler = preprocessing.StandardScaler().fit(Ind)
    Ind=scaler.transform(Ind) 
    kpliegues = StratifiedKFold(y=Obj, n_folds=10)
    SS=[];BS=[];SB=[];BB=[];Salida=pd.DataFrame();S=[];B=[]
    for train_index, test_index in kpliegues:
        #☻modelo_lr = sk.linear_model.LogisticRegression()
        #modelo_lr.fit(X=Ind[train_index,],y=Obj[train_index])
        modelo_lr= RandomForestClassifier()
        modelo_lr.fit(X=Ind[train_index,],y=Obj[train_index])
        predicion = modelo_lr.predict(Ind[test_index,])
        #pre_prob = modelo_lr.predict_proba(Ind[test_index,])
        Tabla=pd.crosstab(Obj[test_index], predicion, rownames=['REAL'], colnames=['PREDICCION'])
        S.append(pd.value_counts(Obj).iloc[0])
        B.append(pd.value_counts(Obj).iloc[1])
        SS.append(Tabla.iloc[0,0])
        BS.append(Tabla.iloc[0,1])
        SB.append(Tabla.iloc[1,0])
        BB.append(Tabla.iloc[1,1])
        #print(pd.crosstab(Obj[test_index], predicion, rownames=['REAL'], colnames=['PREDICCION']))
    Salida=Salida.append(pd.DataFrame({"Modelo":5,
                                        "COIN":coin,
                                       "CLAVE":INDICA,
                                       "Sell":S,
                                       "Buy":B,
                                       "SS":SS,
                                       "SB":SB,
                                       "BS":BS,
                                       "BB":BB}))
    return Salida