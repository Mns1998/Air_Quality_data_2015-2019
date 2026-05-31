import pandas as pd
import glob
import os

# Species to keep
wanted_species = [
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

# Find all reduced files
csv_files = glob.glob("airquality_*_reduced.csv")

print(f"Found {len(csv_files)} files")

# Create Dataset folder if it doesn't exist
os.makedirs("Dataset", exist_ok=True)

for file in csv_files:

    print(f"\nProcessing: {file}")

    try:

        # Read file
        df = pd.read_csv(file)

        # Keep only desired species
        df = df[df["Specie"].isin(wanted_species)]

        # Pivot species into columns
        pivot_df = df.pivot_table(
            index=["Date", "Country", "City"],
            columns="Specie",
            values="median",
            aggfunc="first"
        ).reset_index()

        # Ensure all species columns exist
        for specie in wanted_species:
            if specie not in pivot_df.columns:
                pivot_df[specie] = "Not Calculated"

        # Fill missing values
        pivot_df = pivot_df.fillna("Not Calculated")

        # Reorder columns
        pivot_df = pivot_df[
            ["Date", "Country", "City"] + wanted_species
        ]

        # Extract year from filename
        year = file.replace("airquality_", "").replace("_reduced.csv", "")

        # Save into Dataset folder
        output_file = os.path.join(
            "Dataset",
            f"waqi-airqualitydata-{year}.csv"
        )

        pivot_df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")

    except Exception as e:
        print(f"Error processing {file}: {e}")

print("\nAll files processed successfully.")