import random
import tkinter as tk

from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation #it makes an animation by repeatedly calling a function function
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
root=tk.Tk()
root.geometry('350x200')

def buttonFunction():
   
    print('Hi! Ymir')
btn = tk.Button(root,text=" asd",command=buttonFunction)
btn.grid(column=0,row=0)  

plt.style.use('fivethirtyeight') #just style to make it bold

xvalues = []
yvalues = []

index = count() #you take real time ecg signals from there


def plotting(i):
    xvalues.append(next(index))
    yvalues.append() # there might be y values
    plt.cla()  # clears the axe
    plt.plot(xvalues, yvalues)
    plt.tight_layout()




#ani = FuncAnimation(plt.gcf(), plotting, interval=1000)

plt.tight_layout()
plt.show()

root.mainloop()