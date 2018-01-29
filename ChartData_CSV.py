
import pandas as pd
import PoloniexAPI as polo
import time

P=polo.Poloniex("","")
Tiker=P.returnTicker()

coin=[]
for i in Tiker.keys():
    coin.append(i)
    
i=5
for i in range(9,len(coin)):
    Salida= pd.DataFrame(P.returnChartData(coin[i]))
    Salida.to_csv('D:/Repositorio/Python/Coin TFM/ChartData/'+coin[i]+'.csv')
    print(i)
    time.sleep(5)
    
#datos=pd.DataFrame(P.returnMarketTradeHistory("BTC_DASH","01/11/2017","02/11/2017"))
#data = pd.DataFrame(P.returnMarketTradeHistory("BTC_DASH","01/11/2017","02/11/2017"))





