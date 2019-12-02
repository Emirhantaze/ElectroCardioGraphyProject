from __future__ import division
import numpy as np
import talib as ta  
from scipy.signal import butter, lfilter,cheby2,ellip
# this page used for butterworth filter design 
# https://scipy-cookbook.readthedocs.io/items/ButterworthBandpass.html
def cheby_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = cheby2(order, 1,[low, high], btype='band')
    return b, a


def cheby_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = ellip_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
def ellip_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = ellip(order,1, 1,[low, high], btype='band')
    return b, a


def ellip_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = ellip_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y    
def myfft(tin,fin):
    ECG=fin
    t=tin
    L=len(t)
    Ts = np.mean(np.diff(t))
    Fs = 1/Ts                          
    Fn = Fs/2
    FECG = np.fft.fft(ECG)
    temp=np.floor(L/2)
    Fv = np.linspace(0, 1, temp)*Fn
    temp=len(Fv)+1
    Iv = np.arange(1,temp)
    FECG = np.abs(FECG[Iv])/L
    return Fv,FECG
def delete_first(t,f):
    flag = True
    i=0
    difft = np.diff(t)
    t=t[20:len(t)]
    f=f[20:len(f)]
    while flag:
        if(difft(i)>0.006):
            flag=False
        i=i+1
    t=t[i:len(t)]
    f=f[i:len(f)]
    return [t,f]
def findPerf(t,f,flag):
    temp=delete_first(t,f)
    t=temp[0]
    f=temp[1]
    f=f-ta.MA(f,75)
    temp=[]
    ii=0
    if(flag):
        for i in np.arange(0,len(f)-100):
            temp = [temp , np.mean(np.diff(f[i:i+100]))]
            if np.abs(temp[i]==np.min(np.abs(temp))):
                ii=i
        f=f[ii:ii+100]
        t=t[ii:ii+100]
