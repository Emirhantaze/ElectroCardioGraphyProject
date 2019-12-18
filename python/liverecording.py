import serial
import serial.tools.list_ports
import csv
import time
from decimal import getcontext
#sudo chmod a+rw /dev/ttyACM1
#ser = serial.Serial("/dev/ttyACM1")
#ser = serial.Serial("/dev/cu.usbmodem14101")
ser = serial.Serial("COM5")
fieldnames = ["t","f"]
print(serial.tools.list_ports.comports().__getitem__(0))
with open('Rawdata.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
getcontext().prec = 4
a=time.time()

print(ser.readline().decode())
while True:
    s=time.time()-a
    try:
   
        with open('Rawdata.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {
                "f": ser.readline().decode(),
                "t": ((s*1000-(s*1000)%1))/1000

                
                }
            
            rawsignaltime=np.append(rawsignaltime,x)
            rawsignal=np.append(rawsignal,round(y,2))
            csv_writer.writerow(info)
        temp = len(rawsignal)
        if(temp>600):
            rawsignal=rawsignal[temp-600:temp]
            rawsignaltime=rawsignaltime[temp-600:temp]
    except:
        print()

       