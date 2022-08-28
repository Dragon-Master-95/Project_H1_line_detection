#"RA- 279.11249  Dec- -8.22694"

#importing libraries required
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/jovian-explorer/Project_H1_line_detection/main/LAB_Spectrum.csv'

pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)

dataset = pd.read_csv(url)
#print(dataset)

RA= "$18h36m$" 
Dec= "-8.22694$^{\circ}$"

# accessing the different columns of the csv dataset I made above
dataset.columns = ["v_lsr","T_B"]
#storing values for each column into a separate arrays
v_lsr = np.array(dataset.v_lsr)           # Values of velocity
T_B= np.array(dataset.T_B)                # Values of temperature

fig = plt.figure()
#plt.scatter(v_lsr, T_B, s = 1,label = "?")
plt.plot(v_lsr, T_B,label = "LAB")

plt.xlabel("$v_{lsr}$ [km/s]")
plt.ylabel("Brightness Temperature $T_{B}$ [K]")
#plt.title("HI profile for RA- $18h36m$ Dec- $-8.22694^{\circ}$")
plt.title("HI profile for RA " + f"{RA}" + " Dec "+ f"{Dec}")
plt.legend(loc = 'best')
fig.savefig('LAB.png')
plt.show()
