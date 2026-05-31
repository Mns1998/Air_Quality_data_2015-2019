import pandas as pd

# Read master dataset
df = pd.read_csv("waqi-airqualitydata-master.csv")

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

# Count available variables per row
df["AvailableVariables"] = (
    df[value_columns]
    .notna()
    .sum(axis=1)
)

print("Original rows:", len(df))

# Keep rows with at least 4 available variables
filtered_df = df[df["AvailableVariables"] >= 4].copy()

print("Filtered rows:", len(filtered_df))
print("Removed rows:", len(df) - len(filtered_df))

# Remove helper column
filtered_df.drop(
    columns=["AvailableVariables"],
    inplace=True
)

# Save filtered dataset
filtered_df.to_csv(
    "waqi-airqualitydata-master-filtered.csv",
    index=False
)

print("\nSaved as:")
print("waqi-airqualitydata-master-filtered.csv")