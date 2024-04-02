import sys
import os
import glob
from multiprocessing import Pool
import pandas as pd


#
# Integrate ticks
#
#   python mt5_integrate_ticks.py usdjpy 2024
#
#

def read_csv(filename):
    df = pd.read_csv(filename, index_col='datetime', parse_dates=True)
    df = df.dropna()
    print("done to read", filename)
    return df

if __name__=="__main__":
    instrument = str(sys.argv[1])
    year       = int(sys.argv[2])
    core_count = 4

    csv_files = []
    for month in range(1, 13):
        csv_path  = f"data_mt5_ticks/{instrument}/{instrument}_{year}_{month}_ticks.csv"
        if os.path.exists(csv_path):
            csv_files = csv_files + [csv_path]
    
    with Pool(core_count) as p:
        df_list = p.map(read_csv, csv_files)
    all_df = pd.concat(df_list)
    print("sorting index of all_df")
    all_df = all_df.sort_index()
    print("saving result...")
    all_df.to_csv(f"./data_mt5_ticks/{instrument}_{year}_ticks.csv", header=True)
    print("done.")
