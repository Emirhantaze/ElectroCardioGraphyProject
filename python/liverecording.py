import serial
import serial.tools.list_ports
import csv
import time
from decimal import getcontext
#sudo chmod a+rw /dev/ttyACM1
#ser = serial.Serial("/dev/ttyACM1")
#ser = serial.Serial("/dev/cu.usbmodem14101")
ser = serial.Serial("COM3",115200)
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
                "t": round(s,4)

                
                }
            print(round(s,4))

            csv_writer.writerow(info)
     
            
    except:
        print()

       