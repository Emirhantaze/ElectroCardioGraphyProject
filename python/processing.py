import serial
import serial.tools.list_ports
import csv
from time import sleep
import time
import pandas as pd
import ecgF  as e
import numpy as np
from scipy.signal import find_peaks
from multiprocessing import Process
from decimal import getcontext
def saveraw():
    """

    ser = serial.Serial("COM5",115200)
    fieldnames = ["t","f"]
    print(serial.tools.list_ports.comports().__getitem__(0))
    with open('Rawdata.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    
        a=time.time()
        print("tets")
        try:
            print(ser.readline().decode())
        
            while True:
                s=time.time()-a
                print(np.round(s,4))
                info = {
                    "f": ser.readline().decode(),
                    "t": np.round(s,4)

                        
                    }
                csv_writer.writerow(info)
        except:
            print("saveerr")       
                
    """
    
    ser = serial.Serial("COM5",115200)
    fieldnames = ["t","f"]
    print(serial.tools.list_ports.comports().__getitem__(0))
    with open('Rawdata.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    getcontext().prec = 4
    a=time.time()
    f=1
    try:
        ser.reset_input_buffer()
        ser.readline()
        ser.readline()
        sleep(0.1)
        print(ser.readline())
    except:
        print("")
   
    while True:
        
        
        try:
            with open('Rawdata.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                try :
                    x=ser.readline()
                    f=x.split(",")
                    s=f[1]-a
                except:
                    f=[1,1]
                    s=1
                info = {
                    "f": round(float(f[0]),5),
                    "t": round(s,5)

                        
                    }
                print(round(s,4))

                csv_writer.writerow(info)
         
        except:
            print("")
        
             
def filtering():
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
        try:
            c=time.time()
            data = pd.read_csv('Rawdata.csv')
            y =  (data['f'].values)
            x =  (data['t'].values)

            
            #plt.plot(x,y)
            #now we got raw whole signal now we get only last 2 thousand values with checking size
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
            sleep(0.011)
            
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
                
                try:
                   
                    for i in range(len(f)-say-1,len(f)-1):
                        info={
                            "t":round(x[i],3),
                            "f":round(f[i],1)
                        }
                        csv_writer.writerow(info)
                        #print(Fs)
                except:
                    print("savet")
        except:
            print("filter")
if __name__ == '__main__':
    target1 = Process(target = saveraw)
    target2 = Process(target = filtering)
    target1.start()
    sleep(5)

    target2.start()
    sleep(3)
