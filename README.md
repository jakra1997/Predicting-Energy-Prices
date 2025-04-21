# ⚡ Energy Price Forecasting with Multimodal AI

This project aims to forecast hourly energy prices using machine learning models that combine **structured time series data** (such as solar/wind/load/gas/oil) with **unstructured sentiment signals** extracted from energy-related news. </br>

Done by: Jad Akra "jaa65@mail.aub.edu" for EECE690 - Intro to Machine Learning @ American University of Beirut

---

## 📊 Problem Overview

Accurate energy price forecasting is vital for traders, operators, and policy makers to manage risk, plan energy usage, and enable smart grids. Prices are affected by multiple factors, including:
- Renewable energy production
- Load (demand)
- Fuel prices (Oil, Gas)
- Weather conditions
- Public sentiment and geopolitical news

---

## 📁 Dataset Overview
Data can be found under the folder: </br>
/data/raw

## Credits
time_series_60min_singleindex_filtered.csv "https://data.open-power-system-data.org/time_series/2020-10-06" </br>
load demand, solar production, wind production

weather_data_filtered.csv "https://data.open-power-system-data.org/weather_data/2020-09-16" </br>
temperature, irradiation

Germany.csv "https://ember-energy.org/data/european-wholesale-electricity-price-data/" </br>
Energy Prices

RBRTEd.csv "https://www.eia.gov/dnav/pet/hist/RBRTED.htm" </br>
Oil Prices

daily.csv "https://datahub.io/core/natural-gas#readme" </br>
Gas Prices

wp_hl.csv & wsj_hl.csv "https://www.kaggle.com/datasets/morjanat/news-headline-1" </br>
News_Category_Dataset_v3.json "https://www.kaggle.com/datasets/rmisra/news-category-dataset" </br>
News Headlines

### Structured Data:
- Germany electricity grid data (2015–2020)
- Hourly resolution
- Features: solar, wind, load, temperature, gas/oil prices, irradiance

### Unstructured Data:
- ~100k filtered energy-related news headlines (2015–2019)
- Sentiment scored using BERT (avg score, positive ratio)
- Categorized and filtered by impactful topics (e.g., *Middle East*, *Markets*, *Politics*)

---

## 🧪 Modeling Approaches

### Unimodal Approach:
- Model: `XGBoostRegressor`
- Features: Time lags, calendar signals, ratios (wind/load)
- Training on raw price data
- Baseline performance:  
  - 24h MAE ≈ 6.07  
  - 168h MAE ≈ 6.33  
  - 336h MAE ≈ 6.64  

### Multimodal Approach:
- Early-stage fusion of structured data + sentiment features
- Sentiment features lagged to avoid data leakage
- Slight improvement in RMSE observed across forecasting horizons

---

## 🤖 Model Architecture

We explored:
- **Time-lagged feature engineering**
- **Smoothed rolling averages**
- **Derivative-based forecasting**
- **Sentiment-category interactions**
- **Total energy cost estimation:**
  - `Cost = Predicted Price × Load`
## Results

![image](https://github.com/user-attachments/assets/6d6f5d95-10b0-462d-a25e-d84a57aa45d5)

---

## 🚀 Deployment

### 🐳 Docker + FastAPI

Run a RESTful API to serve predictions:

#### Dockerfile Highlights:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
