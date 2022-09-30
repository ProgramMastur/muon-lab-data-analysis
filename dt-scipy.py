import scipy as spicy
import pandas as pd
import numpy as np

for filename in os.listdir(f"./Data/Autosave/"):
    
    df = pd.read_csv(f"./Data/Autosave/{filename}", header=4, encoding='utf8')
    df = df.dropna(axis=1,how="all")
    
    voltages = df["Ampl"]
    
    peak_indices = spicy.findpeaks(voltages)
    
    print(peak_indices)

print("hooray")
