import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import GifImagePlugin
import scipy.io
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button,Cursor,RadioButtons,Slider,CheckButtons
from matplotlib.text import Text
import pandas as pd
import serial
import ecgF  as e
import csv
import time
from time import sleep
from scipy.signal import find_peaks
from serial.tools import list_ports
import easygui
ports=[];
load_f=[]
load_t=[]
selected_port="";
ser=serial.Serial()

ser.port=easygui.enterbox("please enter your portname","choose a port")
ser.baudrate=115200
ser.open()

filetypes = [ ["*.csv", "*.Csv", "CSV files"] ,["All files","*"] ]
ser.reset_input_buffer()
taken = str(ser.readline())
taken = str(ser.readline())
taken = str(ser.readline())
taken = str(ser.readline())
imageObject = Image.open("./test.gif")
imageObject.seek(0)
j=0
instant_t=[1]
instant_f=[1]
f=[1]
t=[1]


flag=True
flag1=False
fig = plt.figure(figsize=(8,4.5),facecolor=(0.129,0.129,0.129))
ax3=fig.add_subplot(212)
line3, =ax3.plot([0],[0])
ax2=fig.add_subplot(211)
line2, =ax2.plot([0],[0])
ax1=fig.add_subplot(111)
line1, =ax1.plot([0],[0])
line11, =ax1.plot([0],[0],"*r")
line22, =ax2.plot([0],[0],"*r")
line11.set_data([],[])
line22.set_data([],[])
line1.set_data([],[])
line2.set_data([],[])
line3.set_data([],[])
ax1.tick_params(axis='x', colors='white')
ax1.tick_params(axis='y', colors='white')
ax2.tick_params(axis='x', colors='white')
ax2.tick_params(axis='y', colors='white')
ax3.tick_params(axis='x', colors='white')
ax3.tick_params(axis='y', colors='white')
fig.subplots_adjust(left=0.20,right=0.80,bottom=0.2,top=0.95)
typeSelectorax = plt.axes([0.01,0.71,0.14,0.25])
typeSelector = RadioButtons(typeSelectorax,("none","filter"))
slider1ax = plt.axes([0.01,0.26,0.04,0.4])
slider1 = Slider(slider1ax,"low",0.05,10,orientation="vertical",color=(0.15, 0.00, 0.20))
slider1.label.set_color("white")

slider1.valtext.set_color("white")
slider2ax = plt.axes([0.06,0.26,0.04,0.4])
slider2 = Slider(slider2ax,"high",1,60,orientation="vertical",color=(0.15, 0.00, 0.20))
slider2.label.set_color("white")
slider3ax = plt.axes([0.11,0.26,0.04,0.4])
slider3 = Slider(slider3ax,"order",1,5,2,orientation="vertical",valstep=1,color=(0.15, 0.00, 0.20))
slider3.label.set_color("white")
slider4ax = plt.axes([0.20,0.07,0.6,0.07])
slider4 = Slider(slider4ax,"X-leftside",0,1,0.7,color=(0.15, 0.00, 0.20))
slider4.label.set_color("white")
slider5ax = plt.axes([0.20,0.0,0.6,0.07])
slider5 = Slider(slider5ax,"X-rightside",0,1,1,color=(0.15, 0.00, 0.20))
slider5.label.set_color("white")
slider2.valtext.set_color("white")
slider3.valtext.set_color("white")
slider4.valtext.set_color("white")
slider5.valtext.set_color("white")
plusbuttonax = plt.axes([0.9,0.01,0.1,0.09])
plusim = Image.open("plus.png")
plusbutton = Button(plusbuttonax,"",plusim,color=(0.129,0.129,0.129),hovercolor=(0.15,0.15,0.15))
savebuttonax=plt.axes([0.9,0.13,0.1,0.1])
loadbuttonax=plt.axes([0.9,0.26,0.1,0.1])
saveim = Image.open("save.png")
savebutton = Button(savebuttonax,"",saveim,color=(0.129,0.129,0.129),hovercolor=(0.17,0.15,0.15))
loadim = Image.open("select.png")
loadbutton = Button(loadbuttonax,"",loadim,color=(0.129,0.129,0.129),hovercolor=(0.15,0.15,0.15))
ecgax= plt.axes([0.78,0.57,0.30,0.30])
plotSelectorax = plt.axes([0.86,0.38,0.14,0.25])
plotSelector = RadioButtons(plotSelectorax,("Raw ECG","Filtered Ecg","FFT of Filtered","MIXED"))
checkboxax= plt.axes([0.01, 0.15, 0.14, 0.07])
checkboxax.set_facecolor((0.22, 0.19, 0.23))
checkbox=CheckButtons(checkboxax,["Zero Phase"])
checkbox.labels[0].set_color("white")
checkbox.lines[0][0].set_color("white")
checkbox.lines[0][0].set_data([0,1],[0,1])
checkbox.lines[0][1].set_data([0,1],[1,0])
checkbox.lines[0][1].set_color("white")
checkbox.rectangles[0].set_visible(0)
ax1.set_visible(True)
ax2.set_visible(False)
ax3.set_visible(False)

def update(i):
    global j,t,f,instant_f,instant_t,flag
    ecgax.clear()
    ecgax.imshow(imageObject)
    #ecgax.title("tetst")
    ecgax.axis("off")

    if(j>=imageObject.n_frames-11):
        j=0
    else:
        j=j+3
    imageObject.seek(j)

    if flag:
        while ser.in_waiting>0:

            try:
                taken = str(ser.readline().decode().strip('\r\n'))
                val=taken.split(" ")
                f.append(float(val[0])-600)
                t.append(int(val[1])/1000)
                instant_f.append(float(val[0])-600)
                instant_t.append(int(val[1])/1000)
            
                if(len(instant_f)>4500):
                    instant_f.pop(0)
                    instant_t.pop(0)
            except:
                pass
    else:
        instant_f=load_f
        instant_t=load_t
        t=[]
        f=[]
    #instant_f=(np.asarray(instant_f)-np.mean(instant_f)).tolist()
    if(len(instant_f)>1200):
        Fs = 1/np.mean(np.diff(instant_t))
        print(Fs)
        if Fs<50:
            Fs=350
        #print(1/np.mean(np.diff(instant_t)))
        
        if(plotSelector.value_selected=="Raw ECG"):
            try:
                if(len(instant_f)==len(instant_t)):
                    
                    line1.set_data(instant_t,instant_f)
                else:
                    pass
                peaks, _ = find_peaks(instant_f, distance=int((60/180)*Fs),height=90)
                try:
                    temp=len(peaks)
                    bpm=60/np.mean(np.diff(np.asarray(instant_t)[peaks[temp-12:temp-2]]))
                    txt = ecgax.text(400,0,int(bpm),verticalalignment='center', horizontalalignment='center',size=50,color="blue")
                except:
                    pass
                
                line11.set_data(np.asarray(instant_t)[peaks],np.asarray(instant_f)[peaks])
                ax1.set_xlim(left=(instant_t[len(instant_t)-2]-instant_t[1])*slider4.val+instant_t[1],right=(instant_t[len(instant_t)-2]-instant_t[1])*slider5.val+instant_t[1]+2)
                ax1.set_ylim(bottom=np.min(instant_f[1000:])-50,top=np.max(instant_f[1000:])+50)
            except:
                pass
            pass
        elif(plotSelector.value_selected=="Filtered Ecg"):
            if(typeSelector.value_selected=="filter"):
                filtered_f=e.butter_bandpass_filter(instant_f,slider1.val,slider2.val,Fs,np.round(slider3.val,0),checkbox.get_status()[0])

            else:
                filtered_f=instant_f
            line1.set_data(instant_t,filtered_f)
            peaks, _ = find_peaks(filtered_f, distance=int((60/180)*Fs),height=90)
            try:
                temp=len(peaks)
                bpm=60/np.mean(np.diff(np.asarray(instant_t)[peaks[temp-12:temp-2]]))
                txt = ecgax.text(400,0,int(bpm),verticalalignment='center', horizontalalignment='center',size=50,color="blue")
            except:
                pass
            line11.set_data(np.asarray(instant_t)[peaks],np.asarray(filtered_f)[peaks])        
            ax1.set_xlim(left=(instant_t[len(instant_t)-2]-instant_t[1])*slider4.val+instant_t[1],right=(instant_t[len(instant_t)-2]-instant_t[1])*slider5.val+instant_t[1]+2)
            ax1.set_ylim(bottom=np.min(filtered_f[1000:])-50,top=np.max(filtered_f[1000:])+50)
            pass
        elif(plotSelector.value_selected=="FFT of Filtered"):
            if(len(instant_f)==len(instant_t)):
                a,b = e.myfft(instant_t,instant_f)
                line1.set_data(a,b)
                line11.set_data([],[])
                ax1.set_xlim(right=100,left=-5)
                ax1.set_ylim(bottom=-0.5,top=np.max(b)+0.1)
            else:
                pass
            pass
        else:
            if(typeSelector.value_selected=="filter"):
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
            ax2.set_xlim(left=(instant_t[len(instant_t)-2]-instant_t[1])*slider4.val+instant_t[1],right=(instant_t[len(instant_t)-2]-instant_t[1])*slider5.val+instant_t[1]+2)
            ax2.set_ylim(bottom=np.min(filtered_f[1000:])-50,top=np.max(filtered_f[1000:])+50)
            if(len(instant_f)==len(instant_t)):
                a,b = e.myfft(instant_t,instant_f)
                line3.set_data(a,b)
                ax3.set_xlim(right=100,left=-5)
                ax3.set_ylim(bottom=-0.5,top=np.max(b)+0.1)
            else:
                pass
            pass
    else:
        try:
            instant_f.pop(0)
            instant_t.pop(0)
        except:
            pass

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
        ser.close()
        ata=time.time()
        while(time.time()-ata<0.1):
            pass
        if(flag1):
            pass
    else:
        ser.open()
        ser.reset_input_buffer()
        flag=1
def load(label):
    global load_f,load_t,flag
    flag=False
    ata=time.time()
    while(time.time()-ata<0.1):
        pass
    ser.close()
    path = None
    while path == None :
        path=easygui.fileopenbox(title="open",filetypes=filetypes,default="*.csv")
    data = pd.read_csv(path)
    
    load_f = data['f'].values.tolist()
    load_t = data['t'].values.tolist()

def save(label):
    global t, f
    path = None
    while path == None :
        path=easygui.filesavebox(title="save",filetypes=filetypes,default="*.csv")
    with open(path,"w") as csv_file:
        
        csv_writer = csv.DictWriter(csv_file, fieldnames=["t","f"])
        csv_writer.writeheader()
            
        try:
            for i in range(1200,len(f)-1):
                info={
                    "t":round(t[i],3),
                    "f":round(f[i],1)
                }
                csv_writer.writerow(info)
                #print(Fs)
        except:
            print("save error!!") 

    
loadbutton.on_clicked(load)
plotSelector.on_clicked(axdefiner)
plusbutton.on_clicked(start_stop)
savebutton.on_clicked(save)
ani = FuncAnimation(fig,update,interval=10)
plt.show()