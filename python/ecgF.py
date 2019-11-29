from __future__ import division
import numpy as np
def myfft(tin,fin):
    ECG=fin[np.arange(250,len(fin))]
    t=tin[np.arange(250,len(tin))]
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
    return [Fv,FECG]
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
