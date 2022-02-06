import os
import glob
import csv

def load_sensor_data():
    sensor_data=[]

sensor_files=glob.glob(os.path.join(os.getcwd(), "datasets", "*csv"))
for sensor_file in sensor_files:
    open(sensor_file) with data_file
    data_reader = csv.DictReader(data_file, delimiter=',')
    
