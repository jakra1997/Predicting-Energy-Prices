# 🧠 Forecasting Method Summary: Recursive Forecasting with XGBoost

---

## 🔍 Overview

This project uses **recursive forecasting** powered by **XGBoost**, a tree-based machine learning model, to predict hourly energy prices over multiple future horizons (1 day to 1 year). The approach draws inspiration from traditional time series models like **ARIMA**, but offers greater flexibility and performance.

---

## 🔁 What is Recursive Forecasting?

Recursive forecasting is a strategy where a **single model is trained to predict one time step ahead** (e.g., 1 hour), and then that prediction is **fed back into the model** as input to forecast the next time step, and so on.

This allows us to extend our forecast window beyond the original training range, even up to **12 months** into the future.

---

## 🧠 Why XGBoost?

- **No assumptions about linearity or stationarity**
- Handles **nonlinear** relationships
- Supports **custom features** (lags, rolling means, calendar info)
- Performs well on **tabular time series data**

---

## 🧮 How It Works

1. **Train a model** using known features from the past:
   - Lag features (price 1h, 24h, 168h ago)
   - Rolling stats (24h & 168h mean)
   - Calendar features (hour, day of week, month)

2. **Predict one step ahead**

3. **Feed that prediction back into the model** as a new lagged value

4. Repeat for as many time steps as needed (24, 168, 720, etc.)

---

## 🔄 Comparison to ARIMA

| Feature              | ARIMA                         | XGBoost Recursive                      |
|----------------------|-------------------------------|----------------------------------------|
| Model Type           | Statistical                   | Machine Learning (Gradient Boosting)   |
| Input Data           | Only past target values       | Lagged features + calendar features    |
| Assumptions          | Stationary, linear            | No strong assumptions                  |
| Seasonality          | Built-in (SARIMA)             | Via calendar + rolling features        |
| Forecast Horizon     | Recursive                     | Recursive                              |

---

## 📈 Results Achieved

Forecasts were generated for:
- **1 day**
- **1 week**
- **1 month**
- **3 months**
- **6 months**
- **12 months**

With evaluation using **MAE** and **RMSE** compared to actual energy prices.

---

