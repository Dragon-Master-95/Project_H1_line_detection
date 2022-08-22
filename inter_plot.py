import os
import argparse
import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import datetime

def inter_plot(data,timestamps,dt,f1,f2,fname):
    x = np.linspace(data[1,1],data[1,2],np.shape(data)[1]-3)/1e+6 #freqencies
    y = pd.DataFrame(timestamps,columns=['Timestamp'])
    z = data[:,3:] 
    
    hrs =  y['Timestamp'].dt.hour.to_numpy()
    m = y['Timestamp'].dt.minute.to_numpy()
    s = y['Timestamp'].dt.second.to_numpy()
    hrs = hrs+m/60+s/3600
    for i in range(0,len(hrs)-1):
        if hrs[i+1]<hrs[i]:
            hrs[i+1] = hrs[i+1]+24
            
    count = 1
    flag = int(0)
    data_flat = np.zeros(np.shape(z)[1])
    flat_data_list=[]
    for i in range(0,len(hrs)):
        if((hrs[i]<=hrs[flag]+dt)):
            data_flat = data_flat + z[i,:]
            count=count+1
        else:
            flag = i
            data_flat = data_flat/count
            count = 1
            flat_data_list.append(data_flat)
            data_flat = np.zeros(np.shape(z)[1])
    
    count=0
    print("Starting ploting routine........")
    print(len(flat_data_list))
    for d in flat_data_list:
        count=count+1
#        try:
        h1 = plt.figure()
        plt.plot(x[np.where(((x>=f1)&(x<=f2)))],d[np.where(((x>=f1)&(x<=f2)))])
        plt.grid()
        plt.xlabel('Frequency in MHz')
        plt.ylabel('Relative Magnitude in dB')
        plt.ylim(-0.15,0.1)
#            plt.show()
#            flag = input('Want to save figure?(Y|y/N|n): ')
#            if(flag == 'Y' or flag == 'y'):
        name = fname[:-3]+'_time_avg_dt_'+str(dt)+'hrs_'+str(count)+'.png'
        h1.savefig(name) 
#            else:
#                print('Moving on to next plot.....') 
#        except:
#            try:
#                h1 = plt.figure()
#                plt.plot(x[np.where(x>=f1)],d[np.where(x>=f1)])
#                plt.grid()
#                plt.xlabel('Frequency in MHz')
#                plt.ylabel('Relative Magnitude in dB')
#                plt.show()
#                flag = input('Want to save figure?(Y|y/N|n): ')
#                if(flag == 'Y' or flag == 'y'):
#                    name = fname[:-3]+'_time_avg_dt_'+str(dt)+'hrs_'+str(count)+'.png'
#                    h1.savefig(name) 
#                else:
#                    print('Moving on to next plot.....')
#            except:
#                h1 = plt.figure()
#                plt.plot(x[np.where(x<=f2)],d[np.where(x<=f2)])
#                plt.grid()
#                plt.xlabel('Frequency in MHz')
#                plt.ylabel('Relative Magnitude in dB')
#                plt.show()
#                flag = input('Want to save figure?(Y|y/N|n): ')
#                if(flag == 'Y' or flag == 'y'):
#                    name = fname[:-3]+'_time_avg_dt_'+str(dt)+'hrs_'+str(count)+'.png'
#                    h1.savefig(name) 
#                else:
#                    print('Moving on to next plot.....')

