
"""
#---------Imports
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#---------End of imports

fig = plt.Figure()
    # x-array

def animate(i):
    print()

root = Tk.Tk()

#combo = Tk.Combobox(root, ftype=1, low=2, high= 3)




plt1 = fig.add_subplot(2221)
plt2 = fig.add_subplot(2222)
plt3 = fig.add_subplot(2223)
plt4 = fig.add_subplot(2224)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place()



ani = animation.FuncAnimation(fig, animate, interval=30)

Tk.mainloop()

"""
#---------Imports
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
from tkinter.ttk import Combobox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#---------End of imports

fig = plt.Figure(figsize=(10,10))

x = np.arange(0, 2*np.pi, 0.01)        # x-array

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,

root = Tk.Tk()
v = ["butter", "ellip", "cheby","none"]
combo =Combobox(root, values=v)

combo.set("none")
combo.grid(row=0,column=0)
root.geometry("900x720")
label = Tk.Label(root,text="SHM Simulation").place()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(relx=0.5, rely=0.1,anchor="n")

ax = fig.add_subplot(111)
line, = ax.plot(x, np.sin(x))
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

Tk.mainloop()
