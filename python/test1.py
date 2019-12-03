
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import *
from tkinter.ttk import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()
root = Tk()

figure = Figure(figsize=(4, 5), dpi=100)
plot = figure.add_subplot(1, 1, 1)

def animate(i):
    
    
    plot.plot([1,3,5,6])
   
   

   
    

btn = Button(root, text="Click Me")
 
btn.pack(side=tkinter.LEFT)

canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().pack(side=LEFT)
ani = FuncAnimation(figure, animate, interval=1000)

root.mainloop()
root.quit()