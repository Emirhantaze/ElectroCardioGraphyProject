import serial
import serial.tools.list_ports
import csv
import io
ser = serial.Serial("/dev/ttyACM0")
#print(serial.tools.list_ports.comports().__getitem__(0))

print (ser.readline())