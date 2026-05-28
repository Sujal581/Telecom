import streamlit as st
import io
import pandas as pd
import plotly.express as px
from styles import (inject_css, sidebar_brand, page_header, section_header,
                   kpi_card, insight_card, footer, COLORS, chart_label, plotly_futuristic_layout, df_table, executive_insight,show_table)
import plotly.graph_objects as go
from data import load_data, sidebar_filters

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

# ───────────────── HEADER ─────────────────
page_header(
    "Compare Tools",
    "AI-powered mobile analytics, pricing insights & device performance monitoring",
    "🔬"
)


# ==========================================
# ⚖️ SMARTPHONE COMPARISON TOOL
# ==========================================

section_header(
    "⚖️ Smartphone Comparison Tool",
    "Compare multiple smartphones side-by-side across performance, battery, camera, and pricing metrics"
)

# ==========================================
# 📱 PHONE SELECTION
# ==========================================

selected_phones = st.multiselect(
    "📱 Select Smartphones (PID)",
    options=df["PID"].unique(),
    default=df["PID"].unique()[:3]
)

compare_df = df[df["PID"].isin(selected_phones)]

# ==========================================
# 📊 COMPARISON TABLE
# ==========================================

chart_label(
    "📊 Smartphone Comparison Table",
    "Compare key smartphone specifications side-by-side"
)

comparison_table = compare_df[
    [
        "PID",
        "RAM",
        "Bty_Pwr",
        "PC",
        "FC",
        "Price",
        "Weight",
        "Int_Mem"
    ]
]

comparison_table = comparison_table.rename(columns={
    "PID": "Phone ID",
    "RAM": "RAM",
    "Bty_Pwr": "Battery",
    "PC": "Primary Camera",
    "FC": "Front Camera",
    "Price": "Price",
    "Weight": "Weight",
    "Int_Mem": "Storage"
})

df_table(
    comparison_table,
)

insight_card(
    "📊 Comparison Insight: The table allows quick identification of smartphones offering the best balance between performance, battery life, and pricing."
)

# ==========================================
# 📡 RADAR CHART COMPARISON
# ==========================================

chart_label(
    "📡 Radar Chart Comparison",
    "Visual comparison of smartphone performance metrics"
)

# Create camera score
compare_df["Camera_Score"] = compare_df["PC"] + compare_df["FC"]

radar_metrics = [
    "RAM",
    "Bty_Pwr",
    "Camera_Score",
    "Price",
    "Weight"
]

fig_radar = go.Figure()

for _, row in compare_df.iterrows():

    fig_radar.add_trace(go.Scatterpolar(
        r=[
            row["RAM"],
            row["Bty_Pwr"],
            row["Camera_Score"],
            row["Price"],
            row["Weight"]
        ],
        theta=[
            "RAM",
            "Battery",
            "Camera",
            "Price",
            "Weight"
        ],
        fill='toself',
        name=f"PID {row['PID']}"
    ))

fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True
        )
    ),
    showlegend=True,
    height=600
)

fig_radar.update_layout(**plotly_futuristic_layout())

st.plotly_chart(fig_radar, use_container_width=True)

insight_card(
    "📡 Radar Insight: Radar charts help identify smartphones that provide balanced overall performance across multiple hardware categories."
)

# ==========================================
# 🏆 BEST VALUE DEVICE
# ==========================================

# Create value score
compare_df["Value_Score"] = (
    compare_df["RAM"] +
    compare_df["Bty_Pwr"] +
    compare_df["Camera_Score"]
) / compare_df["Price"]

best_phone = compare_df.sort_values(
    by="Value_Score",
    ascending=False
).iloc[0]

section_header(
    "🏆 Best Value Smartphone",
    "Identifies the strongest overall value proposition among selected devices"
)

st.success(
    f"""
    📱 Best Value Device: PID {best_phone['PID']}
    
    💰 Price: ₹ {best_phone['Price']:,.0f}
    
    🧠 RAM: {best_phone['RAM']}
    
    🔋 Battery: {best_phone['Bty_Pwr']} mAh
    
    📸 Camera Score: {best_phone['Camera_Score']}
    """
)

insight_card(
    "🏆 Value Insight: The selected best-value smartphone offers the strongest balance between hardware specifications and pricing."
)

# ==========================================
# 🔥 IMPORTANT COMPARISON INSIGHTS
# ==========================================

section_header(
    "🔥 Important Comparison Insights",
    "Key observations derived from multi-device comparison analysis"
)

insight_card(
    "🧠 Smartphones with higher RAM and larger batteries generally provide stronger performance capabilities."
)

insight_card(
    "📸 Premium camera systems are commonly associated with higher smartphone pricing."
)

insight_card(
    "⚖️ Radar charts help identify balanced devices rather than focusing on a single specification."
)

insight_card(
    "🚀 Value-oriented smartphones combine strong hardware specifications with competitive pricing."
)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "📊 Smartphone Analytics Dashboard • Built with Streamlit & Plotly"
)