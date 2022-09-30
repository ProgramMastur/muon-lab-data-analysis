import numpy as np
import pandas as pd
import os, sys



# filename = f"C1PatrickAndGeorge00042.csv"


# df.reset_index(drop=True, inplace=True)

# iterate through all files in the data directory
for filename in os.listdir(f"./Data/Autosave/"):
    
    # create a dataframe with the csv data
    df = pd.read_csv(f"./Data/Autosave/{filename}", header=4, encoding='utf8')
    df = df.dropna(axis=1,how="all")

    first_peak_t, second_peak_t, highest_V1, highest_V2 = None, None, None, None
    no_peak_dt = None
    go_to_second_peak = False
    
    # setup to ignore signals below a certain amplitude
    booleans = []
    for voltage in df.ampl:
        pair = df.iloc[i].tolist()
        if pair[2]<threshold:
            booleans.append(False)
        else:
            booleans.append(True)


    # iterate through the dataframe
    for i in range(0,len(df)):
        pair = df.iloc[i].tolist() # keep track of one coordinate pair at a time
        if not go_to_second_peak:
            if highest_V1 is None:
                highest_V1 = pair[1]
            if pair[1] > highest_V1:
                first_peak_t, highest_V1 = pair[0], pair[1]
        if go_to_second_peak:
            if highest_V2 is None:
                highest_V2 = -2
            if pair[1] > highest_V2:
                second_peak_t, highest_V2 = pair[0], pair[1]
                # print(pair, i)
        if not go_to_second_peak and first_peak_t is not None and abs(pair[0] - first_peak_t) > 1e-7 and pair[1] > -1.4:
            go_to_second_peak = True

    delta_t = second_peak_t - first_peak_t
    print(filename, delta_t)

#TODO: check if the first instance of the highest data value is actually the top of each primary oscillation
#TODO: introduce a low-pass filter to smooth out data
#TODO: maybe use numpy convolution for the low-pass??
