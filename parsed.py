import argparse
import os
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
parser.add_argument("-f1","--startfrequency", help="Mention start frequency in MHz (Default: Full range)")
parser.add_argument("-f2","--stopfrequency", help="Mention stop frequency in MHz (Default: Full range)")
parser.add_argument("-dt","--deltatime", help="This is for multiple time averaged plot delta time t in hours (decimal values are accepted), an interractive save rutine")


args = parser.parse_args()

try:
    f1 = float(args.startfrequency)
except:
    f1=None
try:
    f2 = float(args.stopfrequency)
except:
    f2=None
try:
    dt = float(args.deltatime)
except:
    dt=None
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

