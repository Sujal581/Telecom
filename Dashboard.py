

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from styles import (inject_css, sidebar_brand, page_header, section_header,
                   kpi_card, insight_card, footer, COLORS, chart_label, plotly_futuristic_layout, df_table, executive_insight,show_table)
from data import load_data, sidebar_filters

inject_css()
sidebar_brand()
df=load_data()
filtered_df = sidebar_filters(df)

# ───────────────── TITLE ─────────────────
st.set_page_config(
    page_icon="📳",
    page_title="Telecom | Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# PAGE CONFIG
# ==========================================

page_header(
    "Smartphone Analytics Dashboard",
    "AI-powered mobile analytics, pricing insights & device performance monitoring",
    "📱"
)
# ==========================================
# HEADER
# ==========================================

st.caption(
    f"Last Updated: {datetime.now().strftime('%d %B %Y • %H:%M:%S')}"
)

# ==========================================
# KPI SECTION
# ==========================================

section_header(
    "📊 Live Smartphone Insights",
    "Real-time insights generated dynamically from filtered smartphone data"
)

total_phones = filtered_df.shape[0]
avg_price = filtered_df["Price"].mean()
avg_ram = filtered_df["RAM"].mean()
avg_battery = filtered_df["Bty_Pwr"].mean()
avg_camera = filtered_df["Camera_Score"].mean()

col1,col2,col3,col4,col5 = st.columns(5)

with col1: kpi_card(col1, "📱 Total Phones", f"{total_phones}")
with col2: kpi_card(col2, "💰 Avg Price", f"₹ {avg_price:,.0f}")
with col3: kpi_card(col3, "🧠 Avg RAM", f"{avg_ram:.0f}")
with col4: kpi_card(col4, "🔋 Avg Battery", f"{avg_battery:.0f} mAh")
with col5: kpi_card(col5, "📸 Avg Camera", f"{avg_camera:.1f}")

# ==========================================
# LIVE INSIGHTS
# ==========================================

section_header(
    "⚡ Real-Time Executive Insights",
    "Automatically generated business insights based on current filters"
)

best_ram = filtered_df.loc[
    filtered_df["RAM"].idxmax()
]

best_battery = filtered_df.loc[
    filtered_df["Bty_Pwr"].idxmax()
]

executive_insight(
    what=f"There are currently {total_phones} smartphones matching the selected filters.",
    why="Filtered insights help users instantly focus on relevant smartphone segments.",
    impact=f"Average smartphone price is ₹ {avg_price:,.0f}, indicating current market positioning.",
    recommendation="Use filters dynamically to identify high-value smartphone categories."
)

executive_insight(
    what=f"Highest RAM device offers {best_ram['RAM']} RAM.",
    why="RAM strongly influences multitasking and gaming performance.",
    impact="High RAM devices are generally associated with premium pricing categories.",
    recommendation="Target high RAM devices when analyzing flagship smartphone performance."
)

executive_insight(
    what=f"Strongest battery device includes {best_battery['Bty_Pwr']} mAh capacity.",
    why="Battery life is one of the most important smartphone purchasing factors.",
    impact="Large battery devices attract gaming and multimedia users.",
    recommendation="Balance battery performance with pricing to identify strong value devices."
)

# ==========================================
# PRICE DISTRIBUTION
# ==========================================

section_header(
    "💰 Price Distribution Analysis",
    "Understand smartphone pricing trends in real time"
)

col6,col7 = st.columns(2)

with col6:

    chart_label(
        "📊 Price Histogram",
        "Distribution of smartphone prices"
    )

    fig = px.histogram(
        filtered_df,
        x="Price",
        nbins=20,
        color="Price"
    )

    fig.update_layout(**plotly_futuristic_layout())

    st.plotly_chart(fig, use_container_width=True)

with col7:

    chart_label(
        "📦 Price Boxplot",
        "Detect premium outliers and price spread"
    )

    fig = px.box(
        filtered_df,
        y="Price",
        color="RAM"
    )

    fig.update_layout(**plotly_futuristic_layout())

    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# FEATURE RELATIONSHIPS
# ==========================================

section_header(
    "🧠 Feature Relationships",
    "Analyze how hardware features impact smartphone pricing"
)

col8,col9 = st.columns(2)

with col8:

    chart_label(
        "🧠 RAM VS Price",
        "Relationship between RAM and smartphone pricing"
    )

    fig = px.scatter(
        filtered_df,
        x="RAM",
        y="Price",
        size="Bty_Pwr",
        color="RAM",
        hover_data=["Int_Mem","PC","FC"]
    )

    fig.update_layout(**plotly_futuristic_layout())

    st.plotly_chart(fig, use_container_width=True)

with col9:

    chart_label(
        "🔋 Battery VS Price",
        "Relationship between battery power and pricing"
    )

    fig = px.line(
        filtered_df.sort_values("Bty_Pwr"),
        x="Bty_Pwr",
        y="Price",
        markers=True
    )

    fig.update_layout(**plotly_futuristic_layout())

    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# CAMERA ANALYSIS
# ==========================================

section_header(
    "📷 Camera Intelligence",
    "Explore camera performance trends and pricing"
)

col10,col11 = st.columns(2)

with col10:

    chart_label(
        "📸 Camera Score VS Price",
        "Combined camera capability vs pricing"
    )

    fig = px.scatter(
        filtered_df,
        x="Camera_Score",
        y="Price",
        size="RAM",
        color="Camera_Score",
        hover_data=["PC","FC","Bty_Pwr"]
    )

    fig.update_layout(**plotly_futuristic_layout())

    st.plotly_chart(fig, use_container_width=True)

with col11:

    chart_label(
        "📱 Screen Size VS Price",
        "Display size impact on smartphone pricing"
    )

    fig = px.area(
        filtered_df.sort_values("Screen_Size"),
        x="Screen_Size",
        y="Price"
    )

    fig.update_layout(**plotly_futuristic_layout())

    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# TOP SMARTPHONES TABLE
# ==========================================

section_header(
    "🏆 Top Smartphones",
    "Highest value smartphones based on performance and pricing"
)

filtered_df["Value_Score"] = (
    filtered_df["RAM"] +
    filtered_df["Bty_Pwr"] +
    filtered_df["Camera_Score"]
) / filtered_df["Price"]

top_phones = filtered_df.sort_values(
    by="Value_Score",
    ascending=False
).head(10)

df_table(
    top_phones[
        [
            "PID",
            "Price",
            "RAM",
            "Bty_Pwr",
            "PC",
            "FC",
            "Camera_Score"
        ]
    ]
)

# ==========================================
# SMART RECOMMENDATION ENGINE
# ==========================================

section_header(
    "🏆 Smart Recommendation Engine",
    "Automatically identifies the best-value smartphone"
)

best_phone = filtered_df.sort_values(
    by="Value_Score",
    ascending=False
).iloc[0]

st.success(f"""
📱 Recommended Smartphone: {best_phone['PID']}

💰 Price: ₹ {best_phone['Price']:,.0f}

🧠 RAM: {best_phone['RAM']}

🔋 Battery: {best_phone['Bty_Pwr']} mAh

📸 Camera Score: {best_phone['Camera_Score']}

⭐ Value Score: {best_phone['Value_Score']:.4f}
""")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "📊 Smartphone Analytics Dashboard • Built with Streamlit & Plotly"
)