import scipy as spicy
import pandas as pd
import numpy as np
import os, sys

dt_list = []

for filename in os.listdir(f"./Background Data/"):
    
    df = pd.read_csv(f"./Background Data/{filename}", header=4, encoding='utf8')
    df = df.dropna(axis=1,how="all")
    
    voltages = df["Ampl"].tolist()
    
    peak_indices = spicy.signal.find_peaks(voltages, -0.862)
    ## parameters: x (signal), height=None, threshold=None, distance=None, prominence=None
    print(filename)
    print(peak_indices[0])
    
    if(len(peak_indices[0])==2):
        dt_list.append((((peak_indices[0])[1]) - ((peak_indices[0])[0]))*(0.25E-9))

print("hooray1")
dt_dataframe = pd.DataFrame(dt_list) 
dt_dataframe.to_csv('dt-bg.csv')
print("hooray2")
