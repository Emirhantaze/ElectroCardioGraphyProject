from time import sleep
from threading import Thread
import tkinter as Tk
from tkinter.ttk import Combobox
from tkinter import StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import csv #read and write the data
import time
import matplotlib.pyplot as plt #plotting library for python
import numpy as np #scientific computing library which contains Fourier, Linear Algebra etc.
import ecgF  as e
import pandas as pd
#import ecgF as e
from scipy.signal import find_peaks
from decimal import getcontext #fast correctly rounded decimal points aritmetic
def f():
    global filteredsignal,filteredsignaltime
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
        sleep(0.004)
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
                if (say!=0):
                    for i in range(len(f)-say-3,len(f)+1):
                        info={
                            "t":round(x[i],3),
                            "f":round(f[i],1)
                        }
                        filteredsignal=np.append(filteredsignal,round(f[i],1))
                        filteredsignaltime=np.append(filteredsignaltime,round(x[i],3))
                        csv_writer.writerow(info)
            except:
                print()
        temp = len(filteredsignal)
        if(temp>600):
            filteredsignal=filteredsignal[temp-600:temp]
            filteredsignaltime=filteredsignaltime[temp-600:temp]
        print(int(round((c*Fs),0)))
def t():
    fieldnames = ["t", "f"]
    global rawsignal,rawsignaltime

    with open('Rawdata.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    a=round(time.time(),3)
    while True:
        y=np.cos(2*3.14*1*(round((time.time()-a),3)))
        x=round(time.time()-a,4)
        with open('Rawdata.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {
                "f": round(y,2),
                "t": x
                
            }
            rawsignaltime=np.append(rawsignaltime,x)
            rawsignal=np.append(rawsignal,round(y,2))
            csv_writer.writerow(info)
        temp = len(rawsignal)
        if(temp>600):
            rawsignal=rawsignal[temp-600:temp]
            rawsignaltime=rawsignaltime[temp-600:temp]
        time.sleep(0.001)
def tekrarla(ne="a", bekleme=0):
    while True:
        print (ne)
        #sleep(bekleme)

        #sleep(bekleme)
def animate(i):
    a=time.time()
    global filteredsignal,filteredsignaltime,rawsignal,rawsignaltime
    
    #x,y1=e.itself(rawsignaltime,rawsignal)
    #print(x[1])
    x,y1=e.itself(rawsignaltime,rawsignal)
    if(i>4 and (i%5)==0):
        
        ax2.cla()
        ax4.cla()
   
    #y1=y1-3456
    temp=len(x)
    ax1.plot(x[temp-10:temp],y1[temp-10:temp],"r")
    ax1.set_xlim(left=(x[temp-1]-5),right=(x[temp-1]))
    
    x,y=e.myfft(x,y1)
    ax2.plot(x,y,"y") 
    
    
    x,y1=e.itself(filteredsignaltime,filteredsignal)
    
    peaks, _ = find_peaks(y1, distance=110)
    
    #y1=y1-3456
    temp=len(x)
    ax3.plot(x[temp-10:temp],y1[temp-10:temp],"r")
    ax3.plot(x[peaks], y1[peaks], "xr")
    ax3.set_xlim(left=(x[temp-1]-5),right=(x[temp-1]))
    x,y=e.myfft(x,y1)
    ax4.plot(x,y,"y")
    #print(time.time()-a)
    #ax1.cla()
    
    #y1=y1-mina
    #ax1.plot(x,y1)
def callback():
    with open("filter.csv","a") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=["type","lowf","highf","order"])
        
        info = {
                 "type": combo.get(),
                 "lowf": v1.get(),
                 "highf":v2.get(),
                 "order":v3.get()
                
                  }
        csv_writer.writerow(info)
if __name__ == '__main__':
    
    tis = Thread(target = f)#, args = ("tis",0.5))
    ah = Thread(target = t)#, args = ("ah",3))
    filteredsignal=[]
    filteredsignaltime=[]
    rawsignal=[]
    rawsignaltime=[]
    
    ah.start()
    sleep(1)
    tis.start()
    sleep(1)
    root = Tk.Tk()
    root.title("Electrocardiograhp (ECG) Simulation")
    fig = plt.Figure(figsize=(12,7),facecolor='black',edgecolor="black")
    #root.attributes("-zoomed", True)
    root.configure(background="black")      # x-array


    xf=1
    xr=1
    data=pd.read_csv('Filtereddata.csv',skiprows=xf,usecols=[0,1], names=['t', 'f'])
    temp=len(data)
    print(temp)
    if(temp>600):
        xf=xf+temp-600
    data=pd.read_csv('Rawdata.csv',skiprows=xf,usecols=[0,1], names=['t', 'f'])
    temp=len(data)
    print(temp)
    if(temp>600):
        xr=xr+temp-600
    frametop =Tk.Frame(root)
    frametop.pack(side="top")
    v = ["butter", "ellip", "cheby", "none"]
    label = Tk.Label(frametop, text="Filter Type Selection: ").pack(side="left")
    combo = Combobox(frametop, values=v, state="readonly")
    combo.set("none")

    combo.pack(side="left")
    label1 = Tk.Label(frametop,text="Low Frequency").pack(side="left")
    v1 = StringVar()
    entry1 = Tk.Entry(frametop,width=5,textvariable=v1).pack(side="left")
    v2 = StringVar()
    label2 = Tk.Label(frametop,text="High frequency").pack(side="left")
    entry2 = Tk.Entry(frametop,width=5,textvariable=v2).pack(side="left")
    v3 = StringVar()
    label3 = Tk.Label(frametop,text="Order (Cut-off) ").pack(side="left")
    entry3 = Tk.Entry(frametop,width=5,textvariable=v3).pack(side="left")
    b = Tk.Button(frametop, text="OK", command=callback)
    b.pack(side="left")




    canvas = FigureCanvasTkAgg(fig, master=root)
    #canvas.get_tk_widget().place(relx=0.5, rely=0.025, anchor="n")
    canvas.get_tk_widget().pack(side="bottom",fill="x")

    ax1 = fig.add_subplot(221)
    ax1.set_fc("black")
    ax2 = fig.add_subplot(222)
    ax2.set_fc("black")
    ax3 = fig.add_subplot(223)
    ax3.set_fc("black")
    ax4 = fig.add_subplot(224)
    ax4.set_fc("black")
    bpmlabel=Tk.Label(frametop,text="BPM: ")
    bpmlabel.pack(side="left")

    ani = animation.FuncAnimation(fig, animate, interval=10)
    print('succes')
    Tk.mainloop()