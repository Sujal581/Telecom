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
    "Camera Analysis dashboard",
    "AI-powered mobile analytics, pricing insights & device performance monitoring",
    "📷"
)

# ───────────────── KPI CARDS ─────────────────
avg_pc = df["PC"].mean()
avg_fc = df["FC"].mean()
camera_score = (df["PC"]+df["FC"]).mean()
pc_price_corr = df["PC"].corr(df["Price"])
fc_price_corr = df["FC"].corr(df["Price"])

col1,col2,col3,col4,col5=st.columns(5)
kpi_card(col1,"📹 Primary Camera",f"{avg_pc:.1f} MP",color="#700000")
kpi_card(col2,"📷 Font Camera",f"{avg_pc:.1f} MP",color="#E45555")
kpi_card(col3,"💯 Average Camera Score",f"{avg_pc:.1f} %",color="#F40404")
kpi_card(col4,"💸 Primary Camera VS Price",f"{avg_pc:.1f} %",color="#950606")
kpi_card(col5,"💸 Font Camera VS Price",f"{avg_pc:.2f} %",color="#FF0000")

# ───────────────── CAMERA ANALYSIS ─────────────────
section_header("📷 Camera Analysis")

col1,col2=st.columns(2)

with col1:
    chart_label("📹 Primary Camera VS Price","Analyze how primary camera quality impacts smartphone pricing")
    fig=px.scatter(df,x="PC",y="Price",color="PC",size="RAM",hover_data=["FC","Int_Mem","Bty_Pwr"])
    fig.update_layout(**plotly_futuristic_layout())
    fig.update_xaxes(title="Primary Camera")
    fig.update_yaxes(title="Price")
    st.plotly_chart(fig,use_container_width=True)
    executive_insight(
        what="This scatter plot analyzes the relationship between primary camera quality and smartphone pricing.",
        why="Primary camera performance is one of the strongest consumer purchasing factors in modern smartphones.",
        impact="Devices with higher primary camera specifications generally appear in premium price segments, highlighting the importance of photography-focused smartphones.",
        recommendation="Focus on balancing camera quality and pricing to identify smartphones that provide strong photography performance at competitive value."
    )

with col2:
    chart_label("📷 Front Camera VS Price","Examines the relationship between selfie camera quality and smartphone pricing")
    fc_avg = (df.groupby("FC")["Price"].mean().reset_index())
    fig=px.line(fc_avg,x="FC",y="Price",markers=True)
    fig.update_layout(**plotly_futuristic_layout())
    fig.update_xaxes(title="Front Camera")
    fig.update_yaxes(title="Average Price")
    st.plotly_chart(fig,use_container_width=True)
    executive_insight(
        what="This line chart explores how front camera quality influences smartphone pricing trends.",
        why="High-quality selfie cameras are increasingly important for social media, video calls, and content creation.",
        impact="Smartphones with stronger front camera specifications generally trend toward higher average pricing categories.",
        recommendation="Analyze selfie camera improvements alongside overall device pricing to identify balanced consumer-focused smartphones."
    )

col3,col4=st.columns(2)
with col3:
    df["Camera_Score"]=df["PC"]+df["FC"]
    chart_label("💯 Camera Score VS Price","Shows how combined camera capabilities influence smartphone pricing")
    fig=px.density_heatmap(df,x="Camera_Score",y="Price",nbinsx=20,nbinsy=20)
    fig.update_layout(**plotly_futuristic_layout())
    fig.update_xaxes(title="Camera Score")
    fig.update_yaxes(title="Price")
    st.plotly_chart(fig,use_container_width=True)
    executive_insight(
        what="This heatmap visualizes pricing concentration based on combined camera performance.",
        why="Overall camera capability strongly impacts smartphone value perception and purchasing decisions.",
        impact="Most premium smartphones cluster within higher camera score and higher price ranges.",
        recommendation="Use combined camera analysis to identify feature-rich smartphones with strong multimedia capabilities and optimized pricing."
    )

with col4:
    df["Camera_Score"]=df["PC"]+df["FC"]
    chart_label("🧠 RAM VS Camera Performance","Visualizes the relationship between RAM, camera strength and smartphone pricing")
    fig=px.scatter(df,x="RAM",y="Camera_Score",color="Price",size="Price",hover_data=["PC","FC","Int_Mem","Bty_Pwr"],opacity=0.7)
    fig.update_layout(**plotly_futuristic_layout())
    fig.update_xaxes(title="RAM")
    fig.update_yaxes(title="Camera Score")
    st.plotly_chart(fig,use_container_width=True)
    executive_insight(
        what="This bubble chart analyzes the combined relationship between RAM, camera performance, and smartphone pricing.",
        why="Modern premium smartphones typically combine high-performance hardware with advanced camera systems.",
        impact="Devices with both larger RAM capacities and stronger camera performance consistently occupy higher pricing tiers.",
        recommendation="Identify smartphones that efficiently balance performance and camera capabilities to maximize customer value."
    )

# ───────────────── INSIGHTS ─────────────────
section_header("🔥 Important Camera Insights")
insight_card("📷 Smartphones with stronger primary cameras are generally positioned in premium pricing categories.",kind="cyan")
insight_card("🤳 Devices with higher front camera resolutions tend to target content creators and premium users.",kind="success")
insight_card("📸 Smartphones offering stronger overall camera systems are consistently associated with higher market value.",kind="purple")
insight_card("🧠 Premium smartphones often combine high RAM and advanced camera systems to target performance-focused users.",kind="cyan")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "📊 Smartphone Analytics Dashboard • Built with Streamlit & Plotly"
)