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
    "Price Analysis Dashboard",
    "AI-powered mobile analytics, pricing insights & device performance monitoring",
    "💰"
)

# ───────────────── KPI CARDS ─────────────────
avg_price = df["Price"].mean()
median_price = df["Price"].median()
min_price = df["Price"].min()
max_price = df["Price"].max()

col1,col2,col3,col4 = st.columns(4)
kpi_card(col1,"💰 Average Price",f"₹{avg_price:,.0f}",color="#EF4444")
kpi_card(col2,"💸 Median Price",f"₹{median_price:,.0f}",color="#F59E0B")
kpi_card(col3,"🔻 Minimum Price",f"₹{min_price:,.0f}",color="#3B82F6")
kpi_card(col4,"🔺 Maximmum Price",f"₹{max_price:.0f}",color="#F59E0B")


# ───────────────── PRICE DISTRIBUTION ─────────────────   
st.markdown("---") 
tab1, tab2 = st.tabs(["💰 Price Analysis", "📱 Feature-Based Price Analysis"])
with tab1:
    col1,col2=st.columns(2)
    with col1:
        section_header("💰 Price Analysis")
        chart_label("📦 Price Boxplot","Show how smartphone prices are spread across different price range")
        fig=px.box(df,y="Price",color_discrete_sequence=["#AB63FA"])
        fig.update_layout(**plotly_futuristic_layout())
        fig.update_yaxes(title="Price")
        st.plotly_chart(fig,use_container_width=True)
        executive_insight(
            what="This boxplot visualizes the spread and variation of smartphone prices across the dataset.",
            why="The chart helps identify the median price range, pricing consistency, and premium outliers within the smartphone market.",
            impact="A wide price spread indicates the presence of multiple market segments including budget, mid-range, and flagship devices. Premium outliers highlight niche high-end competition.",
            recommendation="Focus competitive analysis on the mid-range segment since it contains the highest concentration of smartphones and customer demand."
        )

    with col2:
        section_header("🧠 RAM VS Price")
        chart_label("🧠 RAM Vs Price","Analysis how RAM capacity impacts smartphones pricing")
        fig=px.scatter(df,x="RAM",y="Price",size="RAM",hover_data=["Int_Mem","Bty_Pwr"])
        fig.update_layout(**plotly_futuristic_layout())
        fig.update_xaxes(title="RAM")
        fig.update_yaxes(title="Price")
        st.plotly_chart(fig,width="content")
        executive_insight(
            what="This scatter plot analyzes the relationship between smartphone RAM capacity and pricing.",
            why="Higher RAM configurations improve multitasking, gaming performance, and overall device responsiveness.",
            impact="Devices with larger RAM capacities consistently trend toward higher price segments, reflecting their premium performance positioning.",
            recommendation="Identify the most cost-efficient RAM configurations within the mid-range category to maximize consumer value."
        )

    col3,col4=st.columns(2)
    with col3:
        section_header("🔋 Battery VS Price")
        chart_label("🔋 Battery VS Price","Examine the relationship between battery capacity and smartphones price")
        fig=px.scatter(df,x="Bty_Pwr",y="Price",size="RAM",color="Bty_Pwr",hover_data=["Int_Mem"])
        fig.update_layout(**plotly_futuristic_layout())
        fig.update_xaxes(title="Battery Power")
        fig.update_yaxes(title="Price")
        st.plotly_chart(fig,width="content")
        executive_insight(
            what="This chart explores how battery capacity influences smartphone pricing trends.",
            why="Battery life is one of the most important factors affecting user experience, especially for gaming and productivity-focused devices.",
            impact="Higher-capacity batteries are commonly associated with premium smartphones and performance-oriented models.",
            recommendation="Analyze battery efficiency alongside pricing to identify devices offering strong endurance at competitive value."
        )
    with col4:
        section_header("💾 Internal Memory VS Price")
        chart_label("💾 Internal Memory VS Price","Examine the relationship between internal memory and smartphones price")
        fig=px.scatter(df,x="Int_Mem",y="Price",size="RAM",color="Int_Mem",hover_data=["Bty_Pwr"])
        fig.update_layout(**plotly_futuristic_layout())
        fig.update_xaxes(title="Internal Memory")
        fig.update_yaxes(title="Price")
        st.plotly_chart(fig,width="content")
        executive_insight(
            what="This scatter plot highlights the relationship between internal storage capacity and smartphone pricing.",
            why="Higher internal memory allows users to store more applications, media files, and system data efficiently.",
            impact="Smartphones with larger storage capacities generally command higher prices due to increased consumer demand for storage flexibility.",
            recommendation="Focus on identifying storage configurations that provide strong value without significantly increasing device pricing."
        )

    # ───────────────── INSIGHTS ─────────────────

    section_header("🔥 Important Pricing Insights")
    insight_card("💰 Pricing Insight: Most smartphones are concentrated in the mid-range pricing category, indicating strong competition in affordable premium devices.",kind="success")
    insight_card("🧠 RAM Insight: Smartphones with higher RAM configurations consistently trend toward higher price segments.",kind="cyan")
    insight_card("💾 Storage Insight: Devices offering larger internal memory capacities are generally priced significantly higher.",kind="purple")
    insight_card("🔋 Battery Insight: Higher battery capacities slightly increase smartphone prices, especially in gaming and performance-focused devices.")

with tab2:
    section_header("💰 Price Analysis By Feature")
    col1,col2=st.columns(2)
    with col1:
        chart_label("🛜 Price By Wifi","Compares pricing between phones with and without Wifi support")
        fig=px.violin(df,x="Wi_Fi",y="Price",points="all",box=True,color="Wi_Fi")
        fig.update_layout(**plotly_futuristic_layout())
        fig.update_xaxes(title="Wifi Support")
        fig.update_yaxes(title="Price")
        st.plotly_chart(fig,use_container_width=True)
        executive_insight(
            what="This violin plot compares smartphone price distributions based on WiFi support availability.",
            why="WiFi connectivity is considered a standard feature in modern smartphones and plays an important role in user experience.",
            impact="Devices with WiFi support appear across all pricing categories, indicating that wireless connectivity has become an essential smartphone feature.",
            recommendation="Focus on combining connectivity features with hardware specifications to identify smartphones offering the best overall value."
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
        chart_label("📱Screen Size VS Price","Analyze how smartphone screen size impacts pricing trends")
        fig=px.scatter(df,x="Screen_Size",y="Price",size="RAM",color="Screen_Size",hover_data=["Bty_Pwr"])
        fig.update_layout(**plotly_futuristic_layout())
        fig.update_xaxes(title="Screen Size")
        fig.update_yaxes(title="Price")
        st.plotly_chart(fig,width="content")
        executive_insight(
            what="This scatter plot examines the relationship between smartphone screen size and pricing trends.",
            why="Larger displays improve gaming, streaming, and productivity experiences, making screen size an important consumer preference factor.",
            impact="Smartphones with larger screens generally trend toward higher price categories, especially within premium and entertainment-focused segments.",
            recommendation="Identify the optimal screen-size-to-price balance to target users seeking immersive experiences at competitive pricing."
        )

    # ───────────────── INSIGHTS ─────────────────
    insight_card("📱 Feature Insight: Phones supporting modern features like Touch Screen, WiFi, and Bluetooth dominate the premium market category.",kind="success")
    insight_card("📈 Market Insight: A small number of flagship devices create noticeable premium outliers in the overall price distribution.",kind="cyan")

    # ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "📊 Smartphone Analytics Dashboard • Built with Streamlit & Plotly"
)