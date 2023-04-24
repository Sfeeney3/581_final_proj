import pandas as pd
from sklearn import preprocessing
import math
import scipy.stats as stats

soxl = pd.read_csv('./csv/soxl.csv',header=0, names = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])


close = soxl["Close"]   # Select the column using column name and assign it to a new object



def returns(close):
    
    dataFrameSum = pd.DataFrame(columns=["daily_return_normalized"])

    #get daily return
    for i in range(len(close)):
        if i <1:
            pass
        else:
            #print("Element at index", i, ":", close[i])
            daily_return = (close[i-1]/close[i]) -1
            
            new_row = pd.Series({'daily_return_normalized': daily_return })
            dataFrameSum = pd.concat([dataFrameSum, new_row.to_frame().T], ignore_index=True)
            
    
    
    print(len(dataFrameSum))
    
    return dataFrameSum


dataFrameSum = returns(close)

n = len(soxl) - len(dataFrameSum)

soxl.drop(soxl.tail(n).index,inplace=True)
  


soxl = soxl.join(dataFrameSum[['daily_return_normalized']].set_axis(soxl.index))

soxl.to_csv("./csv/soxl_aug.csv")










