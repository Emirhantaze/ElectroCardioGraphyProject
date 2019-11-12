import numpy as np
import statistics
def myfft(tin,fin):
    ECG=fin[np.arange(250,len(fin))]
    t=tin[np.arange(250,len(tin))]
    L=len(t)
    Ts = statistics.mean(np.diff(t))
    Fs = 1/Ts                                     
    Fn = Fs/2
    FECG = np.fft.fft(ECG)
    temp=np.floor(L/2)
    Fv = np.linspace(0, 1, temp)*Fn
    temp=len(Fv)+1
    Iv = np.arange(1,temp)
    FECG = np.abs(FECG[Iv])/L
    return [Fv,FECG]