
# 🗓️ Sunday Project Summary (Energy Forecasting + News Collection)

## 🔄 1. Forecasting Features for Energy Price Modeling
We revisited the forecasting pipeline with a more realistic approach:
- **Objective**: Predict energy price for Jan 1–7, 2020 using only past data.
- **Method**: Forecast all SHAP-relevant input features for the prior week (Dec 25–31, 2019), then use those as inputs.
- **Features Predicted**:
  - `DE_solar_generation_actual`
  - `DE_wind_generation_actual`
  - `DE_load_actual_entsoe_transparency`
  - `Oil_Price`
  - `solar_load_ratio`
  - `wind_load_ratio`

## 📉 2. Evaluation Results (Forecasted Inputs → Price)
- When actual inputs were used: **MAE: 1.97**, **RMSE: 3.13**
- With predicted inputs: **MAE: 27.05**, **RMSE: 28.48**
- 🔍 **Insight**: Even strong models like XGBoost are highly sensitive to inaccurate inputs. This validates the importance of accurate feature forecasting in multimodal time series setups.

## 📦 3. News/Sentiment Data Collection (GDELT)
We restarted efforts to collect historical news for sentiment analysis:
- 🧠 Shifted focus from Germany-only to **worldwide impactful events**
- 📆 Timeframe: **July–December 2017**
- 🗂️ Data source: **GDELT Events Database**
- 🔍 Filtered by **energy-related themes**: `ENERGY`, `OIL`, `GAS`, `ELECTRICITY`
- 📄 Output: `gdelt_energy_events_2017_H2.csv` (to be generated)

## 📁 Notebooks Created
- `10e_fast_multioutput_forecast_shap_features.ipynb`: Fast forecast using reduced features
- `09a_download_gdelt_energy_events_2017_H2.ipynb`: Scraper for GDELT event records

## ✅ Next Steps
- Run GDELT notebook and explore results
- Analyze tone and volume over time
- Integrate news sentiment into final multimodal prediction model
