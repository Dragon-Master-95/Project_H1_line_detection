import os
import argparse
import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import datetime

def plotting_data(data,fname,timestamps):
    
    x = np.linspace(data[1,1],data[1,2],np.shape(data)[1]-3)/1e+6
    y = np.arange(0,np.shape(data)[0])
    ylabel = pd.DataFrame(timestamps,columns=['Timestamp'])
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
    plt.yticks(y[k.astype(int)],ylabel['Timestamp'][k.astype(int)])
    plt.xticks(rotation = 45)
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
    
