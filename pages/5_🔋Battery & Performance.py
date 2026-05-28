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
    "Battery & Performance Dashboard",
    "AI-powered mobile analytics, pricing insights & device performance monitoring",
    "🔋"
)

avg_battery = df["Bty_Pwr"].mean()
max_battery = df["Bty_Pwr"].max()
battery_price = df["Bty_Pwr"].corr(df["Price"])
battery_weight = df["Bty_Pwr"].corr(df["Weight"])

col1,col2,col3,col4=st.columns(4)
kpi_card(col1,"🔋 Average Battery",f"{avg_battery:.0f} mAh",color="#700000")
kpi_card(col2,"📈 Maximum Battery",f"{max_battery:.0f} mAh",color="#E45555")
kpi_card(col3,"💸 Battery vs Price",f"{battery_price:.2f}",color="#F40404")
kpi_card(col4,"⚖️ Battery vs Weigh",f"{battery_weight:.2f}",color="#950606")

section_header("🔋 Battery Performance Analysis")
col1,col2=st.columns(2)
with col1:
    chart_label("🔋 Battery vs Price","Shows how smartphone prices vary across different battery capacities")
    fig_battery_price = px.line(df.sort_values("Bty_Pwr"),x="Bty_Pwr",y="Price",markers=True)
    fig_battery_price.update_layout(**plotly_futuristic_layout())
    fig_battery_price.update_xaxes(title="Battery Power (mAh)")
    fig_battery_price.update_yaxes(title="Price")
    st.plotly_chart(fig_battery_price, use_container_width=True)
    executive_insight(
        what="This line chart examines how smartphone pricing changes across different battery capacities.",
        why="Battery performance is a major purchasing factor for users seeking longer usage time and better device reliability.",
        impact="Higher-capacity batteries generally appear in mid-range and premium smartphones, though battery size alone does not fully determine pricing.",
        recommendation="Combine battery analysis with performance and display features to identify smartphones offering the best long-term value."
    )

with col2:
    chart_label("⚖️ Battery vs Weight","Analyzes how battery size impacts smartphone weight")
    fig_battery_weight = px.bar(df.sort_values("Bty_Pwr").head(30),x="Bty_Pwr",y="Weight",color="Weight")
    fig_battery_weight.update_layout(**plotly_futuristic_layout())
    fig_battery_weight.update_xaxes(title="Battery Power (mAh)")
    fig_battery_weight.update_yaxes(title="Weight (g)")
    st.plotly_chart(fig_battery_weight, use_container_width=True)
    executive_insight(
        what="This bar chart explores the relationship between battery capacity and smartphone weight.",
        why="Larger batteries often require additional physical space and materials, which can increase overall device weight.",
        impact="Devices with higher battery capacities generally trend toward heavier designs, especially in gaming and performance-focused smartphones.",
        recommendation="Identify smartphones that optimize battery capacity while maintaining lightweight and ergonomic designs."
    )

col3,col4=st.columns(2)
with col3:
    chart_label("🧠 RAM vs Battery","Examines how RAM configurations relate to battery capacity")
    ram_battery_avg = (df.groupby("RAM")["Bty_Pwr"].mean().reset_index())
    fig_ram_battery = px.area(ram_battery_avg,x="RAM",y="Bty_Pwr")
    fig_ram_battery.update_layout(**plotly_futuristic_layout())
    fig_ram_battery.update_xaxes(title="RAM")
    fig_ram_battery.update_yaxes(title="Average Battery Power (mAh)")
    st.plotly_chart(fig_ram_battery, use_container_width=True)
    executive_insight(
        what="This area chart analyzes the relationship between RAM configurations and average battery capacity.",
        why="Higher RAM devices typically support advanced multitasking and gaming workloads, which often require stronger battery performance.",
        impact="Smartphones with larger RAM capacities generally feature higher battery capacities to support increased power consumption.",
        recommendation="Focus on balancing RAM and battery optimization to deliver better performance efficiency and longer device usage."
    )

with col4:
    df["Screen_Size"] = df["Scr_h"] * df["Scr_w"]
    chart_label("📱 Screen Size vs Battery Capacity", "Shows how display size influences battery requirements")
    screen_battery_avg = (df.groupby("Screen_Size")["Bty_Pwr"].mean().reset_index())
    fig_screen_battery = px.line(screen_battery_avg,x="Screen_Size",y="Bty_Pwr",markers=True)
    fig_screen_battery.update_layout(**plotly_futuristic_layout())
    fig_screen_battery.update_xaxes(title="Screen Size")
    fig_screen_battery.update_yaxes(title="Average Battery Power (mAh)")
    st.plotly_chart(fig_screen_battery, use_container_width=True)
    executive_insight(
        what="This chart examines how smartphone screen size impacts battery capacity requirements.",
        why="Larger displays consume more power due to increased brightness, resolution, and screen activity.",
        impact="Smartphones with larger screens generally include higher battery capacities to maintain acceptable battery life and performance.",
        recommendation="Analyze display-to-battery optimization trends to identify devices that balance immersive viewing experiences with strong battery efficiency."
    )

# ───────────────── INSIGHTS ─────────────────
section_header("🔥 Important Performance Insights",)
insight_card("🔋 Battery capacity positively impacts smartphone pricing and is strongly associated with performance-focused devices.",kind="success")
insight_card("⚖️ Larger batteries slightly increase smartphone weight because of added hardware requirements.",kind="cyan")
insight_card("🧠 High-performance smartphones combine larger RAM and battery capacities for multitasking and gaming.",kind="success")
insight_card("📱 Bigger smartphone displays usually require larger batteries to support increased power consumption.",kind="purple")
insight_card("🚀 Premium smartphones optimize battery, RAM, and display size together to deliver balanced hardware efficiency.")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "📊 Smartphone Analytics Dashboard • Built with Streamlit & Plotly"
)