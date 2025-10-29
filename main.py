import pandas as pd
import glob 

import os

print("Working directory:", os.getcwd())

# If your CSVs are in a folder next to this script
files = glob.glob("Data_SHPE/*.csv")

print("Files found:", files)

# Read all found CSVs
df_list = []
for f in files:
    try:
        df_list.append(pd.read_csv(f))
        print("Loaded:", f)
    except Exception as e:
        print("Skipped:", f, "| Reason:", e)

# Combine all data if files were found
if df_list:
    df = pd.concat(df_list, ignore_index=True)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df['full_name'] = df['full_name'].str.title().str.strip()
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.drop_duplicates(subset=['full_name', 'event_name'])
    print("Final dataset shape:", df.shape)
else:
    print("⚠️ No CSV files found. Check your folder path!")

#Load all CVs
files = glob.glob("Data_SHPE/*.csv")
df_list = [pd.read_csv(f) for f in files]
df = pd.concat(df_list,ignore_index=True)

#Standardize Column Names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_") 

#Clean member names 
df['full_name'] = df['full_name'].str.title().str.strip()

#Parse TimeStamps
df['timestamp'] = pd.to_datetime(df['timestamp'], errors= 'coerce')

#Remoce Duplicates 
df = df.drop_duplicates(subset=['full_name', 'event_name'])

print(files)