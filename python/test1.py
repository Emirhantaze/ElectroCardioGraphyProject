
#---------Imports
from tkinter.ttk import Combobox
from tkinter import StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
import pandas as pd
#---------End of imports
root = Tk.Tk()
root.title("Electrocardiograhp (ECG) Simulation")
fig = plt.Figure(figsize=(12,7))
#root.attributes("-zoomed", True)
       # x-array


xt=0
def animate(i):
    x=0
    y1=0
    rows=[]
    a=time.time()
    global xt
    data=pd.read_csv('Rawdata.csv',skiprows=xt,usecols=[0,1], names=['t', 'f'])
    temp=len(data)
    print(temp)
    if(temp>600):
        xt=xt+temp-600
    data_top = data.head()  
    print(data_top)
    y1 = data["t"]
    x = data["f"]
    
    ax1.cla()
    
    #y1=y1-3456
    try:
        ax1.plot(x,y1)
    except:
        print()
    print(time.time()-a)
    #ax1.cla()
    
    #y1=y1-mina
    #ax1.plot(x,y1)
    

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

b = Tk.Button(frametop, text="OK", command=callback)
b.pack(side="left")




canvas = FigureCanvasTkAgg(fig, master=root)
#canvas.get_tk_widget().place(relx=0.5, rely=0.025, anchor="n")
canvas.get_tk_widget().pack(side="bottom",fill="x")

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
bpmlabel=Tk.Label(frametop,text="BPM: ")
bpmlabel.pack(side="left")

ani = animation.FuncAnimation(fig, animate, interval=200)
print('succes')
Tk.mainloop()
