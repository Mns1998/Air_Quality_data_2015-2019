import pandas as pd
import glob

# Find all airquality CSV files
csv_files = glob.glob("airquality_*.csv")

print(f"Found {len(csv_files)} files")

# Columns to remove
columns_to_remove = ["count", "min", "max", "variance"]

for file in csv_files:

    print(f"Processing: {file}")

    try:
        # Read CSV
        df = pd.read_csv(file)

        # Remove columns if they exist
        existing_columns = [
            col for col in columns_to_remove
            if col in df.columns
        ]

        df = df.drop(columns=existing_columns)

        # Create output filename
        output_file = file.replace(".csv", "_reduced.csv")

        # Save new file
        df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")

    except Exception as e:
        print(f"Error processing {file}: {e}")

print("\nAll files processed successfully.")