 
import csv
import random
import time
import numpy as np

fieldnames = ["f", "t"]


with open('Rawdata.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
a=round(time.time(),3)
while True:
    y=np.cos(2*3.14*1*(round((time.time()-a),3)))
    x=time.time()-a
    with open('Rawdata.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "f": y,
            "t": x
            
        }

        csv_writer.writerow(info)
        
    time.sleep(0.005)