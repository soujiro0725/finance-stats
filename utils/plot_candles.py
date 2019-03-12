import mpl_finance

def pc(plt, df, keys=['Open', 'Hight', 'Low', 'Close']):
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1, 1, 1)
    mpl_finance.candlestick2_ohlc(ax, 
                                  df[keys[0]], 
                                  df[keys[1]], 
                                  df[keys[2]], 
                                  df[keys[3]], 
                                  width=2, 
                                  alpha=0.5, 
                                  colorup='r', 
                                  colordown='b')
    ax.plot(df_.index, df_.Close.rolling(5).mean())
    ax.plot(df_.index, df_.Close.rolling(25).mean())
    ax.grid()
    #locator = mdates.AutoDateLocator()
    #ax.xaxis.set_major_locator(locator)
    #ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))