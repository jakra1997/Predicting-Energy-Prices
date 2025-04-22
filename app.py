import streamlit as st
import pandas as pd
from datetime import datetime

# --- UI ---
st.title("🔋 Energy Price Prediction Viewer")

# Date slider for selecting a date in 2019
selected_date = st.slider(
    "Select a date during 2019",
    min_value=datetime(2019, 1, 1),
    max_value=datetime(2019, 12, 31),
    format="YYYY-MM-DD"
)

# Dropdown for prediction length
prediction_length = st.selectbox(
    "Select prediction horizon (in hours)",
    options=["24", "48", "72", "168", "336", "672"],
    index=0
)

# Load results
def load_results(model_type):
    path = f"data/results/{model_type}_{prediction_length}h.csv"
    try:
        df = pd.read_csv(path, parse_dates=["date"])
        df.set_index("date", inplace=True)
        return df
    except FileNotFoundError:
        st.error(f"{model_type}_{prediction_length}h.csv not found.")
        return None

# Display results
def display_prediction(df, label):
    if selected_date in df.index:
        value = df.loc[selected_date, "predicted_price"]
        st.success(f"{label} Prediction: {value:.2f} EUR/MWhe")
    else:
        st.warning(f"No data available for {label} model on {selected_date.strftime('%Y-%m-%d')}")

# Load and display predictions
st.subheader("🔍 Predictions")
for model in ["U", "M"]:  # U = Unimodal, M = Multimodal
    df = load_results(model)
    if df is not None:
        label = "Unimodal" if model == "U" else "Multimodal"
        display_prediction(df, label)
