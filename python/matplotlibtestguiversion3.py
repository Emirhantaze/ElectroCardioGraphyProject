import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import GifImagePlugin
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button,Cursor,RadioButtons,Slider
from matplotlib.text import Text
imageObject = Image.open("./test.gif")
imageObject.seek(0)
j=0;
fig = plt.figure(figsize=(12,6),facecolor=(0.129,0.129,0.129))
ax=fig.add_subplot()
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
fig.subplots_adjust(left=0.20,right=0.80,bottom=0.04)
typeSelectorax = plt.axes([0.01,0.71,0.14,0.25])
typeSelector = RadioButtons(typeSelectorax,("none","butter","ellip","cheby"))
slider1ax = plt.axes([0.01,0.26,0.04,0.4])
slider1 = Slider(slider1ax,"low",0.05,5,orientation="vertical")
slider1.label.set_color("white")
slider2ax = plt.axes([0.06,0.26,0.04,0.4])
slider2 = Slider(slider2ax,"low",0.05,5,orientation="vertical")
slider2.label.set_color("white")
slider3ax = plt.axes([0.11,0.26,0.04,0.4])
slider3 = Slider(slider3ax,"low",0.05,5,orientation="vertical")
slider3.label.set_color("white")
plusbuttonax = plt.axes([0.9,0.01,0.1,0.09])
plusim = Image.open("plus.png")
plusbutton = Button(plusbuttonax,"",plusim,color=(0.129,0.129,0.129),hovercolor=(0.15,0.15,0.15))
savebuttonax=plt.axes([0.9,0.13,0.1,0.1])
loadbuttonax=plt.axes([0.9,0.26,0.1,0.1])
saveim = Image.open("save.png")
savebutton = Button(savebuttonax,"",saveim,color=(0.129,0.129,0.129),hovercolor=(0.17,0.15,0.15))
loadim = Image.open("select.png")
loadbutton = Button(loadbuttonax,"",loadim,color=(0.129,0.129,0.129),hovercolor=(0.15,0.15,0.15))
applybuttonax  = plt.axes([0.01,0.12,0.14,0.07])
applybutton = Button(applybuttonax,"apply",color="white",hovercolor=(0.15,0.15,0.15))
ecgax= plt.axes([0.78,0.57,0.30,0.30])
plotSelectorax = plt.axes([0.86,0.38,0.14,0.25])
plotSelector = RadioButtons(plotSelectorax,("Raw ECG","Filtered Ecg","FFT of Filtered","MIXED"))
def update(i):
    global j
    ecgax.cla()
    ecgax.imshow(imageObject)
    #ecgax.title("tetst")
    ecgax.axis("off")
    txt = ecgax.text(400,0,j,verticalalignment='center', horizontalalignment='center',size=50,color="blue")
    if(j>=imageObject.n_frames-7):
        j=0
    else:
        j=j+3
    imageObject.seek(j)

txt = ecgax.text(0.4,0.1,"XX",size=50,color="blue")
ani = FuncAnimation(fig,update,interval=16)
plt.show()