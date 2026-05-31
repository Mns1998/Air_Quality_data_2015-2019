import pandas as pd
import glob
import os
import re

# Find all original CSV files in the current folder
csv_files = [f for f in glob.glob("*.csv") if not f.startswith("airquality_")]

print(f"Found {len(csv_files)} CSV files")

for file in csv_files:

    filename = os.path.basename(file)

    print(f"Processing: {filename}")

    try:
        # Skip first 4 metadata rows
        df = pd.read_csv(file, skiprows=4)

        # Extract year or year range from filename
        year_match = re.search(r'(\d{4}(?:-\d{4})?)', filename)

        if year_match:
            year_part = year_match.group(1).replace("-", "_")
            cleaned_name = f"airquality_{year_part}.csv"
        else:
            print(f"Could not determine year for {filename}")
            continue

        # Save cleaned file
        df.to_csv(cleaned_name, index=False)

        print(f"Saved: {cleaned_name}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("\nAll files processed successfully.")