import serial
import serial.tools.list_ports
import csv
from time import sleep
import time
import pandas as pd
import ecgF  as e
from tkinter.ttk import Combobox
from tkinter import StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib
from matplotlib.animation import FuncAnimation
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import find_peaks
from multiprocessing import Process
def saveraw():
    ser = serial.Serial("COM5")
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
            
            
                
                

                info = {
                    "f": ser.readline().decode(),
                    "t": np.round(s,4)

                        
                    }
                csv_writer.writerow(info)
        except:
            print("saveerr")       
                
           
      
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
            sleep(0.001)
            
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
                    for i in range(len(f)-say,len(f)-1):
                        info={
                            "t":round(x[i],3),
                            "f":round(f[i],1)
                        }
                        csv_writer.writerow(info)
                        print(Fs)
                except:
                    print("savet")
        except:
            print("filter")
def animate(i):
    try:
        data = pd.read_csv('Rawdata.csv')
        temp=len(data['t'])
        y1 = data['f'][temp-500:temp].values
        x = data['t'][temp-500:temp].values
        Fs = 1/(np.mean(np.diff(x)))
        peaks, _ = find_peaks(y1, distance=int((60/110)*Fs))
        ax1.plot(x,y1,"r")
        ax1.plot(x[peaks],y1[peaks],"xy")
        ax1.set_xlim(left=float(data['t'][temp-1])-5,right=float(data['t'][temp-1]))
        data = pd.read_csv('Filtereddata.csv')
        temp=len(data['t'])
        y1 = data['f'][temp-500:temp].values
        x = data['t'][temp-500:temp].values
        
        ax3.plot(x,y1,"r")
        ax3.set_xlim(left=float(data['t'][temp-1])-5,right=float(data['t'][temp-1]))
        peaks, _ = find_peaks(y1, distance=150)
        ax3.plot(x[peaks],y1[peaks],"xy")
        v.set("bpm: "+str(round(np.mean(np.diff(x[peaks]))*60/(len(peaks)-1),2)))
    except:
        print("animate")
def guifunc():
    time.sleep(1)
    
    
    
    

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
    target1 = Process(target = saveraw)
    target2 = Process(target = filtering)
    
    target1.start()
    sleep(10)
    target2.start()
    sleep(10)
    
    
    
    root = Tk.Tk()
    root.title("Electrocardiograhp (ECG) Simulation")
    fig = plt.Figure(figsize=(12,7),facecolor=(0.48, 0.48, 0.48),edgecolor="white")
    #root.attributes("-zoomed", True)
    root.configure(background="white")      # x-array



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
    global ax1
    ax1 = fig.add_subplot(221)
    ax1.set_fc((0.16, 0.19, 0.20))
    ax1.set_title("Raw ECG")
    ax2 = fig.add_subplot(222)
    ax2.set_fc((0.16, 0.19, 0.20))
    ax3 = fig.add_subplot(223)
    ax3.set_fc((0.16, 0.19, 0.20))
    ax3.set_title("fft")
    ax4 = fig.add_subplot(224)
    ax4.set_fc((0.16, 0.19, 0.20))
    ax4.set_title("x")
    line1 = ax1.plot()
    v=StringVar()
    bpmlabel=Tk.Label(frametop,textvariable=v)
    v.set("bpm= ")
    bpmlabel.pack(side="left")
    ani = FuncAnimation(fig,animate,interval=100)
    root.mainloop()
