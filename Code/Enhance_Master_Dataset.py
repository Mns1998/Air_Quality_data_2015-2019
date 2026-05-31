import pandas as pd

# Read filtered master dataset
df = pd.read_csv("waqi-airqualitydata-master-filtered.csv")

print(f"Rows before processing: {len(df)}")

# --------------------------------------------------
# Create Year and Month columns
# --------------------------------------------------

df["Year"] = df["YearMonth"].str[:4].astype(int)

month_num = df["YearMonth"].str[5:7].astype(int)

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

df["Month"] = month_num.map(month_names)

# --------------------------------------------------
# Add Continent column
# --------------------------------------------------

continent_map = {

    # Europe
    "AT":"Europe","BE":"Europe","BG":"Europe","CH":"Europe",
    "CZ":"Europe","DE":"Europe","DK":"Europe","EE":"Europe",
    "ES":"Europe","FI":"Europe","FR":"Europe","GB":"Europe",
    "GR":"Europe","HR":"Europe","HU":"Europe","IE":"Europe",
    "IT":"Europe","LT":"Europe","LU":"Europe","LV":"Europe",
    "NL":"Europe","NO":"Europe","PL":"Europe","PT":"Europe",
    "RO":"Europe","RS":"Europe","SE":"Europe","SI":"Europe",
    "SK":"Europe","UA":"Europe",

    # Asia
    "AE":"Asia","BD":"Asia","CN":"Asia","HK":"Asia",
    "ID":"Asia","IL":"Asia","IN":"Asia","IQ":"Asia",
    "IR":"Asia","JP":"Asia","JO":"Asia","KR":"Asia",
    "KW":"Asia","LB":"Asia","MM":"Asia","MN":"Asia",
    "MY":"Asia","NP":"Asia","OM":"Asia","PH":"Asia",
    "PK":"Asia","QA":"Asia","SA":"Asia","SG":"Asia",
    "TH":"Asia","TR":"Asia","TW":"Asia","VN":"Asia",

    # North America
    "CA":"North America",
    "MX":"North America",
    "US":"North America",

    # South America
    "AR":"South America",
    "BO":"South America",
    "BR":"South America",
    "CL":"South America",
    "CO":"South America",
    "EC":"South America",
    "PE":"South America",
    "PY":"South America",
    "UY":"South America",
    "VE":"South America",

    # Africa
    "DZ":"Africa",
    "EG":"Africa",
    "ET":"Africa",
    "GH":"Africa",
    "KE":"Africa",
    "MA":"Africa",
    "NG":"Africa",
    "TN":"Africa",
    "UG":"Africa",
    "ZA":"Africa",

    # Oceania
    "AU":"Oceania",
    "NZ":"Oceania"
}

df["Continent"] = df["Country"].map(continent_map)

# Any unknown country code
df["Continent"] = df["Continent"].fillna("Unknown")

# --------------------------------------------------
# Reorder columns
# --------------------------------------------------

final_columns = [
    "Year",
    "Month",
    "Country",
    "Continent",
    "City",
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

df = df[final_columns]

# --------------------------------------------------
# Save final dataset
# --------------------------------------------------

output_file = "waqi-airqualitydata-final.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nDone!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Saved as: {output_file}")