import time
import ecgF as e
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from matplotlib.widgets import Cursor

def main():
    mat = scipy.io.loadmat('datas/31.10.2019.mat')
    
    t=mat['t9'][0]
    f=-mat['f9'][0]
    print(len(f))
    tf=e.myfft(t,f)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.plot(tf[0],tf[1])
    ax.set_xlim(0,100)
    ax.grid(True)
    cursor = Cursor(ax, useblit=True, color='r', linewidth=0.4)
    plt.show()



if __name__ == "__main__":
    main()    