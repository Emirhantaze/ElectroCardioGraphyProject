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
    tf=e.myfft(t,f)
    plt.plot(tf[0],tf[1])
    plt.show()


if __name__ == "__main__":
    main()
    