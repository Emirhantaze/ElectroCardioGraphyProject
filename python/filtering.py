from __future__ import division
"""
our first method will be the taking signal
Then to analayze we take the last x values of it
then we move it to the moving avarage filter 
then filtering with selected mod, order and frequencies 
then peak finding
then plotting out everything
"""
'''
Author Emirhan Taze
'''
import pandas as pd
import talib as ta
import csv
import time
import matplotlib.pyplot as plt
import numpy as np
import ecgF  as e
from decimal import getcontext
from scipy.signal import butter, lfilter,cheby2,ellip,find_peaks
getcontext().prec = 4
with open("filter.csv","w") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=["type","lowf","highf","order"])
    csv_writer.writeheader()
    info = {
                "type": "butter",
                "lowf": 1,
                "highf":20,
                "order":2
                
                }
    csv_writer.writerow(info)
with open("Filtereddata.csv","w") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=["t","f"])
    csv_writer.writeheader()
#while True:
data = pd.read_csv('Rawdata.csv')
y =  (data['f'].values)
x =  (data['t'].values)
y = np.array(y, dtype=float)
y=-y
#plt.plot(x,y)
#now we got raw whole signal now we get only last thousand values with checking size
temp = len(y)
if temp>1000:
    y=y[temp-1001:temp-1]
    x=x[temp-1001:temp-1]
#now moving avarage will be applied to signal
c=time.time()
y=y-ta.MA(y,200)
#after moving avareage we gaot selected filter and cutoffs so that we can start
temp=pd.read_csv("filter.csv")
temp1=len(temp["type"])
filtertype=temp["type"][temp1-1]
highf=temp["highf"][temp1-1]
lowf=temp["lowf"][temp1-1]
order=temp["order"][temp1-1]
Fs = 1/(np.mean(np.diff(x)))

f=y
if(filtertype=="none"):
    f=y
elif(filtertype=="butter"):
    f=e.butter_bandpass_filter(y,lowf,highf,Fs)
    print("succeeded!")
elif(filtertype=="cheby"):
    f=e.cheby_bandpass_filter(y,lowf,highf,Fs,order=order)
elif(filtertype=="ellip"):
    f=e.ellip_bandpass_filter(y,lowf,highf,Fs,order=order)


peaks, _ = find_peaks(y, distance=150)
plt.plot(x,y)
plt.plot(x[peaks], y[peaks], "x")
bpm=60/(np.mean(np.diff(x[peaks])))
print(time.time()-c)
print(bpm)
plt.show()
