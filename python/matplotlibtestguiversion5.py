import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time
from PIL import GifImagePlugin
#from matplotlib.animation import FuncAnimation
import scipy.io
from matplotlib.widgets import Button,Cursor,RadioButtons,Slider
from matplotlib.text import Text
import pandas as pd
import serial
import ecgF  as e
from time import sleep
from scipy.signal import find_peaks
from serial.tools import list_ports
import easygui
from drawnow import drawnow
ports=[];
load_t=np.linspace(0,10,1000)
load_f=np.sin(2*3.14*np.linspace(0,10,1000))
selected_port="";
for x in list_ports.comports():
    ports.append(x)
selected_portname=easygui.choicebox(msg='Pick something.', title=' ', choices=(ports))
for x in ports:
    
    if(str(x)==selected_portname):
        selected_port=x.device
#ser=serial.Serial(selected_port,115200)
#print(selected_port)
filetypes = [ ["*.csv", "*.Csv", "CSV files"] ,["All files","*"] ]
#ser.reset_input_buffer()
#ser.readline()
sleep(1)
imageObject = Image.open("./test.gif")
imageObject.seek(0)
j=0
instant_t=[1,34,2]
instant_f=[1,1,35]
f=[1]
t=[1]
mat = scipy.io.loadmat('../datas/31.10.2019.mat') #loading matlab file

t=mat['t9'][0] #What are the purpose of them?
f=-mat['f9'][0]
flag=False
fig = plt.figure(figsize=(8,4.5),facecolor=(0.129,0.129,0.129))
ax3=fig.add_subplot(212)
line3, =ax3.plot([0],[0])
ax2=fig.add_subplot(211)
line2, =ax2.plot([0],[0])
ax1=fig.add_subplot(111)
line1, =ax1.plot([0,1],[0,1])
line11, =ax1.plot([0],[0],"*r")
line22, =ax2.plot([0],[0],"*r")
line11.set_data([],[])
line22.set_data([],[])
#line1.set_data([],[])
line2.set_data([],[])
line3.set_data([],[])
ax1.tick_params(axis='x', colors='white')
ax1.tick_params(axis='y', colors='white')
ax2.tick_params(axis='x', colors='white')
ax2.tick_params(axis='y', colors='white')
ax3.tick_params(axis='x', colors='white')
ax3.tick_params(axis='y', colors='white')
fig.subplots_adjust(left=0.20,right=0.80,bottom=0.04)
typeSelectorax = plt.axes([0.01,0.71,0.14,0.25])
typeSelector = RadioButtons(typeSelectorax,("none","butter","ellip","cheby"))
slider1ax = plt.axes([0.01,0.26,0.04,0.4])
slider1 = Slider(slider1ax,"low",0.05,10,orientation="vertical")
slider1.label.set_color("white")
slider2ax = plt.axes([0.06,0.26,0.04,0.4])
slider2 = Slider(slider2ax,"high",1,60,orientation="vertical")
slider2.label.set_color("white")
slider3ax = plt.axes([0.11,0.26,0.04,0.4])
slider3 = Slider(slider3ax,"order",0,5,orientation="vertical")
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
ax1.set_visible(True)
ax2.set_visible(False)
ax3.set_visible(False)

def axdefiner(label):
    if(label=="MIXED"or False):
        ax2.set_title(plotSelector.value_selected)
        ax1.set_visible(False)
        ax2.set_visible(True)
        ax3.set_visible(True)
    else:
        ax1.set_title(plotSelector.value_selected)
        ax1.set_visible(True)
        ax2.set_visible(False)
        ax3.set_visible(False)
def start_stop(label):
    global flag,instant_f,instant_t
    if(flag==1):
        flag=0
    else:
        ser.reset_input_buffer()
        instant_f=[]
        instant_t=[]
        flag=1
def load(label):
    global load_f,load_t,flag
    flag=False
    print(type(instant_f))
    path=easygui.fileopenbox(title="test",filetypes=filetypes,default="*.csv")
    data = pd.read_csv(path)
    
    load_f = data['f'].values.tolist()
    load_t = data['t'].values.tolist()


    
    
    
loadbutton.on_clicked(load)
plotSelector.on_clicked(axdefiner)
plusbutton.on_clicked(start_stop)
i=1.0

while 1:
    aaa=time.time()
    i=i+7
    load_t=np.linspace(0+i/100,10+i/100,100)
    print(0+i/10)
    load_f=np.sin(2*3.14*np.linspace(0+i/100,10+i/100,100))
    
    if flag:
        while ser.in_waiting>0:
            
            try:
                taken = str(ser.readline().decode().strip('\r\n'))
                val=taken.split(" ")
                f.append(float(val[0]))
                t.append(int(val[1])/1000)
                instant_f.append(float(val[0]))
                instant_t.append(int(val[1])/1000)
            
                if(len(instant_f)>2001):
                    instant_f.pop(0)
                    instant_t.pop(0)
            except:
                pass
    else:
        instant_f=f
        instant_t=t

    
    if(plotSelector.value_selected=="Raw ECG"):
        try:
            if(len(instant_f)==len(instant_t)):
                ax1.cla()
                
                ax1.plot(instant_t,instant_f,"g")
            else:
                pass
            peaks, _ = find_peaks(instant_f, distance=int((60/110)*Fs),height=90)
            try:
               pass
                
            except:
                pass
            
            line11.set_data(np.asarray(instant_t)[peaks],np.asarray(instant_f)[peaks])
            ax1.set_xlim(right=instant_t[len(instant_t)-1]+2,left=instant_t[len(instant_t)-1]-7)
            ax1.set_ylim(bottom=np.mean(instant_f)-150,top=np.mean(instant_f)+150)
        except:
            pass
        pass
    elif(plotSelector.value_selected=="Filtered Ecg"):
        if(typeSelector.value_selected=="butter"):
            filtered_f=e.butter_bandpass_filter(instant_f,slider1.val,slider2.val,Fs,np.round(slider3.val,0))
        else:
            filtered_f=instant_f
        line1.set_data(instant_t,filtered_f)
        peaks, _ = find_peaks(instant_f, distance=int((60/110)*Fs),height=90)
        try:
            bpm=60/np.mean(np.diff(np.asarray(instant_t)[peaks[np.arange(0,len(peaks))]]))
            txt = ecgax.text(400,0,int(bpm),verticalalignment='center', horizontalalignment='center',size=50,color="blue")
        except:
            pass
        line11.set_data(np.asarray(instant_t)[peaks],np.asarray(filtered_f)[peaks])        
        ax1.set_xlim(right=instant_t[len(instant_t)-1]+2,left=instant_t[len(instant_t)-1]-4)
        ax1.set_ylim(bottom=np.mean(filtered_f)-50,top=np.mean(filtered_f)+50)
        pass
    elif(plotSelector.value_selected=="FFT of Filtered"):
        if(len(instant_f)==len(instant_t)):
            a,b = e.myfft(instant_t,instant_f)
            line1.set_data(a,b)
            line11.set_data([],[])
            ax1.set_xlim(right=50,left=-5)
            ax1.set_ylim(bottom=-10,top=150)
        else:
            pass
        pass
    else:
        if(typeSelector.value_selected=="butter"):
            filtered_f=e.butter_bandpass_filter(instant_f,slider1.val,slider2.val,Fs,np.round(slider3.val,0))
        else:
            filtered_f=instant_f
        line2.set_data(instant_t,filtered_f)
        peaks, _ = find_peaks(instant_f, distance=int((60/110)*Fs),height=90)
        try:
            bpm=60/np.mean(np.diff(np.asarray(instant_t)[peaks[np.arange(0,len(peaks))]]))
            txt = ecgax.text(400,0,int(bpm),verticalalignment='center', horizontalalignment='center',size=50,color="blue")
        except:
            pass
        line22.set_data(np.asarray(instant_t)[peaks],np.asarray(filtered_f)[peaks])        
        ax2.set_xlim(right=instant_t[len(instant_t)-1]+2,left=instant_t[len(instant_t)-1]-7)
        ax2.set_ylim(bottom=np.mean(filtered_f)-150,top=np.mean(filtered_f)+150)
        if(len(instant_f)==len(instant_t)):
            a,b = e.myfft(instant_t,instant_f)
            line3.set_data(a,b)
            ax3.set_xlim(right=70,left=-5)
            ax3.set_ylim(bottom=-5,top=100)
        else:
            pass
        pass

    sleep(0.07)
    ax1.set_title(np.round(time.time()-aaa,3))
    
    plt.pause(0.01)

