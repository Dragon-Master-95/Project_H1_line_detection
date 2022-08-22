import os
import argparse
import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import datetime

def data_flatenning(df):
    last_col = copy.deepcopy(df.columns[-1])
        
    df['DateTime'] = pd.to_datetime(df[0]+df[1])
    df['DateTime'].dt.strftime('%Y-%m-%d %H:%M:%S')
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

