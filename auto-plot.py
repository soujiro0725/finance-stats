import datetime
import json
import boto3
import io
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
#import seaborn as sns
plt.style.use('ggplot')

pickle_file = '../btc-autotrader/lib/data/log/2019-03-08T20:58:17.154575.pickle'

def update_plot():

    fig, ax1 = plt.subplots(figsize=(15,10))
    ax2 = ax1.twinx()
    ax2.legend()
    
    while True:
        df = pd.read_pickle(pickle_file)
        
        ax1.plot(df.datetime, df.btc_current_price, color='r')
        ax1.plot(df.datetime, df.btc_current_price.rolling(70).mean(), color='pink')
        #ax1.scatter(df.datetime, df.bid_price, color='black')
        ax2.plot(df.datetime, df.rate_of_change, color='b')
        ax2.plot(df.datetime, df.acceleration, color='g')
        
        plt.pause(.01)

if __name__ == '__main__':
    update_plot()
    
