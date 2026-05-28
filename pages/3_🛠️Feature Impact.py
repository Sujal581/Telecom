import streamlit as st
import io
import pandas as pd
import plotly.express as px
from styles import (inject_css, sidebar_brand, page_header, section_header,
                   kpi_card, insight_card, footer, COLORS, chart_label, plotly_futuristic_layout, df_table, executive_insight,show_table)
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
    "Feature Impact Dashboard",
    "AI-powered mobile analytics, pricing insights & device performance monitoring",
    "🛠️"
)

# ───────────────── KPI CARDS ─────────────────
avg_ram = df["RAM"].mean()
avg_battery = df["Bty_Pwr"].mean()
battery_weight = df["Weight"].mean()
avg_storage = df["Int_Mem"].mean()

col1,col2,col3,col4=st.columns(4)
kpi_card(col1,"🧠 Average RAM",f"{avg_ram:,.0f} GB",color="#EF4444")
kpi_card(col2,"🔋 Average Battery",f"{avg_battery:,.0f} mAh",color="#771313")
kpi_card(col3,"💾 Average Storage",f"{avg_storage:,.0f} GB",color="#E91313")
kpi_card(col4,"⚖️ Average Weight",f"{battery_weight:,.0f} g",color="#710E0E")

# ───────────────── CORRELATION CHART ─────────────────
section_header("🛠️ Feature Impact Analysis")
chart_label("🔥 Correlation Heatmap","Display relationships between smartphones specifications and pricing")
corr_columns=["Price","RAM","Bty_Pwr","Int_Mem","PC","FC","Weight","Px_h","Px_w","Scr_h","Scr_w"]
corr_metrix=df[corr_columns].corr()
fig=px.imshow(corr_metrix,text_auto=True,aspect="auto",color_continuous_scale="Turbo")
fig.update_layout(**plotly_futuristic_layout())
st.plotly_chart(fig,use_container_width=True)
executive_insight(
    what="This correlation heatmap visualizes the relationships between smartphone specifications and pricing.",
    why="Correlation analysis helps identify which hardware features have the strongest influence on smartphone prices and overall market positioning.",
    impact="Features such as RAM, internal memory, camera quality, and screen resolution often show stronger positive correlations with pricing, indicating their importance in premium device segmentation.",
    recommendation="Prioritize highly correlated features when performing pricing strategy, feature engineering, or predictive modeling for smartphone market analysis."
)

# ───────────────── FEATURE BASED PRICING ─────────────────
col1,col2=st.columns(2)
with col1:
        chart_label("🛜 Price By Wifi","Compares pricing distribution between smartphones with and without WiFi support")
        wifi_avg = (df.groupby("Wi_Fi")["Price"].mean().reset_index())
        fig=px.bar(wifi_avg,x="Wi_Fi",y="Price",color="Wi_Fi",text_auto=".0f")
        fig.update_layout(**plotly_futuristic_layout())
        fig.update_xaxes(title="Wifi Support")
        fig.update_yaxes(title="Average Price")
        st.plotly_chart(fig,use_container_width=True)
        executive_insight(
            what="This bar chart compares average smartphone pricing based on WiFi support availability.",
            why="WiFi connectivity is a standard feature that significantly improves smartphone usability and internet accessibility.",
            impact="Devices with WiFi support dominate the smartphone market across all pricing categories.",
            recommendation="Combine connectivity analysis with hardware specifications to identify smartphones offering balanced value and performance."
        )

with col2:
        chart_label("📱 Price By Touch Screen","Compares smartphone pricing between touchscreen and non-touchscreen devices")
        touch_avg = (df.groupby("Tch_Scr")["Price"].mean().reset_index())
        fig=px.pie(touch_avg,names="Tch_Scr",values="Price",hole=0.5)
        fig.update_layout(**plotly_futuristic_layout())
        st.plotly_chart(fig,use_container_width=True)
        executive_insight(
            what="This donut chart visualizes smartphone pricing distribution based on touchscreen availability.",
            why="Touchscreen functionality is one of the most important features driving modern smartphone adoption.",
            impact="Most premium smartphones belong to the touchscreen category, highlighting its dominance in the current market.",
            recommendation="Prioritize touchscreen device analysis because they represent the most commercially relevant smartphone segment."
        )

col3,col4=st.columns(2)
with col3:
        chart_label("ᛒ Price By Bluetooth","Compares smartphone pricing based on Bluetooth support")
        fig=px.box(df,x="Blue",y="Price",color="Blue")
        fig.update_layout(**plotly_futuristic_layout())
        fig.update_xaxes(title="Bluetooth Support")
        fig.update_yaxes(title="Price")
        st.plotly_chart(fig,use_container_width=True)
        executive_insight(
            what="This boxplot analyzes smartphone pricing variation based on Bluetooth support.",
            why="Bluetooth functionality is essential for wireless accessories, smart devices, and ecosystem connectivity.",
            impact="Bluetooth-enabled smartphones are present across nearly all price categories, showing its importance as a core smartphone feature.",
            recommendation="Combine Bluetooth support analysis with premium hardware features to identify high-value smartphones."
        )

with col4:
        df["Screen_Size"]=df["Scr_h"]*df["Scr_w"]
        chart_label("📱 Screen Size VS Price","Analyzes how smartphone screen size impacts pricing trends")
        screen_avg = (df.groupby("Screen_Size")["Price"].mean().reset_index())
        fig=px.area(screen_avg,x="Screen_Size",y="Price")
        fig.update_layout(**plotly_futuristic_layout())
        fig.update_xaxes(title="Screen Size")
        fig.update_yaxes(title="Average Price")
        st.plotly_chart(fig,use_container_width=True)
        executive_insight(
            what="This area chart examines how smartphone pricing changes across different screen sizes.",
            why="Larger displays improve gaming, entertainment, and productivity experiences for users.",
            impact="Smartphones with larger displays generally trend toward higher pricing categories, especially premium entertainment-focused devices.",
            recommendation="Identify the optimal balance between screen size and pricing to target users seeking immersive smartphone experiences."
        )

# ───────────────── INSIGHTS ─────────────────
section_header("🔥 Important Feature Insights")
insight_card("🔥 RAM, Internal Memory and Battery Power show the strongest positive relationships with smartphone pricing.",kind="success")
insight_card("🧠 RAM appears to be one of the strongest pricing factors, with higher RAM devices consistemtly positioned in permium price range.",kind="cyan")
insight_card("🔋 Smartphones with larger batteries generally trend toward higher pricing, especially performance-oriented devices.",kind="purple")
insight_card("📱 Larger screen smartphones are commonly associated with mid-to-premium pricing categories.",kind="success")
insight_card("⚖️ Heavier smartphones often include larger battery and premium hardware, contributting to higher prices.",kind="cyan")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "📊 Smartphone Analytics Dashboard • Built with Streamlit & Plotly"
)