

#---------Imports
from tkinter.ttk import Combobox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

#---------End of imports
matplotlib.use('MacOSX')
root = Tk.Tk()
fig = plt.Figure(figsize=(12,7))
#root.attributes("-zoomed", True)
x = np.arange(0, 2*np.pi, 0.01)        # x-array

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,
frametop =Tk.Frame(root)
frametop.pack(side="top")
v = ["butter", "ellip", "cheby", "none"]
combo = Combobox(frametop, values=v, state="readonly")
combo.set("none")

combo.pack(side="left")
label1 = Tk.Label(frametop,text="LOw Frequency").pack(side="left")
entry1 = Tk.Entry(frametop).pack(side="left")
label2 = Tk.Label(frametop,text="high frequency").pack(side="left")
entry2 = Tk.Entry(frametop).pack(side="left")
label3 = Tk.Label(frametop,text="Order ").pack(side="left")
entry3 = Tk.Entry(frametop).pack(side="left")
def callback():
    print ("click!")

b = Tk.Button(frametop, text="OK", command=callback)
b.pack(side="left")




canvas = FigureCanvasTkAgg(fig, master=root)
#canvas.get_tk_widget().place(relx=0.5, rely=0.025, anchor="n")
canvas.get_tk_widget().pack(side="left")
frameright=Tk.Frame(root)
frameright.pack(side="right")
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
bpmlabel=Tk.Label(frameright,text="BPM: XXX   ")
bpmlabel.pack(side="right")
line, = ax1.plot(x, np.sin(x))
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

Tk.mainloop()
