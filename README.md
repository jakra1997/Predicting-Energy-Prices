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
/data/raw </br>
or </br>
https://drive.google.com/drive/folders/177Za4MCs7PLsISKVG6Aa4DdxCxxd3wKB?usp=sharing

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

 ## Files

    01_data_merge.ipynb
      merges numeric data into one csv file
│   02_EDA.ipynb
      performs EDA on the numeric data
│   03_baseline_model.ipynb
      baseline model to predict the energy price
│   03_baseline_model_168h.ipynb
      baseline model to predict the energy price for 1 week      
│   03_baseline_model_24h.ipynb
      baseline model to predict the energy price for 1 day  
│   03_baseline_model_336h.ipynb
      baseline model to predict the energy price for 2 weeks  
│   03_baseline_model_48h.ipynb
      baseline model to predict the energy price for 2 days  
│   03_baseline_model_672h.ipynb
      baseline model to predict the energy price for 1 month  
│   03_baseline_model_72h.ipynb
      baseline model to predict the energy price for 3 days  
│   09b_news_eda_filtering.ipynb
      filters news headlines and performs EDA
│   09c_bert_sentiment_analysis_torch.ipynb
      performs sentiment analysis on the headlines and turns it into numeric data
│   09d_sentiment_EDA_energy_prices.ipynb
      performs EDA on the numeric data
│   11_Multimodal Model_168h.ipynb
      baseline model to predict the energy price for 1 week  
│   11_Multimodal Model_24h.ipynb
      baseline model to predict the energy price for 1 day  
│   11_Multimodal Model_336h.ipynb
      baseline model to predict the energy price for 2 weeks  
│   11_Multimodal Model_48h.ipynb
      baseline model to predict the energy price for 2 days  
│   11_Multimodal Model_672h.ipynb
      baseline model to predict the energy price for 1 month  
│   11_Multimodal Model_72h.ipynb
      baseline model to predict the energy price for 3 days  


## Results

![image](https://github.com/user-attachments/assets/6d6f5d95-10b0-462d-a25e-d84a57aa45d5)

---

## 🚀 Deployment

### User Interface
To access the user interface, write: </br>
python -m streamlit run app.py </br> 


### 🐳 Docker + FastAPI (does not work)

Run a RESTful API to serve predictions:

#### Dockerfile Highlights:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
