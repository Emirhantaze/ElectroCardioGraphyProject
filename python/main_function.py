from __future__ import division
import time
import ecgF as e
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import pandas as pd
from matplotlib.widgets import Cursor
  
'''
To use Move mean use ta.MA(FUNCTION,perioad)
'''
def main():
    """
    mat = scipy.io.loadmat('datas/31.10.2019.mat') #loading matlab file
    
    t=mat['t9'][0] #What are the purpose of them?
    f=-mat['f9'][0]
    """
    data = pd.read_csv('Rawdata.csv')
    f =  (data['f'].values)
    t =  (data['t'].values)
    tf=e.myfft(t,f)
    fig = plt.figure(figsize=(8, 6))
    plt.show(block=False) # what is that?
    ax = fig.add_subplot(111)
    ax.plot(tf[0],tf[1])
    ax.set_xlim(0,100)
    ax.grid(True)
    plt.xticks(np.arange(0,101,5)) #xtics : Get or set the current tick locations and labels of the x-axis.
    #It is setting the x ticks with list of ticks.
    cursor = Cursor(ax, useblit=True, color='r', linewidth=0.4)
    plt.show(block=True)



if __name__ == "__main__":
    main()    