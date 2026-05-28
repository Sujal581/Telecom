import streamlit as st
import io
import pandas as pd
import plotly.express as px
from styles import (inject_css, sidebar_brand, page_header, section_header,
                   kpi_card, insight_card, footer, COLORS, chart_label, plotly_futuristic_layout, df_table, executive_insight,show_table)
from data import load_data, sidebar_filters

inject_css()
sidebar_brand()

# ───────────────── TITLE ─────────────────
st.set_page_config(
    page_icon="📳",
    page_title="Telecom | Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ───────────────── HEADER ─────────────────
page_header(
    "Overview Dashboard",
    "AI-powered mobile analytics, pricing insights & device performance monitoring",
    "📱"
)

df=load_data()
# ───────────────── KPI CARDS ─────────────────
avg_price = df["Price"].mean()
median_price = df["Price"].median()
avg_ram = df["RAM"].mean()
battery_weight = df["Weight"].mean()

col1,col2,col3,col4 = st.columns(4)
kpi_card(col1,"💰Average Price",f"₹{avg_price:,.0f}",color="#EF4444")
kpi_card(col2,"💸Median Price",f"₹{median_price:,.0f}",color="#F59E0B")
kpi_card(col3,"🧠Average RAM",f"{avg_ram:,.0f} GB",color="#3B82F6")
kpi_card(col4,"🔋Battery Weight",f"{battery_weight:.0f} g",color="#F59E0B")

section_header("📉Distribution Summary")
dcol1, dcol2, dcol3 = st.columns(3)

# ───────────────── PRICE RANGE ─────────────────
with dcol1:
    st.markdown(
        f"""
<div style="
    background: rgba(255,255,255,0.78);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(239,68,68,0.12);
    border-left: 4px solid #EF4444;
    padding: 1rem 1.2rem;
    border-radius: 18px;
    box-shadow: 0 4px 20px rgba(239,68,68,0.06);
">

<div style="
    color:#9CA3AF;
    font-size:0.72rem;
    font-weight:700;
    letter-spacing:0.08em;
">
💸 PRICE RANGE
</div>

<div style="
    color:#111827;
    font-size:1.45rem;
    font-weight:700;
    margin-top:0.65rem;
">
₹ {df["Price"].mean():,.0f}
</div>

<div style="margin-top:0.65rem;color:#6B7280;font-size:0.88rem;">
<strong>Min:</strong> ₹ {df["Price"].min():,.0f}
</div>

<div style="color:#6B7280;font-size:0.88rem;">
<strong>Max:</strong> ₹ {df["Price"].max():,.0f}
</div>

</div>
""",
        unsafe_allow_html=True
    )

# ───────────────── RAM RANGE ─────────────────
with dcol2:
    st.markdown(
        f"""
<div style="
    background: rgba(255,255,255,0.78);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(124,58,237,0.12);
    border-left: 4px solid #7C3AED;
    padding: 1rem 1.2rem;
    border-radius: 18px;
    box-shadow: 0 4px 20px rgba(124,58,237,0.06);
">

<div style="
    color:#9CA3AF;
    font-size:0.72rem;
    font-weight:700;
    letter-spacing:0.08em;
">
🧠 RAM RANGE
</div>

<div style="
    color:#111827;
    font-size:1.45rem;
    font-weight:700;
    margin-top:0.65rem;
">
{df["RAM"].mean():.1f} GB
</div>

<div style="margin-top:0.65rem;color:#6B7280;font-size:0.88rem;">
<strong>Min:</strong> {df["RAM"].min():,.0f} GB
</div>

<div style="color:#6B7280;font-size:0.88rem;">
<strong>Max:</strong> {df["RAM"].max():,.0f} GB
</div>

</div>
""",
        unsafe_allow_html=True
    )

# ───────────────── BATTERY RANGE ─────────────────
with dcol3:
    st.markdown(
        f"""
<div style="
    background: rgba(255,255,255,0.78);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(245,158,11,0.12);
    border-left: 4px solid #F59E0B;
    padding: 1rem 1.2rem;
    border-radius: 18px;
    box-shadow: 0 4px 20px rgba(245,158,11,0.06);
">

<div style="
    color:#9CA3AF;
    font-size:0.72rem;
    font-weight:700;
    letter-spacing:0.08em;
">
🔋 BATTERY RANGE
</div>

<div style="
    color:#111827;
    font-size:1.45rem;
    font-weight:700;
    margin-top:0.65rem;
">
{df["Bty_Pwr"].mean():,.0f} mAh
</div>

<div style="margin-top:0.65rem;color:#6B7280;font-size:0.88rem;">
<strong>Min:</strong> {df["Bty_Pwr"].min():,.0f} mAh
</div>

<div style="color:#6B7280;font-size:0.88rem;">
<strong>Max:</strong> {df["Bty_Pwr"].max():,.0f} mAh
</div>

</div>
""",
        unsafe_allow_html=True
    )


# ───────────────── PRICE DISTRIBUTION ─────────────────    
section_header("💰Price Distribution")
chart_label("Price Distribution","Show how smartphone prices are spread across different price range")
fig=px.histogram(df,x="Price",nbins=25,color_discrete_sequence=["#00F5FF"])
fig.update_layout(**plotly_futuristic_layout())
fig.update_xaxes(title="Prices")
fig.update_yaxes(title="Number of Phones")
st.plotly_chart(fig,use_container_width=True)
executive_insight(
    what="This chart shows how smartphone prices are distributed across different price ranges.",
    why="Most smartphone brands focus on mid-range devices because they attract the largest customer segment.",
    impact="A high concentration in the mid-price segment indicates strong market competition, while premium phones appear less frequently due to niche demand.",
    recommendation="Focus pricing and feature analysis on the mid-range segment to identify competitive opportunities and customer preferences."
)

# ───────────────── RAM & BATTERY DISTRIBUTION ─────────────────
col1,col2=st.columns(2)
with col1:
    section_header("🧠RAM Distrinution")
    chart_label("RAM Distribution","Visualizes the speed of RAM capacity among the smartphones model")
    fig=px.histogram(df,x="RAM",nbins=20,color_discrete_sequence=["#AB63FA"])
    fig.update_layout(**plotly_futuristic_layout())
    fig.update_xaxes(title="RAM")
    fig.update_yaxes(title="Number of Phones")
    st.plotly_chart(fig,width="content")
    executive_insight(
        what="This chart shows how RAM capacity is distributed across smartphone models.",
        why="Most smartphone manufacturers focus on mid-range RAM configurations to balance performance and affordability.",
        impact="Higher RAM devices generally target gaming, multitasking, and premium user segments.",
        recommendation="Analyze high-RAM segments to identify premium market opportunities and performance trends."
    )

with col2:
    section_header("🔋Battery Distribution")
    chart_label("Battery Distribution","Displays how battery capacity vary across smartphones model")
    fig=px.histogram(df,x="Bty_Pwr",nbins=20,color_discrete_sequence=["#FFA15A"])
    fig.update_layout(**plotly_futuristic_layout())
    fig.update_xaxes(title="Battery Power")
    fig.update_yaxes(title="Number of Phones")
    st.plotly_chart(fig,width="content")
    executive_insight(
        what="This chart displays the distribution of smartphone battery capacities.",
        why="Battery power is one of the most important factors influencing smartphone usability and customer preference.",
        impact="Devices with larger batteries are often associated with premium usage scenarios such as gaming, streaming, and productivity.",
        recommendation="Focus on battery optimization trends to understand consumer demand for long-lasting devices."
    )

section_header("📲Smartphone Dataset Preview")
chart_label("Smartphones Record","Interactive dataframe containing smartphone hardware specifications and prices")
df_table(df.head(20),height=450)


# ───────────────── INSIGHTS ─────────────────
section_header("📌 Insights")
insight_card("📱 Most samrtphones are concentrated in the mid-proce segment, while premium appear less frequently.",kind="cyan")
insight_card("🧠 Most devices cluster around mid-range RAM configurations, including balanced performance offerings.")
insight_card("🔋 Battery capacities are mostly centered around medium-to-high ranges, reflecting modern long-lasting smartphones trends.",kind="success")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "📊 Smartphone Analytics Dashboard • Built with Streamlit & Plotly"
)