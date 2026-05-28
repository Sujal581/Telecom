import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_csv("Telecom Dataset.csv")

    df["Camera_Score"] = df["PC"] + df["FC"]
    df["Screen_Size"] = df["Scr_h"] * df["Scr_w"]

    return df


def sidebar_filters(df):

    if st.sidebar.button("🔄 Reset Filters"):

        st.session_state["price_filter"] = "All"
        st.session_state["ram_filter"] = "All"
        st.session_state["battery_filter"] = "All"

    # ==========================================
    # SESSION STATE DEFAULTS
    # ==========================================

    if "price_filter" not in st.session_state:
        st.session_state["price_filter"] = "All"

    if "ram_filter" not in st.session_state:
        st.session_state["ram_filter"] = "All"

    if "battery_filter" not in st.session_state:
        st.session_state["battery_filter"] = "All"

    # ==========================================
    # FILTER WIDGETS
    # ==========================================

    price_filter = st.sidebar.selectbox(
        "💰 Price Range",
        ["All", "Budget", "Mid-Range", "Premium"],
        key="price_filter"
    )

    ram_filter = st.sidebar.selectbox(
        "🧠 RAM",
        ["All"] + sorted(df["RAM"].unique().tolist()),
        key="ram_filter"
    )

    battery_filter = st.sidebar.selectbox(
        "🔋 Battery",
        ["All"] + sorted(df["Bty_Pwr"].unique().tolist()),
        key="battery_filter"
    )

    # ==========================================
    # APPLY FILTERS
    # ==========================================

    filtered_df = df.copy()

    # PRICE FILTER

    if price_filter == "Budget":

        filtered_df = filtered_df[
            filtered_df["Price"] < 20000
        ]

    elif price_filter == "Mid-Range":

        filtered_df = filtered_df[
            (filtered_df["Price"] >= 20000) &
            (filtered_df["Price"] < 50000)
        ]

    elif price_filter == "Premium":

        filtered_df = filtered_df[
            filtered_df["Price"] >= 50000
        ]

    # RAM FILTER

    if ram_filter != "All":

        filtered_df = filtered_df[
            filtered_df["RAM"] == ram_filter
        ]

    # BATTERY FILTER

    if battery_filter != "All":

        filtered_df = filtered_df[
            filtered_df["Bty_Pwr"] >= battery_filter
        ]

    return filtered_df