import os
import argparse
import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import datetime

os.system('python3 data_flatenning.py')

print("Loading file....")
try:
    df = pd.read_table(inpf, delimiter=',',header=None)
except:
    print("File Path Error.....\n......Aborting......")


try:
    print("Starting Calibration and Averaging....")
    cal_df = pd.read_table(cal_file, delimiter=',',header=None)
    cal_data, unique_timestamps = data_flatenning(cal_df)
    data, unique_timestamps = data_flatenning(df) 
    data_averaged, timestamps = cal_avgdata(data,cal_data,t,timeres,unique_timestamps)
except:
    print("No calibration file found....\nStarting only Averaging.....")
    data, unique_timestamps = data_flatenning(df)
    data_averaged, timestamps = avgdata(data,t,timeres,unique_timestamps)


print("Averaging Done and Plotting Started!!!!!")
plotting_data(data_averaged,pfile,timestamps)

if dt!=None:
    print("Starting interactive plot saving as delta time is specified.......")
    inter_plot(data_averaged,timestamps,dt,f1,f2,pfile)


print("Done!!!!")
