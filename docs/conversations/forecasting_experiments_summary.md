
# 📊 Energy Price Forecasting Summary (April 19 Session)

This summary documents the key methods and tests we explored for forecasting energy prices, with an emphasis on understanding the role of historical lags vs external features (solar, wind, etc.).

---

## ✅ Goal
Forecast **hourly energy prices** for Germany using different time series and machine learning strategies. The main forecast horizon: **168 hours (1 week)**.

---

## 🔁 Method 1: Recursive Forecast (Autoregressive)
- **Approach**: Train a model (e.g., XGBoost) to predict `price(t+1)` using lagged values of price and calendar features.
- **Recursive loop**: Use predictions as inputs to forecast each hour one by one.
- **Features**:
  - Lagged price (1h, 24h, 168h)
  - Hour, day of week, month

**Pros**:
- Very accurate short-term
- Captures autoregressive momentum well

**Results**:  
📊 MAE ~ **2.00**  
📊 RMSE ~ **3.36**

---

## ⏩ Method 2: Direct Multi-Output Forecast (168 Inputs → 168 Outputs)
- **Approach**: Train one model to predict the **entire week of prices at once**, using the past 168 hours of multiple features.
- **Model**: `MultiOutputRegressor(XGBoost)`
- **Inputs**: Lagged time series of:
  - `Price (EUR/MWhe)`
  - `DE_solar_generation_actual`
  - `DE_wind_generation_actual`
  - `DE_load_actual_entsoe_transparency`
  - `Gas_Price`, `Oil_Price`
  - `DE_radiation_direct_horizontal`, `DE_radiation_diffuse_horizontal`
  - `DE_temperature`

**Pros**:
- Tries to model a full trajectory
- Uses external info like weather & fuel

**Results**:  
📊 MAE ~ **2.23** (example)  
📊 RMSE ~ **3.50–4.20** depending on test window

---

## 🔍 Special Evaluation: Forecast on Jan 1–7, 2020
- Used raw data from `Germany.csv` (2015–2025) to extract the true prices
- Forecast using both models to compare side-by-side
- Recursive model showed **superior accuracy** despite not using external features

---

## 🧠 Insights
- Recursive models using past prices alone outperform more complex models for **short-range prediction**
- External features (solar, wind, gas...) may not help significantly in **short-term** horizons
- However, they offer **interpretability** and may be more useful for **longer-term trends or policy-driven forecasts**

---

## 🎯 Presentation Framing Strategy
- Hypothesis: External energy and weather features are informative
- Result: Not always predictive in short-term
- Reframing:
  - "Short-term energy prices have strong autoregressive structure"
  - "External variables provide context, explanation, and resilience"
  - "Useful for interpretability and long-term planning"

---

## 📁 Files Used
- `merged_energy_data_final_step_1.csv` — cleaned modeling data
- `Germany.csv` — actual energy prices for comparison
- `08_direct_multioutput_forecast.ipynb` — direct XGBoost forecasting notebook
- Recursive forecasting notebooks (prior versions for comparison)

---

Let me know if you’d like this converted to a slide, PDF, or extended into a formal report!
