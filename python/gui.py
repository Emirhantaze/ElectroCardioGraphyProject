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
from matplotlib import style


def animate(i):
    try:
        
        a=time.time()
        data = pd.read_csv('Rawdata.csv')
        temp=len(data['t'])
        y1 = data['f'][temp-2000:temp].values
        x = data['t'][temp-2000:temp].values
        Fs = 1/(np.mean(np.diff(x)))
        rn=np.arange(1,400)
        rn=rn*5
        peaks, _ = find_peaks(y1, distance=int((60/110)*Fs))       
        print(Fs)
        v.set("BPM: "+str(60/np.mean(np.diff(x[peaks[1:len(peaks)]]))))
        line11.set_data(x[rn],y1[rn])
        line12.set_data(x[peaks],y1[peaks])
        ax1.set_xlim(right=x[1999],left=x[1999]-3)
        ax1.set_ylim(bottom=np.mean(y1)-100,top=np.mean(y1)+100)
        data = pd.read_csv('Filtereddata.csv')
        temp=len(data['t'])
        y1 = data['f'][temp-2000:temp].values
        x = data['t'][temp-2000:temp].values
        Fs = 1/(np.mean(np.diff(x)))
        peaks, _ = find_peaks(y1, distance=int((60/110)*Fs))       
        line21.set_data(x[rn],y1[rn])
        line22.set_data(x[peaks],y1[peaks])
        ax2.set_xlim(right=x[1999],left=x[1999]-3)
        ax2.set_ylim(bottom=np.mean(y1)-100,top=np.mean(y1)+100)
        v.set("BPM: "+str(round(60/np.mean(np.diff(x[peaks[len(peaks)-4:len(peaks)-2]])),1)))
        
        
        
        
    except:
        print("animate")

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
    sleep(3)
    
    
    
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
    style.use('ggplot')
    ax1 = fig.add_subplot(221)
    ax1.set_fc((0.16, 0.19, 0.20))
    line11, = ax1.plot([], [],"b")
    line12, = ax1.plot([], [],"xr")
    ax1.set_title("Raw ECG")
    ax2 = fig.add_subplot(222)
    line21, = ax2.plot([], [],"b")
    line22, = ax2.plot([], [],"xr")
    ax2.set_fc((0.16, 0.19, 0.20))
    ax3 = fig.add_subplot(223)
    ax3.set_fc((0.16, 0.19, 0.20))
    ax3.set_title("fft")
    ax4 = fig.add_subplot(224)
    ax4.set_fc((0.16, 0.19, 0.20))
    ax4.set_title("x")
    ax1.set_ylim(bottom=0,top=500)
    ax2.set_ylim(bottom=-300,top=600)
    v=StringVar()
    bpmlabel=Tk.Label(frametop,textvariable=v)
    v.set("bpm= ")
    bpmlabel.pack(side="left")
    ani = FuncAnimation(fig,animate,interval=33)
    root.mainloop()
