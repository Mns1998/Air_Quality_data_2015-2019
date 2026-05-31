import pandas as pd
import glob
import os

input_folder = "Current Dataset"

# Read all yearly files from Dataset
csv_files = [
    f for f in glob.glob(os.path.join(input_folder, "*.csv"))
    if "master" not in os.path.basename(f).lower()
]

print(f"Found {len(csv_files)} files")

dataframes = []

for file in csv_files:

    print(f"Reading: {os.path.basename(file)}")

    df = pd.read_csv(file)

    dataframes.append(df)

# Merge all files
master_df = pd.concat(
    dataframes,
    ignore_index=True
)

# Save directly in Team Project folder
output_file = "waqi-airqualitydata-master.csv"

master_df.to_csv(
    output_file,
    index=False
)

print("\nMerge complete!")
print(f"Total rows: {len(master_df)}")
print(f"Total columns: {len(master_df.columns)}")
print(f"Saved to: {output_file}")