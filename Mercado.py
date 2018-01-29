# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:57:37 2017

@author: Andres
"""

##Simulacion del mercado
#import PoloniexAPI as polo
import pandas as pd
import numpy as np
#P=polo.Poloniex("","")
#Tiker=P.returnTicker()
#for i in range(1, 20, 3):
#    print(i)

#datos=pd.DataFrame(P.returnMarketTradeHistory("BTC_DASH","01/11/2017","02/11/2017"))
#data = pd.DataFrame(P.returnMarketTradeHistory("BTC_DASH","01/11/2017","02/11/2017"))
#BTC_DASH=pd.DataFrame(P.returnChartData("BTC_DASH"))
#BTC_DASH.to_csv(path_or_buf="BTC_DASH.csv")

#BTC_DASH=pd.read_csv(filepath_or_buffer ="BTC_DASH.csv",index_col=0)

def Mercado(Datos,operacion):
    close=Datos["close"]
    date=Datos["date"]
    Fecha=np.float()
    Apertura=0;Estado=0
    #operacion=np.random.choice([0,1],len(close))
    PG=[];GN=[];Invercion=1
    Fee=[];FA=[];FC=[];PC=[];PV=[]
    for w in range(1,len(close)):
        if operacion[w-1] ==0 and operacion[w] ==1 and Estado==0:
            Apertura=close[w-1]
            Fecha=date[w-1]
            Estado=1   
        if operacion[w-1] ==1 and operacion[w]==0 and Estado==1:
            PG.append((Apertura-close[w-1])/Apertura)
            Fee.append(2*Invercion*0.0025)
            FA.append(Fecha)
            FC.append(date[w-1])
            PC.append(Apertura)
            PV.append(close[w-1])        
            Apertura=0
            GN.append(Invercion*(PG[-1])-Fee[-1])
            Estado=0    
            
    Salida=pd.DataFrame({"FA":FA,"FC":FC,"PC":PC,"PV":PV,"Fee":Fee,"GN":GN})
    return Salida
 
   
    
   
#print(BTC_DASH.head(10))

#plt.plot(close)
#plt.show()


