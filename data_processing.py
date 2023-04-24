import pandas as pd

def dataread(etf):
    data = pd.read_csv('./csv/'+etf+'.csv',header=0, names = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

    return data



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





if __name__ == "__main__":  
    #data processing
   print("Stage: Get etfs")
   with open("./config/etfname.txt", "r") as etflist: 
      # reading the file
      data = etflist.read()
      # replacing end splitting the text when newline ('\n') is seen.
      etfs = data.split("\n")

   corrDf = pd.DataFrame(columns=["bndx","gld","ijh","ijr","soxx","spy","vea","vwo"])   
   print("Stage: augment etf data for daily return")
   for etf in etfs:
      print(etf)
      dataEtf = dataread(etf)
      close = dataEtf["Close"]
      dataFrameSum = returns(close)
      
      corrDf[etf]=dataFrameSum.loc[:,"daily_return_normalized"]
      
      n = len(dataEtf) - len(dataFrameSum)

      dataEtf.drop(dataEtf.tail(n).index,inplace=True)
  


      dataEtf = dataEtf.join(dataFrameSum[['daily_return_normalized']].set_axis(dataEtf.index))

      dataEtf.to_csv("./csv/"+etf+"_augmented.csv")
    
    # To find the correlation among
    # the columns using pearson method
   corrDf = corrDf.corr(method ='pearson')
   corrDf.to_csv("./csv/corrDf.csv") 
    
    
      