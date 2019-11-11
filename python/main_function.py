import time
import ecgF as e
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

def main():
    mat = scipy.io.loadmat('datas/31.10.2019.mat')
    
    t=mat['t9'][0]
    f=mat['f9'][0]
    f=-f
    print(len(f))
    tf=e.myfft(t,f)
    plt.plot(tf[0],tf[1])
    plt.xlim(0,100)
    plt.grid(True)
    plt.tick_params(direction='out', length=6, width=2, colors='r',
               grid_color='r', grid_alpha=0.5,
               grid_linestyle='-')
    plt.ginput(n=-1,timeout=120)
    plt.show()



if __name__ == "__main__":
    main()
    