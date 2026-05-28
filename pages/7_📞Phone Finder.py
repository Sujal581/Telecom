import streamlit as st
import io
import pandas as pd
import plotly.express as px
from styles import (inject_css, sidebar_brand, page_header, section_header,
                   kpi_card, insight_card, footer, COLORS, chart_label, plotly_futuristic_layout, df_table, executive_insight,show_table)
import plotly.graph_objects as go
from data import load_data

inject_css()
sidebar_brand()
df=load_data()


# ───────────────── TITLE ─────────────────
st.set_page_config(
    page_icon="📳",
    page_title="Telecom | Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 🔍 SMART PHONE FINDER
# ==========================================

page_header(
    "🔍 Smart Phone Finder",
    "Find the best smartphones based on your budget and performance preferences"
)

# ==========================================
# 🎛️ USER INPUTS
# ==========================================
section_header("🔍 Smart Phone Finder")
col1, col2 = st.columns(2)

with col1:

    max_price = st.slider(
        "💰 Maximum Price",
        min_value=int(df["Price"].min()),
        max_value=int(df["Price"].max()),
        value=int(df["Price"].quantile(0.75))
    )

    min_ram = st.slider(
        "🧠 Minimum RAM",
        min_value=int(df["RAM"].min()),
        max_value=int(df["RAM"].max()),
        value=int(df["RAM"].median())
    )

with col2:

    min_battery = st.slider(
        "🔋 Minimum Battery",
        min_value=int(df["Bty_Pwr"].min()),
        max_value=int(df["Bty_Pwr"].max()),
        value=int(df["Bty_Pwr"].median())
    )

    camera_pref = st.checkbox(
        "📷 Prioritize Strong Camera Performance"
    )

# ==========================================
# 📸 CAMERA SCORE
# ==========================================

df["Camera_Score"] = df["PC"] + df["FC"]

# ==========================================
# 🔍 APPLY FILTERS
# ==========================================

filtered_df = df[
    (df["Price"] <= max_price) &
    (df["RAM"] >= min_ram) &
    (df["Bty_Pwr"] >= min_battery)
].copy()

# ==========================================
# 🏆 VALUE SCORE CALCULATION
# ==========================================

if camera_pref:

    filtered_df["Value_Score"] = (
        filtered_df["RAM"] * 0.30 +
        filtered_df["Bty_Pwr"] * 0.30 +
        filtered_df["Camera_Score"] * 0.40
    ) / filtered_df["Price"]

else:

    filtered_df["Value_Score"] = (
        filtered_df["RAM"] * 0.40 +
        filtered_df["Bty_Pwr"] * 0.40 +
        filtered_df["Camera_Score"] * 0.20
    ) / filtered_df["Price"]

# ==========================================
# 📊 MATCHING PHONES
# ==========================================

section_header(
    "📊 Recommended Smartphones",
    "Matching devices ranked by overall value score"
)

if filtered_df.empty:

    st.warning(
        "⚠️ No smartphones match the selected requirements. Try relaxing some filters."
    )

else:

    recommended_df = filtered_df.sort_values(
        by="Value_Score",
        ascending=False
    )

    display_df = recommended_df[
        [
            "PID",
            "Price",
            "RAM",
            "Bty_Pwr",
            "PC",
            "FC",
            "Int_Mem",
            "Weight",
            "Value_Score"
        ]
    ].rename(columns={
        "PID": "Phone ID",
        "Price": "Price",
        "RAM": "RAM",
        "Bty_Pwr": "Battery",
        "PC": "Primary Camera",
        "FC": "Front Camera",
        "Int_Mem": "Storage",
        "Weight": "Weight",
        "Value_Score": "Value Score"
    })

    df_table(
        display_df,
    )

# ==========================================
# 🏆 TOP RECOMMENDATION
# ==========================================

    best_phone = recommended_df.iloc[0]

    section_header(
        "🏆 Best Recommended Smartphone",
        "Highest-ranked smartphone based on selected preferences"
    )

    st.success(
        f"""
        📱 Recommended Device: PID {best_phone['PID']}
        
        💰 Price: ₹ {best_phone['Price']:,.0f}
        
        🧠 RAM: {best_phone['RAM']}
        
        🔋 Battery: {best_phone['Bty_Pwr']} mAh
        
        📸 Camera Score: {best_phone['Camera_Score']}
        
        ⭐ Value Score: {best_phone['Value_Score']:.4f}
        """
    )

# ==========================================
# 📈 VALUE SCORE VISUALIZATION
# ==========================================

    chart_label(
        "📈 Smartphone Value Score Ranking",
        "Compares recommended smartphones based on overall value efficiency"
    )

    fig_value = px.bar(
        recommended_df.head(10),
        x="PID",
        y="Value_Score",
        color="Value_Score",
        hover_data=["Price", "RAM", "Bty_Pwr"]
    )

    fig_value.update_layout(**plotly_futuristic_layout())

    fig_value.update_xaxes(title="Phone ID")
    fig_value.update_yaxes(title="Value Score")

    st.plotly_chart(fig_value, use_container_width=True)

# ==========================================
# 🔥 IMPORTANT RECOMMENDATION INSIGHTS
# ==========================================

section_header(
    "🔥 Recommendation Insights",
    "Key observations from the smart recommendation engine"
)

insight_card(
    "🧠 Smartphones with balanced RAM, battery capacity, and pricing tend to achieve the highest value scores."
)

insight_card(
    "📸 Enabling camera prioritization increases the ranking of devices with stronger overall camera systems."
)

insight_card(
    "💰 Premium devices do not always provide the best value, especially when pricing increases faster than hardware improvements."
)

insight_card(
    "🚀 The recommendation engine helps identify smartphones offering the strongest hardware efficiency within a selected budget."
)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "📊 Smartphone Analytics Dashboard • Built with Streamlit & Plotly"
)