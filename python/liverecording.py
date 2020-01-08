import serial
import serial.tools.list_ports
import csv
import time
import re
from decimal import getcontext
#sudo chmod a+rw /dev/ttyACM1
#ser = serial.Serial("/dev/ttyACM1")
#ser = serial.Serial("/dev/cu.usbmodem14101")
ser = serial.Serial("COM4",115200)
fieldnames = ["t","f"]
print(serial.tools.list_ports.comports().__getitem__(0))
with open('Rawdata.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
getcontext().prec = 4
a=time.time()

print(ser.readline().decode())
while True:
    
    try:
       a=str(ser.readline())
       t=re.findall("[0-9]*",a)
       print(t[4])
       with open('Rawdata.csv', 'a') as csv_file:
           csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
           csv_writer.writeheader()
           info = {
                        "f": t[2],
                        "t": t[4]

                            
                        }
           csv_writer.writerow(info)   
    except:
        print("test")

       
