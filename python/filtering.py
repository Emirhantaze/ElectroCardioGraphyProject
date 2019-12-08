from __future__ import division
"""
our first method will be the taking signal
Then to analayze the last taken x values of incoming signal
then we move it to the moving avarage filter 
then filtering by a bunch of selected mods such as butter, cheby, elliptic its order and frequencies 
after that we are going to find peaks
Later, plotting out everything
"""
'''
Author Emirhan Taze
'''
import pandas as pd #stand for Python Data Analysis Library # 
            #it takes data (like a CSV or TSV file, or a SQL database),
             #  and creates a Python object with rows and columns
#import talib as ta
import csv #read and write the data
import time
import matplotlib.pyplot as plt #plotting library for python
import numpy as np #scientific computing library which contains Fourier, Linear Algebra etc.
import ecgF  as e

from decimal import getcontext #fast correctly rounded decimal points aritmetic

#getcontext().prec = 4

with open("filter.csv","w") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=["type","lowf","highf","order"])
    csv_writer.writeheader()
    info = {
                "type": "none",
                "lowf": 0.05,
                "highf":30,
                "order":5
                
                }
    csv_writer.writerow(info)

say=2000

with open("Filtereddata.csv","w") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=["t","f"])
    csv_writer.writeheader()
while True:
    c=time.time()
    data = pd.read_csv('Rawdata.csv')
    y =  (data['f'].values)
    x =  (data['t'].values)

    
    #plt.plot(x,y)
    #now we got raw whole signal now we get only last thousand values with checking size
    temp = len(y)

    if temp>2000:
        y=y[temp-2000+1:temp-1]
        x=x[temp-2000+1:temp-1]
    #now moving avarage will be applied to signal
    #Cause of real number problem rigth now we will not use moving avarage method
    #If we found a clear solution it will be replaced
    #y=y-ta.MA(y,200)

    #after moving avareage we got selected filter and cutoffs so that we can start
    temp=pd.read_csv("filter.csv")
    temp1=len(temp["type"])
    filtertype=(temp["type"][temp1-1])
    highf=(temp["highf"][temp1-1])
    lowf=temp["lowf"][temp1-1]
    order=temp["order"][temp1-1]
    Fs = 1/(np.mean(np.diff(x)))
    if(filtertype=="none"):
        f=y
    elif(filtertype=="butter"):
        f=e.butter_bandpass_filter(y,lowf,highf,Fs,order)
        
    elif(filtertype=="cheby"):
        f=e.cheby_bandpass_filter(y,lowf,highf,Fs,order=order)
    elif(filtertype=="ellip"):
        f=e.ellip_bandpass_filter(y,lowf,highf,Fs,order=order)
    c=time.time()-c
    say=int(round((c*Fs),0))
    with open("Filtereddata.csv","a") as csv_file:
        
        csv_writer = csv.DictWriter(csv_file, fieldnames=["t","f"])
        #csv_writer.writeheader()
        for i in range(len(f)-say+1,len(f)-1):
            info={
                "t":x[i],
                "f":f[i]
            }
            csv_writer.writerow(info)
    
    print(round((c*Fs),0))
    
