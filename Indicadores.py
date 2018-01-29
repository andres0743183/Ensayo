# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:59:24 2018

@author: andre
"""
import talib
import numpy as np
import zigzag
#matriz =  numpy.matrix(numpy.empty(shape=(0,len(datos)), dtype='float64'))
#IND='110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
#datos=datos.iloc[(len(datos)-10000):len(datos),:]
#Ind=Indicadores(datos,IND)
#Ind.shape
def Objetivo(datos,cambio=0.03):
    close=datos["close"].as_matrix()
    pivots=zigzag.peak_valley_pivots(close, cambio, cambio*-1)
    movimiento=zigzag.pivots_to_modes(pivots)
    return np.roll(movimiento, 1)[100:]


def Indicadores(datos,IND,shift=0):
 
    high=datos["high"].as_matrix()
    low=datos["low"].as_matrix()
    close=datos["close"].as_matrix()
    rt=datos["close"].pct_change()
    volume=datos["volume"].as_matrix()
    apertura=datos["open"].as_matrix()
    
    matriz =  np.matrix(np.empty(shape=(len(datos),0), dtype='float64'))
    matriz = np.concatenate((matriz,np.matrix(rt.shift(1)).T), axis=1) 
    matriz = np.concatenate((matriz,np.matrix(rt.shift(2)).T), axis=1) 
    matriz = np.concatenate((matriz,np.matrix(rt.shift(3)).T), axis=1) 
    matriz = np.concatenate((matriz,np.matrix(rt.shift(4)).T), axis=1) 
    matriz = np.concatenate((matriz,np.matrix(rt.shift(5)).T), axis=1)
    matriz = np.concatenate((matriz,np.matrix(rt.shift(6)).T), axis=1) 
    matriz = np.concatenate((matriz,np.matrix(rt.shift(7)).T), axis=1) 
    matriz = np.concatenate((matriz,np.matrix(rt.shift(8)).T), axis=1) 
    matriz = np.concatenate((matriz,np.matrix(rt.shift(9)).T), axis=1)
    matriz = np.concatenate((matriz,np.matrix(rt.shift(10)).T), axis=1)
    
    if IND[0]=='1':
        AD=talib.AD(high,low,close,volume)
        AD=np.matrix(np.roll(AD, shift)).T
        matriz = np.concatenate((matriz, AD), axis=1)  
        
    if IND[1]=='1':
        ADOSC=talib.ADOSC(high,low,close,volume,fastperiod=5,slowperiod=10)
        ADOSC= np.matrix(np.roll(ADOSC, shift)).T
        matriz = np.concatenate((matriz, ADOSC), axis=1)
        del ADOSC
    
    if IND[2]=='1':
        ADXR=talib.ADXR(high,low,close,timeperiod=10) 
        ADXR= np.matrix(np.roll(ADXR, shift)).T
        matriz = np.concatenate((matriz, ADXR), axis=1)
        del ADXR
    
    if IND[3]=='1':
        APO=talib.APO(close,fastperiod=5,slowperiod=10)  
        APO= np.matrix(np.roll(APO, shift)).T
        matriz = np.concatenate((matriz, APO), axis=1)
        del APO
    
    if IND[4]=='1':
        AROON=talib.AROON(high,low,timeperiod=10) 
        AROON= np.matrix(np.roll(AROON, shift)).T
        matriz = np.concatenate((matriz, AROON), axis=1)
        del AROON                          
    
    if IND[5]=='1':
        AROONOSC=talib.AROONOSC(high,low,timeperiod=10) 
        AROONOSC= np.matrix(np.roll(AROONOSC, shift)).T
        matriz = np.concatenate((matriz, AROONOSC), axis=1)
        del AROONOSC 
        
    if IND[6]=='1':
        ATR=talib.ATR(high,low,close,timeperiod=10) 
        ATR= np.matrix(np.roll(ATR, shift)).T
        matriz = np.concatenate((matriz, ATR), axis=1)
        del ATR    
    
    if IND[7]=='1':
        AVGPRICE=talib.AVGPRICE(apertura,high,low,close)  
        AVGPRICE= np.matrix(np.roll(AVGPRICE, shift)).T
        matriz = np.concatenate((matriz, AVGPRICE), axis=1)
        del AVGPRICE        
    
    if IND[8]=='1':
        BBANDS=talib.BBANDS(close,timeperiod=10,nbdevdn=10,nbdevup=15) 
        BBANDS= np.matrix(np.roll(BBANDS, shift)).T
        matriz = np.concatenate((matriz, BBANDS), axis=1)
        del BBANDS      
                                             
    #BETA=talib.BETA(close,apertura,timeperiod=10)
    if IND[9]=='1':
        BOP=talib.BOP(apertura,high,low,close)
        BOP= np.matrix(np.roll(BOP, shift)).T
        matriz = np.concatenate((matriz, BOP), axis=1)
        del BOP 
    
    if IND[10]=='1':
        CCI=talib.CCI(high,low,close,timeperiod=10)
        CCI= np.matrix(np.roll(CCI, shift)).T
        matriz = np.concatenate((matriz, CCI), axis=1)
        del CCI 
    
    if IND[11]=='1':
        CDL2CROWS=talib.CDL2CROWS(apertura,high,low,close)  
        CDL2CROWS= np.matrix(np.roll(CDL2CROWS, shift)).T
        matriz = np.concatenate((matriz, CDL2CROWS), axis=1)
        del CDL2CROWS     
    
    if IND[12]=='1':
        CDL3BLACKCROWS=talib.CDL3BLACKCROWS(apertura,high,low,close) 
        CDL3BLACKCROWS= np.matrix(np.roll(CDL3BLACKCROWS, shift)).T
        matriz = np.concatenate((matriz, CDL3BLACKCROWS), axis=1)
        del CDL3BLACKCROWS      
    
    if IND[13]=='1':
        CDL3INSIDE=talib.CDL3INSIDE(apertura,high,low,close) 
        CDL3INSIDE= np.matrix(np.roll(CDL3INSIDE, shift)).T
        matriz = np.concatenate((matriz, CDL3INSIDE), axis=1)
        del CDL3INSIDE                            
    
    if IND[14]=='1':
        CDL3LINESTRIKE=talib.CDL3LINESTRIKE(apertura,high,low,close) 
        CDL3LINESTRIKE= np.matrix(np.roll(CDL3LINESTRIKE, shift)).T
        matriz = np.concatenate((matriz, CDL3LINESTRIKE), axis=1)
        del CDL3LINESTRIKE     

    if IND[15]=='1':
        CDL3OUTSIDE=talib.CDL3OUTSIDE(apertura,high,low,close) 
        CDL3OUTSIDE= np.matrix(np.roll(CDL3OUTSIDE, shift)).T
        matriz = np.concatenate((matriz, CDL3OUTSIDE), axis=1)
        del CDL3OUTSIDE    
          
    if IND[16]=='1':
        CDL3STARSINSOUTH=talib.CDL3STARSINSOUTH(apertura,high,low,close) 
        CDL3STARSINSOUTH= np.matrix(np.roll(CDL3STARSINSOUTH, shift)).T
        matriz = np.concatenate((matriz, CDL3STARSINSOUTH), axis=1)
        del CDL3STARSINSOUTH  
        
    if IND[17]=='1':
        CDL3WHITESOLDIERS=talib.CDL3WHITESOLDIERS(apertura,high,low,close) 
        CDL3WHITESOLDIERS= np.matrix(np.roll(CDL3WHITESOLDIERS, shift)).T
        matriz = np.concatenate((matriz, CDL3WHITESOLDIERS), axis=1)
        del CDL3WHITESOLDIERS         

    if IND[18]=='1':
        CDLADVANCEBLOCK=talib.CDLADVANCEBLOCK(apertura,high,low,close) 
        CDLADVANCEBLOCK= np.matrix(np.roll(CDLADVANCEBLOCK, shift)).T
        matriz = np.concatenate((matriz, CDLADVANCEBLOCK), axis=1)
        del CDLADVANCEBLOCK    

    if IND[19]=='1':
        CDLBELTHOLD=talib.CDLBELTHOLD(apertura,high,low,close) 
        CDLBELTHOLD= np.matrix(np.roll(CDLBELTHOLD, shift)).T
        matriz = np.concatenate((matriz, CDLBELTHOLD), axis=1)
        del CDLBELTHOLD    
 
    if IND[20]=='1':
        CDLBREAKAWAY=talib.CDLBREAKAWAY(apertura,high,low,close) 
        CDLBREAKAWAY= np.matrix(np.roll(CDLBREAKAWAY, shift)).T
        matriz = np.concatenate((matriz, CDLBREAKAWAY), axis=1)
        del CDLBREAKAWAY      
    
    if IND[21]=='1':
        CDLCLOSINGMARUBOZU=talib.CDLCLOSINGMARUBOZU(apertura,high,low,close) 
        CDLCLOSINGMARUBOZU= np.matrix(np.roll(CDLCLOSINGMARUBOZU, shift)).T
        matriz = np.concatenate((matriz, CDLCLOSINGMARUBOZU), axis=1)
        del CDLCLOSINGMARUBOZU      
        
    if IND[22]=='1':
        CDLCONCEALBABYSWALL=talib.CDLCONCEALBABYSWALL(apertura,high,low,close) 
        CDLCONCEALBABYSWALL= np.matrix(np.roll(CDLCONCEALBABYSWALL, shift)).T
        matriz = np.concatenate((matriz, CDLCONCEALBABYSWALL), axis=1)
        del CDLCONCEALBABYSWALL      
            
    if IND[23]=='1':
        CDLCOUNTERATTACK=talib.CDLCOUNTERATTACK(apertura,high,low,close) 
        CDLCOUNTERATTACK= np.matrix(np.roll(CDLCOUNTERATTACK, shift)).T
        matriz = np.concatenate((matriz, CDLCOUNTERATTACK), axis=1)
        del CDLCOUNTERATTACK  
        
    if IND[24]=='1':
        CDLDARKCLOUDCOVER=talib.CDLDARKCLOUDCOVER(apertura,high,low,close) 
        CDLDARKCLOUDCOVER= np.matrix(np.roll(CDLDARKCLOUDCOVER, shift)).T
        matriz = np.concatenate((matriz, CDLDARKCLOUDCOVER), axis=1)
        del CDLDARKCLOUDCOVER      
                         
    if IND[25]=='1':
        CDLDOJI=talib.CDLDOJI(apertura,high,low,close) 
        CDLDOJI= np.matrix(np.roll(CDLDOJI, shift)).T
        matriz = np.concatenate((matriz, CDLDOJI), axis=1)
        del CDLDOJI    
        
    if IND[26]=='1':
        CDLDOJISTAR=talib.CDLDOJISTAR(apertura,high,low,close) 
        CDLDOJISTAR= np.matrix(np.roll(CDLDOJISTAR, shift)).T
        matriz = np.concatenate((matriz, CDLDOJISTAR), axis=1)
        del CDLDOJISTAR            
 
    if IND[27]=='1':
        CDLDRAGONFLYDOJI=talib.CDLDRAGONFLYDOJI(apertura,high,low,close) 
        CDLDRAGONFLYDOJI= np.matrix(np.roll(CDLDRAGONFLYDOJI, shift)).T
        matriz = np.concatenate((matriz, CDLDRAGONFLYDOJI), axis=1)
        del CDLDRAGONFLYDOJI  

    if IND[28]=='1':
        CDLENGULFING=talib.CDLENGULFING(apertura,high,low,close) 
        CDLENGULFING= np.matrix(np.roll(CDLENGULFING, shift)).T
        matriz = np.concatenate((matriz, CDLENGULFING), axis=1)
        del CDLENGULFING 

    if IND[29]=='1':
        CDLEVENINGDOJISTAR=talib.CDLEVENINGDOJISTAR(apertura,high,low,close) 
        CDLEVENINGDOJISTAR= np.matrix(np.roll(CDLEVENINGDOJISTAR, shift)).T
        matriz = np.concatenate((matriz, CDLEVENINGDOJISTAR), axis=1)
        del CDLEVENINGDOJISTAR 

    
    if IND[30]=='1':
        CDLEVENINGSTAR=talib.CDLEVENINGSTAR(apertura,high,low,close) 
        CDLEVENINGSTAR= np.matrix(np.roll(CDLEVENINGSTAR, shift)).T
        matriz = np.concatenate((matriz, CDLEVENINGSTAR), axis=1)
        del CDLEVENINGSTAR                 
 
   
    if IND[31]=='1':
        CDLGAPSIDESIDEWHITE=talib.CDLGAPSIDESIDEWHITE(apertura,high,low,close) 
        CDLGAPSIDESIDEWHITE= np.matrix(np.roll(CDLGAPSIDESIDEWHITE, shift)).T
        matriz = np.concatenate((matriz, CDLGAPSIDESIDEWHITE), axis=1)
        del CDLGAPSIDESIDEWHITE     
    
    
    if IND[32]=='1':
        CDLGRAVESTONEDOJI=talib.CDLGRAVESTONEDOJI(apertura,high,low,close) 
        CDLGRAVESTONEDOJI= np.matrix(np.roll(CDLGRAVESTONEDOJI, shift)).T
        matriz = np.concatenate((matriz, CDLGRAVESTONEDOJI), axis=1)
        del CDLGRAVESTONEDOJI      
    
    
    if IND[33]=='1':
        CDLHAMMER=talib.CDLHAMMER(apertura,high,low,close) 
        CDLHAMMER= np.matrix(np.roll(CDLHAMMER, shift)).T
        matriz = np.concatenate((matriz, CDLHAMMER), axis=1)
        del CDLHAMMER       

    if IND[34]=='1':
        CDLHANGINGMAN=talib.CDLHANGINGMAN(apertura,high,low,close) 
        CDLHANGINGMAN= np.matrix(np.roll(CDLHANGINGMAN, shift)).T
        matriz = np.concatenate((matriz, CDLHANGINGMAN), axis=1)
        del CDLHANGINGMAN  
        
    if IND[35]=='1':
        CDLHARAMI=talib.CDLHARAMI(apertura,high,low,close) 
        CDLHARAMI= np.matrix(np.roll(CDLHARAMI, shift)).T
        matriz = np.concatenate((matriz, CDLHARAMI), axis=1)
        del CDLHARAMI  
  
    if IND[35]=='1':
        CDLHARAMICROSS=talib.CDLHARAMICROSS(apertura,high,low,close) 
        CDLHARAMICROSS= np.matrix(np.roll(CDLHARAMICROSS, shift)).T
        matriz = np.concatenate((matriz, CDLHARAMICROSS), axis=1)
        del CDLHARAMICROSS  

    if IND[37]=='1':
        CDLHIGHWAVE=talib.CDLHIGHWAVE(apertura,high,low,close) 
        CDLHIGHWAVE= np.matrix(np.roll(CDLHIGHWAVE, shift)).T
        matriz = np.concatenate((matriz, CDLHIGHWAVE), axis=1)
        del CDLHIGHWAVE  
        
    if IND[38]=='1':
        CDLHIKKAKE=talib.CDLHIKKAKE(apertura,high,low,close) 
        CDLHIKKAKE= np.matrix(np.roll(CDLHIKKAKE, shift)).T
        matriz = np.concatenate((matriz, CDLHIKKAKE), axis=1)
        del CDLHIKKAKE          
    
    if IND[39]=='1':
        CDLHIKKAKEMOD=talib.CDLHIKKAKEMOD(apertura,high,low,close) 
        CDLHIKKAKEMOD= np.matrix(np.roll(CDLHIKKAKEMOD, shift)).T
        matriz = np.concatenate((matriz, CDLHIKKAKEMOD), axis=1)
        del CDLHIKKAKEMOD      
    
    if IND[40]=='1':
        CDLHOMINGPIGEON=talib.CDLHOMINGPIGEON(apertura,high,low,close) 
        CDLHOMINGPIGEON= np.matrix(np.roll(CDLHOMINGPIGEON, shift)).T
        matriz = np.concatenate((matriz, CDLHOMINGPIGEON), axis=1)
        del CDLHOMINGPIGEON 
        
    if IND[41]=='1':
        CDLIDENTICAL3CROWS=talib.CDLIDENTICAL3CROWS(apertura,high,low,close) 
        CDLIDENTICAL3CROWS= np.matrix(np.roll(CDLIDENTICAL3CROWS, shift)).T
        matriz = np.concatenate((matriz, CDLIDENTICAL3CROWS), axis=1)
        del CDLIDENTICAL3CROWS 
    
    if IND[42]=='1':
        CDLINNECK=talib.CDLINNECK(apertura,high,low,close) 
        CDLINNECK= np.matrix(np.roll(CDLINNECK, shift)).T
        matriz = np.concatenate((matriz, CDLINNECK), axis=1)
        del CDLINNECK     
    
    if IND[43]=='1':
        CDLINVERTEDHAMMER=talib.CDLINVERTEDHAMMER(apertura,high,low,close) 
        CDLINVERTEDHAMMER= np.matrix(np.roll(CDLINVERTEDHAMMER, shift)).T
        matriz = np.concatenate((matriz, CDLINVERTEDHAMMER), axis=1)
        del CDLINVERTEDHAMMER     
 
    if IND[44]=='1':
        CDLKICKING=talib.CDLKICKING(apertura,high,low,close) 
        CDLKICKING= np.matrix(np.roll(CDLKICKING, shift)).T
        matriz = np.concatenate((matriz, CDLKICKING), axis=1)
        del CDLKICKING 
        
    if IND[45]=='1':
        CDLKICKINGBYLENGTH=talib.CDLKICKINGBYLENGTH(apertura,high,low,close) 
        CDLKICKINGBYLENGTH= np.matrix(np.roll(CDLKICKINGBYLENGTH, shift)).T
        matriz = np.concatenate((matriz, CDLKICKINGBYLENGTH), axis=1)
        del CDLKICKINGBYLENGTH 

    if IND[46]=='1':
        CDLLADDERBOTTOM=talib.CDLLADDERBOTTOM(apertura,high,low,close) 
        CDLLADDERBOTTOM= np.matrix(np.roll(CDLLADDERBOTTOM, shift)).T
        matriz = np.concatenate((matriz, CDLLADDERBOTTOM), axis=1)
        del CDLLADDERBOTTOM 

    if IND[47]=='1':
        CDLLONGLEGGEDDOJI=talib.CDLLONGLEGGEDDOJI(apertura,high,low,close) 
        CDLLONGLEGGEDDOJI= np.matrix(np.roll(CDLLONGLEGGEDDOJI, shift)).T
        matriz = np.concatenate((matriz, CDLLONGLEGGEDDOJI), axis=1)
        del CDLLONGLEGGEDDOJI 
     
    if IND[48]=='1':
        CDLLONGLINE=talib.CDLLONGLINE(apertura,high,low,close) 
        CDLLONGLINE= np.matrix(np.roll(CDLLONGLINE, shift)).T
        matriz = np.concatenate((matriz, CDLLONGLINE), axis=1)
        del CDLLONGLINE 
        
    if IND[49]=='1':
        CDLMARUBOZU=talib.CDLMARUBOZU(apertura,high,low,close) 
        CDLMARUBOZU= np.matrix(np.roll(CDLMARUBOZU, shift)).T
        matriz = np.concatenate((matriz, CDLMARUBOZU), axis=1)
        del CDLMARUBOZU 
        
    if IND[50]=='1':
        CDLMATCHINGLOW=talib.CDLMATCHINGLOW(apertura,high,low,close) 
        CDLMATCHINGLOW= np.matrix(np.roll(CDLMATCHINGLOW, shift)).T
        matriz = np.concatenate((matriz, CDLMATCHINGLOW), axis=1)
        del CDLMATCHINGLOW         
        
    if IND[51]=='1':
        CDLMATHOLD=talib.CDLMATHOLD(apertura,high,low,close) 
        CDLMATHOLD= np.matrix(np.roll(CDLMATHOLD, shift)).T
        matriz = np.concatenate((matriz, CDLMATHOLD), axis=1)
        del CDLMATHOLD
        
    if IND[52]=='1':
        CDLMORNINGDOJISTAR=talib.CDLMORNINGDOJISTAR(apertura,high,low,close) 
        CDLMORNINGDOJISTAR= np.matrix(np.roll(CDLMORNINGDOJISTAR, shift)).T
        matriz = np.concatenate((matriz, CDLMORNINGDOJISTAR), axis=1)
        del CDLMORNINGDOJISTAR
    
    if IND[53]=='1':
        CDLMORNINGSTAR=talib.CDLMORNINGSTAR(apertura,high,low,close) 
        CDLMORNINGSTAR= np.matrix(np.roll(CDLMORNINGSTAR, shift)).T
        matriz = np.concatenate((matriz, CDLMORNINGSTAR), axis=1)
        del CDLMORNINGSTAR
        
    if IND[54]=='1':
        CDLONNECK=talib.CDLONNECK(apertura,high,low,close) 
        CDLONNECK= np.matrix(np.roll(CDLONNECK, shift)).T
        matriz = np.concatenate((matriz, CDLONNECK), axis=1)
        del CDLONNECK
    
    if IND[55]=='1':
        CDLPIERCING=talib.CDLPIERCING(apertura,high,low,close) 
        CDLPIERCING= np.matrix(np.roll(CDLPIERCING, shift)).T
        matriz = np.concatenate((matriz, CDLPIERCING), axis=1)
        del CDLPIERCING
        
    if IND[0]=='1':
        CDLRICKSHAWMAN=talib.CDLRICKSHAWMAN(apertura,high,low,close) 
        CDLRICKSHAWMAN= np.matrix(np.roll(CDLRICKSHAWMAN, shift)).T
        matriz = np.concatenate((matriz, CDLRICKSHAWMAN), axis=1)
        del CDLRICKSHAWMAN
        
    if IND[56]=='1':
        CDLRISEFALL3METHODS=talib.CDLRISEFALL3METHODS(apertura,high,low,close) 
        CDLRISEFALL3METHODS= np.matrix(np.roll(CDLRISEFALL3METHODS, shift)).T
        matriz = np.concatenate((matriz, CDLRISEFALL3METHODS), axis=1)
        del CDLRISEFALL3METHODS

    if IND[57]=='1':
        CDLSEPARATINGLINES=talib.CDLSEPARATINGLINES(apertura,high,low,close) 
        CDLSEPARATINGLINES= np.matrix(np.roll(CDLSEPARATINGLINES, shift)).T
        matriz = np.concatenate((matriz, CDLSEPARATINGLINES), axis=1)
        del CDLSEPARATINGLINES
        
    if IND[58]=='1':
        CDLSHOOTINGSTAR=talib.CDLSHOOTINGSTAR(apertura,high,low,close) 
        CDLSHOOTINGSTAR= np.matrix(np.roll(CDLSHOOTINGSTAR, shift)).T
        matriz = np.concatenate((matriz, CDLSHOOTINGSTAR), axis=1)
        del CDLSHOOTINGSTAR

    if IND[59]=='1':
        CDLSHORTLINE=talib.CDLSHORTLINE(apertura,high,low,close) 
        CDLSHORTLINE= np.matrix(np.roll(CDLSHORTLINE, shift)).T
        matriz = np.concatenate((matriz, CDLSHORTLINE), axis=1)
        del CDLSHORTLINE
        
    if IND[60]=='1':
        CDLSPINNINGTOP=talib.CDLSPINNINGTOP(apertura,high,low,close) 
        CDLSPINNINGTOP= np.matrix(np.roll(CDLSPINNINGTOP, shift)).T
        matriz = np.concatenate((matriz, CDLSPINNINGTOP), axis=1)
        del CDLSPINNINGTOP

    if IND[61]=='1':
        CDLSTALLEDPATTERN=talib.CDLSTALLEDPATTERN(apertura,high,low,close) 
        CDLSTALLEDPATTERN= np.matrix(np.roll(CDLSTALLEDPATTERN, shift)).T
        matriz = np.concatenate((matriz, CDLSTALLEDPATTERN), axis=1)
        del CDLSTALLEDPATTERN
        
    if IND[62]=='1':
        CDLSTICKSANDWICH=talib.CDLSTICKSANDWICH(apertura,high,low,close) 
        CDLSTICKSANDWICH= np.matrix(np.roll(CDLSTICKSANDWICH, shift)).T
        matriz = np.concatenate((matriz, CDLSTICKSANDWICH), axis=1)
        del CDLSTICKSANDWICH

    if IND[63]=='1':
        CDLTAKURI=talib.CDLTAKURI(apertura,high,low,close) 
        CDLTAKURI= np.matrix(np.roll(CDLTAKURI, shift)).T
        matriz = np.concatenate((matriz, CDLTAKURI), axis=1)
        del CDLTAKURI
        
    if IND[64]=='1':
        CDLTASUKIGAP=talib.CDLTASUKIGAP(apertura,high,low,close) 
        CDLTASUKIGAP= np.matrix(np.roll(CDLTASUKIGAP, shift)).T
        matriz = np.concatenate((matriz, CDLTASUKIGAP), axis=1)
        del CDLTASUKIGAP
 
    if IND[65]=='1':
        CDLTHRUSTING=talib.CDLTHRUSTING(apertura,high,low,close) 
        CDLTHRUSTING= np.matrix(np.roll(CDLTHRUSTING, shift)).T
        matriz = np.concatenate((matriz, CDLTHRUSTING), axis=1)
        del CDLTHRUSTING
        
    if IND[66]=='1':
        CDLTRISTAR=talib.CDLTRISTAR(apertura,high,low,close) 
        CDLTRISTAR= np.matrix(np.roll(CDLTRISTAR, shift)).T
        matriz = np.concatenate((matriz, CDLTRISTAR), axis=1)
        del CDLTRISTAR

    if IND[67]=='1':
        CDLUNIQUE3RIVER=talib.CDLUNIQUE3RIVER(apertura,high,low,close) 
        CDLUNIQUE3RIVER= np.matrix(np.roll(CDLUNIQUE3RIVER, shift)).T
        matriz = np.concatenate((matriz, CDLUNIQUE3RIVER), axis=1)
        del CDLUNIQUE3RIVER
        
    if IND[68]=='1':
        CDLUPSIDEGAP2CROWS=talib.CDLUPSIDEGAP2CROWS(apertura,high,low,close) 
        CDLUPSIDEGAP2CROWS= np.matrix(np.roll(CDLUPSIDEGAP2CROWS, shift)).T
        matriz = np.concatenate((matriz, CDLUPSIDEGAP2CROWS), axis=1)
        del CDLUPSIDEGAP2CROWS

    if IND[69]=='1':
        CDLXSIDEGAP3METHODS=talib.CDLXSIDEGAP3METHODS(apertura,high,low,close) 
        CDLXSIDEGAP3METHODS= np.matrix(np.roll(CDLXSIDEGAP3METHODS, shift)).T
        matriz = np.concatenate((matriz, CDLXSIDEGAP3METHODS), axis=1)
        del CDLXSIDEGAP3METHODS        
        
    if IND[70]=='1':
        CMO=talib.CMO(close,timeperiod=10) 
        CMO= np.matrix(np.roll(CMO, shift)).T
        matriz = np.concatenate((matriz, CMO), axis=1)
        del CMO 

    #CORREL=talib.CORREL(close,,serie2,timeperiod=10)
    
    if IND[71]=='1':
        DEMA=talib.DEMA(close,timeperiod=10)
        DEMA= np.matrix(np.roll(DEMA, shift)).T
        matriz = np.concatenate((matriz, DEMA), axis=1)
        del DEMA 

    if IND[72]=='1':
        DX=talib.DX(high,low,close,timeperiod=10)
        DX= np.matrix(np.roll(DX, shift)).T
        matriz = np.concatenate((matriz, DX), axis=1)
        del DX 
    
    if IND[73]=='1':
        EMA=talib.EMA(close,timeperiod=10) 
        EMA= np.matrix(np.roll(EMA, shift)).T
        matriz = np.concatenate((matriz, EMA), axis=1)
        del EMA 
        
    if IND[74]=='1':
        EMA=talib.EMA(close,timeperiod=10) 
        EMA= np.matrix(np.roll(EMA, shift)).T
        matriz = np.concatenate((matriz, EMA), axis=1)
        del EMA 
        
    if IND[75]=='1':
        HT_DCPERIOD=talib.HT_DCPERIOD(close) 
        HT_DCPERIOD= np.matrix(np.roll(HT_DCPERIOD, shift)).T
        matriz = np.concatenate((matriz, HT_DCPERIOD), axis=1)
        del HT_DCPERIOD        
    
    if IND[76]=='1':
        HT_DCPHASE=talib.HT_DCPHASE(close) 
        HT_DCPHASE= np.matrix(np.roll(HT_DCPHASE, shift)).T
        matriz = np.concatenate((matriz, HT_DCPHASE), axis=1)
        del HT_DCPHASE     
        
    if IND[77]=='1':
        HT_PHASOR=talib.HT_PHASOR(close) 
        HT_PHASOR= np.matrix(np.roll(HT_PHASOR, shift)).T
        matriz = np.concatenate((matriz, HT_PHASOR), axis=1)
        del HT_PHASOR     

    if IND[78]=='1':
        HT_SINE=talib.HT_SINE(close) 
        HT_SINE= np.matrix(np.roll(HT_SINE, shift)).T
        matriz = np.concatenate((matriz, HT_SINE), axis=1)
        del HT_SINE     

    if IND[79]=='1':
        HT_TRENDLINE=talib.HT_TRENDLINE(close) 
        HT_TRENDLINE= np.matrix(np.roll(HT_TRENDLINE, shift)).T
        matriz = np.concatenate((matriz, HT_TRENDLINE), axis=1)
        del HT_TRENDLINE     
    
    if IND[80]=='1':
        HT_TRENDMODE=talib.HT_TRENDMODE(close) 
        HT_TRENDMODE= np.matrix(np.roll(HT_TRENDMODE, shift)).T
        matriz = np.concatenate((matriz, HT_TRENDMODE), axis=1)
        del HT_TRENDMODE     
    
    if IND[81]=='1':
        KAMA=talib.KAMA(close,timeperiod=10) 
        KAMA= np.matrix(np.roll(KAMA, shift)).T
        matriz = np.concatenate((matriz, KAMA), axis=1)
        del KAMA    
    if IND[82]=='1':
        LINEARREG=talib.LINEARREG(close,timeperiod=10) 
        LINEARREG= np.matrix(np.roll(LINEARREG, shift)).T
        matriz = np.concatenate((matriz, LINEARREG), axis=1)
        del LINEARREG  
        
    if IND[83]=='1':
        LINEARREG_ANGLE=talib.LINEARREG_ANGLE(close,timeperiod=10) 
        LINEARREG_ANGLE= np.matrix(np.roll(LINEARREG_ANGLE, shift)).T
        matriz = np.concatenate((matriz, LINEARREG_ANGLE), axis=1)
        del LINEARREG_ANGLE  
        
    if IND[84]=='1':
        LINEARREG_INTERCEPT=talib.LINEARREG_INTERCEPT(close,timeperiod=10) 
        LINEARREG_INTERCEPT= np.matrix(np.roll(LINEARREG_INTERCEPT, shift)).T
        matriz = np.concatenate((matriz, LINEARREG_INTERCEPT), axis=1)
        del LINEARREG_INTERCEPT  
        
    if IND[85]=='1':
        LINEARREG_SLOPE=talib.LINEARREG_SLOPE(close,timeperiod=10) 
        LINEARREG_SLOPE= np.matrix(np.roll(LINEARREG_SLOPE, shift)).T
        matriz = np.concatenate((matriz, LINEARREG_SLOPE), axis=1)
        del LINEARREG_SLOPE  
        
    if IND[86]=='1':
        MA=talib.MA(close,timeperiod=10) 
        MA= np.matrix(np.roll(MA, shift)).T
        matriz = np.concatenate((matriz, MA), axis=1)
        del MA  
              
    if IND[87]=='1':
        MACD=talib.MACD(close,fastperiod=5,slowperiod=10,signalperiod=14)
        MACD= np.matrix(np.roll(MACD, shift)).T
        matriz = np.concatenate((matriz, MACD), axis=1)
        del MACD  
        
    if IND[88]=='1':
        MACDEXT=talib.MACDEXT(close,fastperiod=5,slowperiod=10,signalperiod=14)
        MACDEXT= np.matrix(np.roll(MACDEXT, shift)).T
        matriz = np.concatenate((matriz, MACDEXT), axis=1)
        del MACDEXT  
    
    if IND[89]=='1':
        MACDFIX=talib.MACDFIX(close,signalperiod=14)
        MACDFIX= np.matrix(np.roll(MACDFIX, shift)).T
        matriz = np.concatenate((matriz, MACDFIX), axis=1)
        del MACDFIX      
      
    #MAMA=talib.MAMA(close,fastlimit=5,slowlimit=10)
    
    if IND[90]=='1':
        MAXINDEX=talib.MAXINDEX(close,timeperiod=15)
        MAXINDEX= np.matrix(np.roll(MAXINDEX, shift)).T
        matriz = np.concatenate((matriz, MAXINDEX), axis=1)
        del MAXINDEX      
    
    if IND[91]=='1':
        MEDPRICE=talib.MEDPRICE(high,low)
        MEDPRICE= np.matrix(np.roll(MEDPRICE, shift)).T
        matriz = np.concatenate((matriz, MEDPRICE), axis=1)
        del MEDPRICE  
        
    if IND[92]=='1':
        MFI=talib.MFI(high,low,close,volume,timeperiod=10)
        MFI= np.matrix(np.roll(MFI, shift)).T
        matriz = np.concatenate((matriz, MFI), axis=1)
        del MFI  
    
    if IND[93]=='1':
        MIDPOINT=talib.MIDPOINT(close,timeperiod=10)
        MIDPOINT= np.matrix(np.roll(MIDPOINT, shift)).T
        matriz = np.concatenate((matriz, MIDPOINT), axis=1)
        del MIDPOINT      
    
    if IND[94]=='1':
        MIDPRICE=talib.MIDPRICE(high,low,timeperiod=10)
        MIDPRICE= np.matrix(np.roll(MIDPRICE, shift)).T
        matriz = np.concatenate((matriz, MIDPRICE), axis=1)
        del MIDPRICE  
        
    if IND[95]=='1':
        MIN=talib.MIN(close,timeperiod=10)
        MIN= np.matrix(np.roll(MIN, shift)).T
        matriz = np.concatenate((matriz, MIN), axis=1)
        del MIN      
   
    if IND[96]=='1':
        MININDEX=talib.MININDEX(close,timeperiod=10) 
        MININDEX= np.matrix(np.roll(MININDEX, shift)).T
        matriz = np.concatenate((matriz, MININDEX), axis=1)
        del MININDEX      
    
    if IND[97]=='1':
        MINMAX=talib.MINMAX(close,timeperiod=10)
        MINMAX= np.matrix(np.roll(MINMAX, shift)).T
        matriz = np.concatenate((matriz, MINMAX), axis=1)
        del MINMAX  
        
    if IND[98]=='1':
        MINMAXINDEX=talib.MINMAXINDEX(close,timeperiod=10)
        MINMAXINDEX= np.matrix(np.roll(MINMAXINDEX, shift)).T
        matriz = np.concatenate((matriz, MINMAXINDEX), axis=1)
        del MINMAXINDEX        
    
    if IND[99]=='1':
        MINUS_DI=talib.MINUS_DI(high,low,close,timeperiod=10)
        MINUS_DI= np.matrix(np.roll(MINUS_DI, shift)).T
        matriz = np.concatenate((matriz, MINUS_DI), axis=1)
        del MINUS_DI      
    
    if IND[100]=='1':
        MINUS_DM=talib.MINUS_DM(high,low,timeperiod=10)
        MINUS_DM= np.matrix(np.roll(MINUS_DM, shift)).T
        matriz = np.concatenate((matriz, MINUS_DM), axis=1)
        del MINUS_DM  
        
    if IND[101]=='1':
        MOM=talib.MOM(close,timeperiod=10)
        MOM= np.matrix(np.roll(MOM, shift)).T
        matriz = np.concatenate((matriz, MOM), axis=1)
        del MOM          
     
    if IND[102]=='1':
        NATR=talib.NATR(high,low,close,timeperiod=10)
        NATR= np.matrix(np.roll(NATR, shift)).T
        matriz = np.concatenate((matriz, NATR), axis=1)
        del NATR      
    
    if IND[103]=='1':
        OBV=talib.OBV(close,volume)
        OBV= np.matrix(np.roll(OBV, shift)).T
        matriz = np.concatenate((matriz, OBV), axis=1)
        del OBV  
        
    if IND[104]=='1':
        PLUS_DI=talib.PLUS_DI(high,low,close,timeperiod=10)
        PLUS_DI= np.matrix(np.roll(PLUS_DI, shift)).T
        matriz = np.concatenate((matriz, PLUS_DI), axis=1)
        del PLUS_DI      
    
    if IND[105]=='1':
        PLUS_DM=talib.PLUS_DM(high,low,timeperiod=10)
        PLUS_DM= np.matrix(np.roll(PLUS_DM, shift)).T
        matriz = np.concatenate((matriz, PLUS_DM), axis=1)
        del PLUS_DM      
    
    if IND[106]=='1':
        PPO=talib.PPO(close,fastperiod=5,slowperiod=10)
        PPO= np.matrix(np.roll(PPO, shift)).T
        matriz = np.concatenate((matriz, PPO), axis=1)
        del PPO  
        
    if IND[107]=='1':
        ROC=talib.ROC(close,timeperiod=10)
        ROC= np.matrix(np.roll(ROC, shift)).T
        matriz = np.concatenate((matriz, ROC), axis=1)
        del ROC      
    
    if IND[108]=='1':
        ROCP=talib.ROCP(close,timeperiod=10)
        ROCP= np.matrix(np.roll(ROCP, shift)).T
        matriz = np.concatenate((matriz, ROCP), axis=1)
        del ROCP      
    
    if IND[109]=='1':
        ROCR=talib.ROCR(close,timeperiod=10)
        ROCR= np.matrix(np.roll(ROCR, shift)).T
        matriz = np.concatenate((matriz, ROCR), axis=1)
        del ROCR  
        
    if IND[110]=='1':
        ROCR100=talib.ROCR100(close,timeperiod=10)
        ROCR100= np.matrix(np.roll(ROCR100, shift)).T
        matriz = np.concatenate((matriz, ROCR100), axis=1)
        del ROCR100        
    
    if IND[111]=='1':
        RSI=talib.RSI(close,timeperiod=10)
        RSI= np.matrix(np.roll(RSI, shift)).T
        matriz = np.concatenate((matriz, RSI), axis=1)
        del RSI      
    
    if IND[112]=='1':
        SAR=talib.SAR(high,low,acceleration=10,maximum=20)
        SAR= np.matrix(np.roll(SAR, shift)).T
        matriz = np.concatenate((matriz, SAR), axis=1)
        del SAR  
        
    if IND[113]=='1':
        SMA=talib.SMA(close,timeperiod=10)
        SMA= np.matrix(np.roll(SMA, shift)).T
        matriz = np.concatenate((matriz, SMA), axis=1)
        del SMA       
       
    if IND[114]=='1':
        STDDEV=talib.STDDEV(close,timeperiod=10) ##Falta un parametro
        STDDEV= np.matrix(np.roll(STDDEV, shift)).T
        matriz = np.concatenate((matriz, STDDEV), axis=1)
        del STDDEV      
    
    if IND[115]=='1':
        STOCH=talib.STOCH(high,low,close,fastk_period=5,slowk_period=10,slowd_period=10)
        STOCH= np.matrix(np.roll(STOCH, shift)).T
        matriz = np.concatenate((matriz, STOCH), axis=1)
        del STOCH  
        
    if IND[116]=='1':
        STOCHF=talib.STOCHF(high,low,close,fastk_period=5)
        STOCHF= np.matrix(np.roll(STOCHF, shift)).T
        matriz = np.concatenate((matriz, STOCHF), axis=1)
        del STOCHF      
    
    if IND[117]=='1':
        STOCHRSI=talib.STOCHRSI(close,timeperiod=10,fastk_period=5,fastd_period=5)
        STOCHRSI= np.matrix(np.roll(STOCHRSI, shift)).T
        matriz = np.concatenate((matriz, STOCHRSI), axis=1)
        del STOCHRSI      
    
    if IND[118]=='1':
        SUM =talib.SUM(close,timeperiod=10)
        SUM= np.matrix(np.roll(SUM, shift)).T
        matriz = np.concatenate((matriz, SUM), axis=1)
        del SUM  
        
    if IND[119]=='1':
        T3 =talib.T3(close,timeperiod=10) ##Falta parametro
        T3= np.matrix(np.roll(T3, shift)).T
        matriz = np.concatenate((matriz, T3), axis=1)
        del T3       
    
    if IND[120]=='1':
        TEMA =talib.TEMA(close,timeperiod=10)
        TEMA= np.matrix(np.roll(TEMA, shift)).T
        matriz = np.concatenate((matriz, TEMA), axis=1)
        del TEMA      
    
    if IND[121]=='1':
        TRANGE =talib.TRANGE(high,low,close)
        TRANGE= np.matrix(np.roll(TRANGE, shift)).T
        matriz = np.concatenate((matriz, TRANGE), axis=1)
        del TRANGE  
        
    if IND[122]=='1':
        TRIMA =talib.TRIMA(close,timeperiod=10)
        TRIMA= np.matrix(np.roll(TRIMA, shift)).T
        matriz = np.concatenate((matriz, TRIMA), axis=1)
        del TRIMA         
    
    if IND[123]=='1':
        TRIX =talib.TRIX(close,timeperiod=10)
        TRIX= np.matrix(np.roll(TRIX, shift)).T
        matriz = np.concatenate((matriz, TRIX), axis=1)
        del TRIX      
    
    if IND[124]=='1':
        TSF =talib.TSF(close,timeperiod=10)
        TSF= np.matrix(np.roll(TSF, shift)).T
        matriz = np.concatenate((matriz, TSF), axis=1)
        del TSF  
        
    if IND[125]=='1':
        TYPPRICE =talib.TYPPRICE(high,low,close)
        TYPPRICE= np.matrix(np.roll(TYPPRICE, shift)).T
        matriz = np.concatenate((matriz, TYPPRICE), axis=1)
        del TYPPRICE           
    
    if IND[126]=='1':
        ULTOSC=talib.ULTOSC(high,low,close,timeperiod1=3,timeperiod2=5,timeperiod3=10)
        ULTOSC= np.matrix(np.roll(ULTOSC, shift)).T
        matriz = np.concatenate((matriz, ULTOSC), axis=1)
        del ULTOSC      
    
    if IND[127]=='1':
        VAR=talib.VAR(close,timeperiod=10)
        VAR= np.matrix(np.roll(VAR, shift)).T
        matriz = np.concatenate((matriz, VAR), axis=1)
        del VAR  
        
    if IND[128]=='1':
        WCLPRICE=talib.WCLPRICE(high,low,close)
        WCLPRICE= np.matrix(np.roll(WCLPRICE, shift)).T
        matriz = np.concatenate((matriz, WCLPRICE), axis=1)
        del WCLPRICE      
    
    if IND[129]=='1':
        WILLR=talib.WILLR(high,low,close,timeperiod=10)
        WILLR= np.matrix(np.roll(WILLR, shift)).T
        matriz = np.concatenate((matriz, WILLR), axis=1)
        del WILLR  
        
    if IND[130]=='1':
        WMA=talib.WMA(close,timeperiod=10)
        WMA= np.matrix(np.roll(WMA, shift)).T
        matriz = np.concatenate((matriz, WMA), axis=1)
        del WMA 
    return matriz[100:,:]         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











