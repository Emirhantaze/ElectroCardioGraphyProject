from __future__ import division
import time
import pandas as pd
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(i):
    a= time.time()
    data = pd.read_csv('Filtereddata.csv')
    temp=len(data['t'])
    y1 = data['f'][temp-600:temp-1]
    x = data['t'][temp-600:temp-1]
    
    plt.cla()
    #y1=y1-mina
    plt.plot(x,y1)
    #plt.xlim(int(x[temp-1])-3,int(x[temp-1]))
    print(round(time.time()-a,4))
    #plt.ylim(-200,500)




    
ani = FuncAnimation(plt.gcf(),animate,interval=3)
plt.show() 
   
        
   

