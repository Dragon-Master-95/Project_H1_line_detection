#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 11:05:22 2022

@author: Dragon_Master
"""

import argparse
import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import datetime

global low, up
parser = argparse.ArgumentParser()

#-h help, 
#-ip input filename with path, 
#-io filename with path, 
#-t average time in seconds (default = 10s)
#-plt plot file name

parser.add_argument("-ip","--inputfile", help="input filename with path")
parser.add_argument("-io","--outputfile", help="output filename with path")
parser.add_argument("-t","--avgtime", help="average time in seconds (default = 10s)")
parser.add_argument("-plt","--plotfilename", help="plot the and save the filename with path")
parser.add_argument("-res","--timeres", help="time resolution of data in seconds (default = 1s)")
parser.add_argument("-cali","--calibrationfile", help="To remove system error provide clibration file path (default setting is to plot non calibrated result)")
parser.add_argument("-l","--lowercutoff", help="lower cutoff for waterfall plot")
parser.add_argument("-u","--uppercutoff", help="lower cutoff for waterfall plot")

args = parser.parse_args()

if args.avgtime==None :
    t = 10
else:
    t = float(args.avgtime)
if args.outputfile==None :
    opf = args.inputfile + '_averaged_t_'+str(t)+'s.csv'
else:
    opf = args.outputfile
if args.plotfilename==None:
    pfile = args.inputfile + '_averaged_t_'+str(t)+'s.png'
else:
    pfile = args.plotfilename
if args.timeres==None :
    timeres=1
else:
    timeres = args.timeres
if args.inputfile==None :
    print("Error.... No Input file detected..... \n..............Aborting...............")
    exit(0)
inpf = args.inputfile
cal_file = args.calibrationfile

if args.lowercutoff==None:
    low = -100
else:
    low = args.lowercutoff

if args.uppercutoff==None:
    up = -100
else:
    up = args.uppercutoff


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\FUNCTIONS//////////////////////////////////
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
    
    
    
def avgdata(data,t,timeres,timestamps):
    if t<timeres:
        print("The (averaging time) < (time resolution) of the data")
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
        

def plotting_data(data,fname,timestamps):
    
    x = np.linspace(data[1,1],data[1,2],np.shape(data)[1]-3)/1e+6
    y = np.arange(0,np.shape(data)[0])
    ylabel = timestamps
    z = data[:,3:]
#    z[np.where(z<=np.min(z)+37)] = -6
#    z = z+20
    print(len(np.where(z<=np.min(z)+25)[0]),len(np.where(z<=np.min(z)+25)[1]))
#    z = z/np.max(z)
    
#    data_thresh=np.where(z>-5.0)
#    z_old=z
#    z[data_thresh]=np.nan    


    
    h1 = plt.figure()
    if(low!=-100 and up!=-100):
        ax = plt.pcolor(x,y,z,cmap='jet', vmin=low, vmax=up)#vmin=np.min(z), vmax=np.max(z))
    elif(low!=-100):
        ax = plt.pcolor(x,y,z,cmap='jet', vmin=low, vmax=np.max(z))
    elif(up!=-100):
        ax = plt.pcolor(x,y,z,cmap='jet', vmin=np.min(z), vmax=up)
    else:
        ax = plt.pcolor(x,y,z,cmap='jet', vmin=np.min(z), vmax=np.max(z))
    plt.xlabel('Frequency (in MHz)')
    plt.ylabel('Time (in IST)')
    k = np.arange(0,y[-1],y[-1]/11)
    plt.yticks(y[k.astype(int)],ylabel[k.astype(int)])
    h1.colorbar(ax)
    h1.tight_layout()
    plt.grid()
    h1.savefig(fname)
    
    h2 = plt.figure()
    plt.plot(x,np.mean(z,axis=0))
    plt.xlabel('Frequency (in MHz)')
    plt.ylabel('Magnitude')
    h2.tight_layout()
    plt.grid()
    name = fname[:-3]+'time_avg.png'
    h2.savefig(name)
    
    h3 = plt.figure()
    plt.plot(ylabel,np.mean(z,axis=1))
    plt.xlabel('Time')
    plt.ylabel('Magnitude')
    plt.xticks(rotation=90)
    h3.tight_layout()
    plt.grid()
    name = fname[:-3]+'freq_avg.png'
    h3.savefig(name)
    
    plt.show()
    
def data_flatenning(df):
    last_col = copy.deepcopy(df.columns[-1])
        
    df['DateTime'] = pd.to_datetime(df[0]+df[1])
    unique_timestamps = df['DateTime'].unique()
        
    if (len(unique_timestamps)==len(df)):
        data = np.zeros((df.shape[0],df.shape[1]-4))
        data[:,0] = unique_timestamps
        data_col_indx = np.arange(6,last_col+1)
        freq_col_indx = np.arange(2,4)
        data[:,1:3] = df[freq_col_indx].to_numpy()
        data[:,3:] = df[data_col_indx].to_numpy()
    else:
        print("Starting Data Flatening.....")
        scanlength = len(df.index[df['DateTime']==df['DateTime'].unique()[0]])
        data_col_indx = np.arange(6,last_col+1)
        freq_col_indx = np.arange(2,4)
        data_mat = df[data_col_indx].to_numpy()
        freq_mat = df[freq_col_indx].to_numpy()
        total_col = scanlength*len(data_col_indx)
        data_mat_unfolded = np.zeros((int(len(df)/scanlength), total_col))
        freq_mat_unfolded = np.zeros((int(len(df)/scanlength), len(freq_col_indx)))
        
        i = 0
        k=[]
        for i in range(0,int(len(df)/scanlength)):
            for j in range(0,scanlength):
                data_mat_unfolded[i,j*len(data_col_indx):j*len(data_col_indx)+len(data_col_indx)] = data_mat[i*8+j,:]
                k.append([j*scanlength,j*scanlength+len(data_col_indx), i*8+j ])
            freq_mat_unfolded[i,0] = freq_mat[i*8,0]
            freq_mat_unfolded[i,1] = freq_mat[i*8-1,1]
        
        print("Flatening Done....")
        rows = len(data_mat_unfolded)
        col = total_col+3
        data = np.zeros((rows,col))
        
        data[:,0] = unique_timestamps
        data[:,1:3] = freq_mat_unfolded
        data[:,3:] = data_mat_unfolded
    
    return data,unique_timestamps

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\MAIN CODE//////////////////////////////////


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


print("Done!!!!")

        
    
    
    
