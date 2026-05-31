import pandas as pd

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

df["AvailableVariables"] = (
    df[value_columns]
    .notna()
    .sum(axis=1)
)

print(df["AvailableVariables"].value_counts().sort_index())