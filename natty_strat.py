import pandas as pd
import pandas_ta as ta
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy import stats
import mplfinance as mpf
import MetaTrader5 as mt5
from datetime import datetime,timedelta
import time
from backtesting import Backtest,Strategy
import talib

def support(df1, l, n1, n2): #n1 n2 before and after candle l
    for i in range(l-n1+1, l+1):
        if(df1.low[i]>df1.low[i-1]):
            return 0
    for i in range(l+1,l+n2+1):
        if(df1.low[i]<df1.low[i-1]):
            return 0
    return 1

#support(df,46,3,2)
            
def resistance(df1, l, n1, n2): #n1 n2 before and after candle l
    for i in range(l-n1+1, l+1):
        if(df1.high[i]<df1.high[i-1]):
            return 0
    for i in range(l+1,l+n2+1):
        if(df1.high[i]>df1.high[i-1]):
            return 0
    return 1

mt5.initialize()
login=24865159
password='Ianhen12-'
server='Deriv-Demo'
mt5.login(login,password,server)

#d1=pd.read_csv('AUDUSD-H1.csv')
d1=pd.DataFrame(mt5.copy_rates_range('AUDJPY',mt5.TIMEFRAME_M5,datetime(2024,1,1,0,0,0),datetime.now()))
#converting the time column to the index
d1['time']=pd.to_datetime(d1['time'],unit='s')
#Check if NA values are in data
d1=d1[d1['tick_volume']!=0]
d1.set_index(d1['time'],inplace=True)
d1


ssd1 = []
rrd1 = []
n1=2
n2=2
for row in range(len(d1)-n2): #len(df)-n2
    if support(d1, row, n1, n2):
        ssd1.append([d1.time.iloc[row],d1.low[row],0])
    if resistance(d1, row, n1, n2):
        rrd1.append([d1.time.iloc[row],d1.high[row],0])
## getting fiarl value gapes
df=d1
bul_fvgs=[]
bear_fvgs=[]
for i in range(3,len(df)-1):
    prev_high=df.high[i-1]
    next_low=df.low[i+1]
    prev_low=df.low[i-1]
    next_high=df.high[i+1]
    
    
    if next_low-prev_high>0:
        bul_fvgs.append((df.time[i],df.high[i-1],df.low[i+1],round(abs(df.high[i-1]-df.low[i+1]),5)))
    if prev_low-next_high>0:
        bear_fvgs.append((df.time[i],df.high[i+1],df.low[i-1],round(abs(df.high[i+1]-df.low[i-1]),5)))

#calculating the moving avergae
d1['sma']=d1.ta.sma(high=d1['high'],low=d1['low'],close=d1['close'],length=20)
bul_fvgs1=bul_fvgs.copy()
bear_fvgs1=bear_fvgs.copy()
##changin the naes of columes
d1.rename(columns={'close':'Close', 'open':'Open', 'high':'High', 'low':'Low','tick_volume':'Volume'}, inplace=True)
from datetime import time
class strat_2(Strategy):

    def init(self):
        pass
    def next(self):
        start_time=time(0,0)
        end_time=time(8,59)
        #print(self.end_time)
        time_now=self.data['time'][-1]
        timestamp = pd.to_datetime(time_now)
        
        if self.data['Close'][-1]>self.data['Open'][-1]:
        
            for x in range(10,len(bul_fvgs)-10):
                
                if (bul_fvgs[x][0]<self.data['time'][-1])&(bul_fvgs[x][1]<self.data['Low'][-1]<bul_fvgs[x][2]):
                    #print(bul_fvgs[x][3])
                    bul_fvgs.pop(x)
                    if (self.data['Close'][-1]>self.data['sma'][-1])&(start_time<=timestamp.time()<=end_time):
                        
                        self.buy(size=1000,sl=self.data['Open']-(3*bul_fvgs[x][3]),tp=self.data['Close'][-1]+(5*bul_fvgs[x][3]))
        

        if self.data['Close'][-1]<self.data['Open'][-1]:
           
        
            for x in range(10,len(bear_fvgs)-10):
                
                if (bear_fvgs[x][0]<self.data['time'][-1])&(bear_fvgs[x][1]<self.data['High'][-1]<bear_fvgs[x][2]):
                    #print(bul_fvgs[x][3])
                    
                    bear_fvgs.pop(x)
                    if (self.data['Close'][-1]<self.data['sma'][-1])&(start_time<=timestamp.time()<=end_time):
                        #print('test')
                        self.sell(size=1000,sl=self.data['Open']+(3*bear_fvgs[x][3]),tp=self.data['Close'][-1]-(9*bear_fvgs[x][3]))

bt = Backtest(d1[5000:], strat_2, cash=1000,margin=1/2000,exclusive_orders=True)
##pulling the backtest data from the class
results=bt.run()
strategy_instance=results._strategy
## getting a data frome of the trades
trades=results._trades