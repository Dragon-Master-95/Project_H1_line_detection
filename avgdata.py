import os
import argparse
import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import datetime

def avgdata(data,t,timeres,timestamps):
    if (timeres!=None):
        if (t<=timeres):
            print("The (averaging time) <= (time resolution) of the data")
            print("Thus, polting and saving the same resolution data")
        return data
    '''
    if (np.floor_divide(t,timeres)<t/timeres):
        print("The ratio of avgtime and timeresolution is in float.")
        divisor=[]
        for k in range(2,min(t,timeres)+1):
            if t%k == timeres%k == 0:
                divisor.append(k)
        if divisor==[]:
            divisor=2
        print("Thus setting avgtime to be %d seconds",divisor)
    '''
    
    new_data = np.zeros((int(np.floor(np.shape(data)[0]/t)),np.shape(data)[1]))
    new_timestamps = []
    for a in range(0,int(np.floor(np.shape(data)[0]/t))):
        new_timestamps.append(timestamps[int(a*t)])
        new_data[int(a),int(0):int(3)] = data[int(a*t),int(0):int(3)]
        new_data[int(a),int(3):] = np.mean(data[int(a*t):int(a*t+t),int(3):],axis=0)
    new_timestamps=np.asarray(new_timestamps)
    return new_data, new_timestamps
