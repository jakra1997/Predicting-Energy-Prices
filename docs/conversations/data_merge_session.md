# 🧠 Data Merge Session — Energy Price Prediction Project
**Date:** 2025-04-18 19:49:53

---

## 📋 Summary

This session involved merging and preparing various datasets for a multi-modal energy price prediction project based on German data from 2015–2020. Datasets included hourly energy consumption, solar/wind generation, irradiance, daily oil & gas prices.

---

## ✅ Key Steps Taken

### 1. **Folder and File Setup**
- Structured project folder for GitHub with folders like `data/raw`, `notebooks/`, and `src/`
- Loaded CSV files:
  - `Germany.csv` — consumption & prices
  - `time_series_60min_singleindex_filtered.csv` — solar & wind generation
  - `weather_data_filtered.csv` — irradiance
  - `daily.csv` — natural gas prices
  - `RBRTEd.csv` — oil prices (trimmed to 2015–2020)

### 2. **Notebook Creation: `01_data_merge.ipynb`**
- Standardized datetime formats
- Removed timezone info from UTC timestamps
- Merged hourly datasets on `utc_timestamp`
- Converted daily gas and oil prices to match `date` format
- Forward-filled missing values in daily data
- Saved the final merged dataset to: `data/processed/merged_energy_data.csv`

### 3. **Fixes & Custom Tweaks**
- Fixed timezone-aware merge errors
- Removed header junk from oil CSV
- Matched daily prices to hourly data using `left_on='date'`
- Dropped redundant columns like `Date`, `Datetime (UTC)`, etc.
- Used `.dropna()`, `.fillna()`, and `.interpolate()` as needed

---

## 🔍 Code Snippets Used

### Show headers:
```python
print(df_hourly.columns)
```

### Show missing rows:
```python
df_hourly[df_hourly['DE_solar_generation_actual'].isna()]
```

### Drop rows after a certain date:
```python
df_hourly = df_hourly[df_hourly['utc_timestamp'] <= '2019-12-30']
```

### Forward fill missing values:
```python
df_hourly['DE_wind_generation_actual'].fillna(method='ffill', inplace=True)
```

### Drop rows with missing data:
```python
df_hourly.dropna(inplace=True)
```

---

## 🧩 Next Steps
- Start EDA: visualize trends, missingness, and distributions
- Build baseline model with XGBoost or LightGBM
- Prepare for multimodal fusion with sentiment data

---

**Generated via ChatGPT - session export**
