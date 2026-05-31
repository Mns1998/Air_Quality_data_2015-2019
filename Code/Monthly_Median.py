import pandas as pd
import numpy as np
import glob
import os

# Input and output folders
input_folder = r"C:\Users\umana\OneDrive\Desktop\Team Project\NoSpecieDataset"
output_folder = r"C:\Users\umana\OneDrive\Desktop\Team Project\Dataset"

print("Current directory:", os.getcwd())
print("Folder exists:", os.path.exists(input_folder))

if os.path.exists(input_folder):
    print("Contents:")
    print(os.listdir(input_folder))

# Create output folder if needed
os.makedirs(output_folder, exist_ok=True)

# Species columns
value_columns = [
    "co",
    "temperature",
    "pm10",
    "no2",
    "o3",
    "so2",
    "pm25",
    "humidity",
    "pressure"
]

# Find all CSV files
csv_files = glob.glob(os.path.join(input_folder, "*.csv"))

print(f"Found {len(csv_files)} files")

for file in csv_files:

    print(f"\nProcessing: {os.path.basename(file)}")

    try:

        # Read file
        df = pd.read_csv(file)

        # Convert Date column
        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce",
            format="mixed"
        )

        # Create YearMonth
        df["YearMonth"] = (
            df["Date"]
            .dt.to_period("M")
            .astype(str)
        )

        # Convert values to numeric
        for col in value_columns:

            if col in df.columns:
                df[col] = pd.to_numeric(
                    df[col],
                    errors="coerce"
                )

        # Monthly median
        monthly_df = (
            df.groupby(
                ["YearMonth", "Country", "City"]
            )[value_columns]
            .median()
            .reset_index()
        )

        # Truncate to 2 decimal places
        for col in value_columns:

            monthly_df[col] = np.where(
                monthly_df[col].notna(),
                np.floor(monthly_df[col] * 100) / 100,
                np.nan
            )

        # Replace NaN with NA
        monthly_df = monthly_df.fillna("NA")

        # Create output filename
        filename = os.path.basename(file)

        output_file = os.path.join(
            output_folder,
            filename
        )

        # Save
        monthly_df.to_csv(
            output_file,
            index=False
        )

        print(f"Saved: {output_file}")

    except Exception as e:

        print(
            f"Error processing {os.path.basename(file)}: {e}"
        )

print("\nAll files processed successfully.")