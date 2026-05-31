Air Quality Dataset Processing Pipeline
Overview

This repository contains the data preprocessing workflow used to transform raw worldwide air quality observations obtained from the World Air Quality Index (WAQI) COVID-19 Air Quality Dataset into a structured dataset suitable for visualization and exploratory analysis.

The original dataset contains daily measurements collected from monitoring stations worldwide, including pollutant concentrations and meteorological variables. Each observation includes statistical descriptors such as count, minimum, maximum, median, and variance for individual species measured in each city.

The objective of this project was to reduce data complexity while preserving long-term temporal and geographical trends in air quality.

Data Source

Source:

World Air Quality Index (WAQI) COVID-19 Air Quality Dataset

The raw dataset contains daily observations for cities worldwide between 2015 and 2026.

Variables available in the original dataset include:

Date
Country
City
Species
Count
Minimum
Maximum
Median
Variance
Data Processing Workflow
1. Metadata Removal

Removed dataset header information and non-data rows from all yearly files.

2. Column Reduction

Removed the following columns:

Count
Minimum
Maximum
Variance

Retained the median value as the primary representative measurement.

3. Species Filtering

Retained only the following pollutants and meteorological variables:

CO (Carbon Monoxide)
NO₂ (Nitrogen Dioxide)
O₃ (Ozone)
SO₂ (Sulfur Dioxide)
PM10
PM2.5
Temperature
Humidity
Pressure

All other species were excluded from further analysis.

4. Data Restructuring

Converted species values from a long format into a wide format where each pollutant or meteorological variable becomes an independent column.

5. Temporal Aggregation

Aggregated daily observations into monthly observations using the median value for each:

Month
Country
City

This reduced dataset size while preserving seasonal and long-term air quality trends.

6. Dataset Integration

Merged yearly datasets into a single master dataset covering the entire study period.

7. Data Quality Filtering

Removed observations containing fewer than four available pollutant or meteorological measurements to improve analytical reliability.

8. Feature Engineering

Added additional analytical features:

Year
Month
Continent

These variables facilitate temporal and geographical analysis.

Final Dataset Structure
Column
Year
Month
Country
Continent
City
CO
Temperature
PM10
NO₂
O₃
SO₂
PM2.5
Humidity
Pressure
Applications

The resulting dataset can be used for:

Air quality visualization
Environmental data storytelling
Trend analysis
Geographic comparisons
Seasonal air quality assessment
Correlation analysis between pollutants and meteorological variables
Dashboard development using Tableau, Power BI, D3.js, Plotly, or similar tools
Technologies Used
Python
Pandas
NumPy
CSV Data Processing

This version is suitable for a university project repository and clearly documents the full preprocessing pipeline from raw WAQI data to the final analysis-ready dataset.