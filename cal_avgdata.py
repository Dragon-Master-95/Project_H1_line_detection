import os
import argparse
import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import datetime

def cal_avgdata(data,cal_data,t,timeres,timestamps):
    if t<timeres:
        print("The (averaging time) < (time resolution) of the data")
        print("Thus, polting and saving the same resolution data")
        return data
    
    new_data = np.zeros((int(np.floor(np.shape(data)[0]/t)),np.shape(data)[1]))
    garbage_var = np.zeros((int(np.floor(np.shape(cal_data)[0]/t)),np.shape(cal_data)[1]))
    new_timestamps = []
    for a in range(0,int(np.floor(np.shape(data)[0]/t))):
        new_timestamps.append(timestamps[int(a*t)])
        new_data[int(a),int(0):int(3)] = data[int(a*t),int(0):int(3)]
        try:
            garbage_var[int(a),int(0):int(3)] = cal_data[int(a*t),int(0):int(3)]
        except:
            garbage_var=1
        new_data[int(a),int(3):] = np.mean(data[int(a*t):int(a*t+t),int(3):],axis=0) - np.mean(cal_data[:,int(3):],axis=0)
    new_timestamps=np.asarray(new_timestamps)
    return new_data, new_timestamps
