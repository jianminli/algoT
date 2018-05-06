#test
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

def graphRawFx():
    time, Open, High, Low, Close, Volume = np.loadtxt(open("USDJPYHourly.csv")
                                                      , delimiter=","
                                                      , skiprows=1)
    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40),(0,0),rowspan=40,colspan=40)

    ax1.plot(time, Open)
    ax1.plot(time, Close)

    #ax1.xaxis.set_major_formatter()

    plt.grid(True)
    plt.show()
