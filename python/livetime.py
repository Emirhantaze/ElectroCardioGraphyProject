from __future__ import division
import time
import pandas as pd

import numpy as np
import scipy.io


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
t = 0
data = pd.read_csv('data.csv')
y1 = data['x_value']
x = data['total_1']
time.sleep(1)
def animate(i):
    data = pd.read_csv('Filtereddata.csv')
    temp=len(data['t'])
    y1 = data['f'][temp-600:temp]
    x = data['t'][temp-600:temp]
    plt.cla()
    
    #y1=y1-mina
    plt.plot(x,y1)
    #plt.xlim(int(x[temp-1])-3,int(x[temp-1]))
    
    #plt.ylim(-200,500)



t = len(x)
    #t=(x[t-1])
    
ani = FuncAnimation(plt.gcf(),animate,interval=20)
plt.show()    
        
   

