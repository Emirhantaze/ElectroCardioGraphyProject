from __future__ import division
import time
import pandas as pd
import ecgF as e
import numpy as np
import scipy.io
import talib as ta  
import drawnow
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
t = 0
data = pd.read_csv('data.csv')
y1 = data['x_value']
x = data['total_1']
def animate():
    plt.plot(x,y1)
    
    plt.xlim(left=t-5,right=t-1)
while True:
    data = pd.read_csv('data.csv')
    y1 = data['x_value']
    x = data['total_1']
    
    t = len(x)
    t=(x[t-1])
    
    drawnow.drawnow(animate)
        
        
   

