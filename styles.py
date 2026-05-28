"""
style.py — APL Logistics · Futuristic LIGHT-THEME edition
Fixed: dataframe dark-theme override + chart label text color set to black.
"""

import streamlit as st

# ── PALETTE ───────────────────────────────────────────────────────────────────
COLORS = {
    "blue":      "#3B82F6",
    "green":     "#10B981",
    "amber":     "#F59E0B",
    "red":       "#EF4444",
    "purple":    "#8B5CF6",
    "cyan":      "#06B6D4",
    "pink":      "#EC4899",
    "primary":   "#4F46E5",
    "secondary": "#7C3AED",
    "accent":    "#06B6D4",
    "success":   "#10B981",
    "warning":   "#F59E0B",
    "danger":    "#EF4444",
}
COLOR_SEQ = [
    "#4F46E5","#7C3AED","#06B6D4","#10B981",
    "#F59E0B","#EF4444","#8B5CF6","#EC4899",
]
GRADIENT_SEQ = COLOR_SEQ

# ── PLOT DEFAULTS ─────────────────────────────────────────────────────────────
PLOT_LAYOUT = dict(
    template="plotly_white",
    paper_bgcolor="rgba(255,255,255,0)",
    plot_bgcolor="rgba(255,255,255,0)",
    font=dict(family="Inter, sans-serif", color="#111827", size=12),
    xaxis=dict(
        gridcolor="rgba(79,70,229,0.07)",
        zeroline=False,
        linecolor="rgba(79,70,229,0.12)",
        tickfont=dict(color="#111827", size=11),
        title_font=dict(color="#111827", size=12),
    ),
    yaxis=dict(
        gridcolor="rgba(79,70,229,0.07)",
        zeroline=False,
        linecolor="rgba(79,70,229,0.12)",
        tickfont=dict(color="#111827", size=11),
        title_font=dict(color="#111827", size=12),
    ),
    margin=dict(l=16, r=16, t=40, b=16),
    legend=dict(
        bgcolor="rgba(255,255,255,0.90)",
        bordercolor="rgba(79,70,229,0.15)",
        borderwidth=1,
        font=dict(size=11, color="#111827"),
    ),
    hoverlabel=dict(
        bgcolor="rgba(255,255,255,0.97)",
        bordercolor="rgba(79,70,229,0.2)",
        font=dict(color="#111827", size=12, family="Inter"),
    ),
)

# ── FONT LINKS ────────────────────────────────────────────────────────────────
_FONT_LINKS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Inter:wght@300;400;500;600;700;800'
    '&family=Orbitron:wght@400;700;900'
    '&family=Rajdhani:wght@400;500;600;700'
    '&display=swap">'
)

PREMIUM_CSS = """
<style>

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* ── APP BACKGROUND ── */
.stApp {
    background: linear-gradient(135deg, #EEF2FF 0%, #F5F7FB 50%, #EDE9FE 100%) !important;
    color: #111827 !important;
}

footer { visibility: hidden; }

.block-container {
    padding: 1.5rem 2.5rem 3rem 2.5rem !important;
    max-width: 1400px;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(255,255,255,0.97) 0%, rgba(238,242,255,0.97) 100%) !important;
    border-right: 1px solid rgba(79,70,229,0.14) !important;
    backdrop-filter: blur(20px) !important;
    box-shadow: 4px 0 32px rgba(79,70,229,0.06) !important;
    visibility: visible !important;
    display: flex !important;
}

[data-testid="stSidebar"] .block-container {
    padding: 1.5rem 1rem !important;
}

/* ── Sidebar toggle — always visible ── */
[data-testid="collapsedControl"],
button[data-testid="collapsedControl"],
[data-testid="stSidebarCollapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    color: #4F46E5 !important;
}

[data-testid="stSidebarNav"] a {
    border-radius: 8px !important;
    padding: 0.5rem 0.75rem !important;
    font-size: 0.875rem !important;
    font-weight: 500 !important;
    color: #6B7280 !important;
    margin: 2px 0 !important;
    transition: all 0.2s ease !important;
    border: 1px solid transparent !important;
}

[data-testid="stSidebarNav"] a:hover {
    background: rgba(79,70,229,0.07) !important;
    color: #4F46E5 !important;
    border-color: rgba(79,70,229,0.18) !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(79,70,229,0.10) !important;
    color: #4F46E5 !important;
    border-left: 3px solid #4F46E5 !important;
    box-shadow: 0 0 12px rgba(79,70,229,0.12) !important;
}

[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .stMarkdown div { color: #6B7280 !important; font-size: 0.82rem !important; }

[data-testid="stSidebar"] hr {
    border-color: rgba(79,70,229,0.1) !important;
    margin: 0.75rem 0 !important;
}

/* ── TYPOGRAPHY ── */
h1 {
    font-family: 'Orbitron', sans-serif !important;
    font-size: 1.75rem !important;
    font-weight: 700 !important;
    color: #111827 !important;
    letter-spacing: 0.04em;
    margin-bottom: 0.25rem !important;
}
h2 {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1.3rem !important;
    font-weight: 700 !important;
    color: #1E293B !important;
    letter-spacing: 0.02em;
}
h3 {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    color: #374151 !important;
}
p, li { color: #6B7280; line-height: 1.7; }

/* ── KPI CARDS ── */
.nc-kpi-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.92), rgba(238,242,255,0.88));
    border-left: 3px solid;
    border-top: 1px solid rgba(255,255,255,0.9);
    border-right: 1px solid rgba(79,70,229,0.06);
    border-bottom: 1px solid rgba(79,70,229,0.06);
    border-radius: 14px;
    padding: 1.1rem 1.25rem;
    margin-bottom: 0.5rem;
    box-shadow: 0 4px 20px rgba(79,70,229,0.08), inset 0 1px 0 rgba(255,255,255,0.9);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    cursor: default;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(12px);
}
.nc-kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(79,70,229,0.25), transparent);
}
.nc-kpi-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(79,70,229,0.14), 0 0 20px rgba(79,70,229,0.06);
}
.nc-kpi-icon { font-size: 1.1rem; margin-bottom: 0.4rem; }
.nc-kpi-label {
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    color: #9CA3AF;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.3rem;
}
.nc-kpi-value {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.45rem;
    font-weight: 700;
    line-height: 1;
}
.nc-kpi-delta { font-size: 0.75rem; color: #9CA3AF; margin-top: 0.35rem; }

/* ── SECTION HEADER ── */
.nc-section-header {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #4F46E5;
    margin: 1.75rem 0 0.75rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(79,70,229,0.14);
    letter-spacing: 0.07em;
    text-transform: uppercase;
}

/* ── CHART LABELS ── */
.nc-chart-label {
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.2rem;
    letter-spacing: 0.03em;
}
.nc-chart-sub { font-size: 0.75rem; color: #9CA3AF; margin-bottom: 0.5rem; }

/* ── INSIGHT CARDS ── */
.nc-insight {
    border-left: 3px solid;
    border-radius: 10px;
    padding: 0.85rem 1.1rem;
    margin-bottom: 0.75rem;
    font-size: 0.875rem;
    line-height: 1.65;
    color: #374151;
    backdrop-filter: blur(4px);
}

/* ── STREAMLIT METRIC ── */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.88) !important;
    border: 1px solid rgba(79,70,229,0.12) !important;
    border-radius: 12px !important;
    padding: 1rem 1.25rem !important;
    transition: transform 0.2s ease !important;
    backdrop-filter: blur(12px) !important;
}
[data-testid="stMetric"]:hover { transform: translateY(-2px) !important; }
[data-testid="stMetricLabel"] {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    color: #9CA3AF !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Orbitron', sans-serif !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    color: #111827 !important;
}

/* ── BUTTONS ── */
.stButton > button {
    background: rgba(255,255,255,0.88) !important;
    color: #4F46E5 !important;
    border: 1px solid rgba(79,70,229,0.25) !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    padding: 0.45rem 1.1rem !important;
    transition: all 0.2s ease !important;
    backdrop-filter: blur(8px) !important;
}
.stButton > button:hover {
    background: rgba(79,70,229,0.08) !important;
    border-color: #4F46E5 !important;
    color: #4F46E5 !important;
    box-shadow: 0 0 14px rgba(79,70,229,0.18) !important;
}

/* ── INPUTS ── */
.stTextInput > div > div > input,
.stSelectbox > div > div,
.stDateInput > div > div > input {
    background: rgba(255,255,255,0.88) !important;
    border: 1px solid rgba(79,70,229,0.18) !important;
    border-radius: 8px !important;
    color: #111827 !important;
    font-size: 0.85rem !important;
}

/* ── DATAFRAME — force full light theme ── */
[data-testid="stDataFrame"] {
    border: 1px solid rgba(79,70,229,0.12) !important;
    border-radius: 14px !important;
    overflow: hidden !important;
    box-shadow: 0 4px 20px rgba(79,70,229,0.07) !important;
}

/* AG-Grid CSS variable overrides (light palette) */
[data-testid="stDataFrame"] [class*="ag-theme"] {
    --ag-background-color: #ffffff !important;
    --ag-foreground-color: #111827 !important;
    --ag-secondary-foreground-color: #374151 !important;
    --ag-header-background-color: #EEF2FF !important;
    --ag-header-foreground-color: #4F46E5 !important;
    --ag-odd-row-background-color: rgba(238,242,255,0.40) !important;
    --ag-even-row-background-color: #ffffff !important;
    --ag-row-hover-color: rgba(79,70,229,0.07) !important;
    --ag-selected-row-background-color: rgba(79,70,229,0.10) !important;
    --ag-border-color: rgba(79,70,229,0.12) !important;
    --ag-row-border-color: rgba(79,70,229,0.06) !important;
    --ag-cell-horizontal-border: solid rgba(79,70,229,0.05) !important;
    --ag-header-column-separator-color: rgba(79,70,229,0.15) !important;
    --ag-font-family: 'Inter', sans-serif !important;
    --ag-font-size: 13px !important;
    --ag-input-focus-border-color: #4F46E5 !important;
    --ag-range-selection-border-color: #4F46E5 !important;
    --ag-modal-overlay-background-color: rgba(238,242,255,0.66) !important;
}

/* AG-Grid element overrides */
[data-testid="stDataFrame"] .ag-root-wrapper,
[data-testid="stDataFrame"] .ag-root,
[data-testid="stDataFrame"] .ag-body-viewport,
[data-testid="stDataFrame"] .ag-center-cols-viewport,
[data-testid="stDataFrame"] .ag-body-container,
[data-testid="stDataFrame"] .ag-full-width-container {
    background-color: #ffffff !important;
    color: #111827 !important;
}

[data-testid="stDataFrame"] .ag-header,
[data-testid="stDataFrame"] .ag-header-row {
    background: linear-gradient(135deg, #EEF2FF, #EDE9FE) !important;
    border-bottom: 1px solid rgba(79,70,229,0.18) !important;
}

[data-testid="stDataFrame"] .ag-header-cell,
[data-testid="stDataFrame"] .ag-header-cell-text,
[data-testid="stDataFrame"] .ag-header-group-cell-label {
    color: #4F46E5 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    background: transparent !important;
}

[data-testid="stDataFrame"] .ag-row {
    background-color: #ffffff !important;
    color: #111827 !important;
    border-bottom: 1px solid rgba(79,70,229,0.05) !important;
}

[data-testid="stDataFrame"] .ag-row-odd {
    background-color: rgba(238,242,255,0.40) !important;
}

[data-testid="stDataFrame"] .ag-row-even {
    background-color: #ffffff !important;
}

[data-testid="stDataFrame"] .ag-row:hover,
[data-testid="stDataFrame"] .ag-row-hover {
    background-color: rgba(79,70,229,0.07) !important;
}

[data-testid="stDataFrame"] .ag-cell,
[data-testid="stDataFrame"] .ag-cell-value {
    color: #111827 !important;
    font-size: 0.83rem !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stDataFrame"] .ag-cell-wrapper,
[data-testid="stDataFrame"] .ag-group-cell-entire-row {
    color: #111827 !important;
}

/* Index column */
[data-testid="stDataFrame"] .ag-pinned-left-cols-container .ag-cell {
    color: #9CA3AF !important;
    font-size: 0.75rem !important;
    background: rgba(79,70,229,0.02) !important;
    border-right: 1px solid rgba(79,70,229,0.08) !important;
}

/* Scrollbar inside dataframe */
[data-testid="stDataFrame"] ::-webkit-scrollbar { width: 6px; height: 6px; }
[data-testid="stDataFrame"] ::-webkit-scrollbar-track { background: #EEF2FF; }
[data-testid="stDataFrame"] ::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #4F46E5, #7C3AED);
    border-radius: 3px;
}

/* ── EXPANDER ── */
[data-testid="stExpander"] {
    background: rgba(255,255,255,0.85) !important;
    border: 1px solid rgba(79,70,229,0.12) !important;
    border-radius: 10px !important;
}
[data-testid="stExpander"] summary { color: #374151 !important; font-weight: 500 !important; }

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.75);
    border-radius: 10px;
    padding: 4px;
    gap: 4px;
    border: 1px solid rgba(79,70,229,0.12);
    backdrop-filter: blur(12px);
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #6B7280 !important;
    border-radius: 8px !important;
    padding: 0.35rem 0.9rem !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    font-family: 'Rajdhani', sans-serif !important;
    letter-spacing: 0.03em !important;
    transition: all 0.2s ease !important;
}
.stTabs [data-baseweb="tab"]:hover {
    background: rgba(79,70,229,0.07) !important;
    color: #4F46E5 !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #4F46E5, #7C3AED) !important;
    color: white !important;
    box-shadow: 0 2px 10px rgba(79,70,229,0.28) !important;
}
.stTabs [aria-selected="true"] p { color: white !important; }

/* ── FILE UPLOADER — full light-theme override ── */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.88) !important;
    border-radius: 14px !important;
}
[data-testid="stFileDropzone"],
[data-testid="stFileUploader"] > div,
[data-testid="stFileUploader"] section {
    background: rgba(255,255,255,0.88) !important;
    border: 2px dashed rgba(79,70,229,0.28) !important;
    border-radius: 14px !important;
    color: #374151 !important;
}
[data-testid="stFileDropzone"] span,
[data-testid="stFileDropzone"] p,
[data-testid="stFileDropzone"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p,
[data-testid="stFileUploader"] small {
    color: #6B7280 !important;
}
[data-testid="stFileDropzone"] button,
[data-testid="stFileUploader"] button {
    background: rgba(79,70,229,0.08) !important;
    color: #4F46E5 !important;
    border: 1px solid rgba(79,70,229,0.28) !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}
[data-testid="stFileDropzone"] button:hover,
[data-testid="stFileUploader"] button:hover {
    background: rgba(79,70,229,0.15) !important;
    border-color: #4F46E5 !important;
}

/* ── HR / DIVIDER ── */
hr {
    border: none !important;
    border-top: 1px solid rgba(79,70,229,0.10) !important;
    margin: 1.5rem 0 !important;
}

/* ── PLOTLY CHART WRAPPER ── */
[data-testid="stPlotlyChart"] > div {
    background: rgba(255,255,255,0.78) !important;
    backdrop-filter: blur(16px) !important;
    border-radius: 18px !important;
    border: 1px solid rgba(255,255,255,0.85) !important;
    box-shadow: 0 4px 24px rgba(79,70,229,0.08), 0 1px 4px rgba(0,0,0,0.03) !important;
    overflow: hidden !important;
    transition: transform 0.25s ease, box-shadow 0.25s ease !important;
}
[data-testid="stPlotlyChart"]:hover > div {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 36px rgba(79,70,229,0.13) !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #EEF2FF; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #4F46E5, #7C3AED);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover { background: #4F46E5; }

/* ── FUTURISTIC HTML TABLE ── */
.ftable-wrap {
    width: 100%;
    overflow-x: auto;
    overflow-y: auto;
    max-height: var(--ftable-height, 420px);
    border-radius: 14px;
    border: 1px solid rgba(79,70,229,0.14);
    background: rgba(255,255,255,0.88);
    backdrop-filter: blur(12px);
    margin-bottom: 1rem;
    box-shadow: 0 4px 20px rgba(79,70,229,0.07);
    scrollbar-width: thin;
    scrollbar-color: #4F46E5 rgba(238,242,255,0.6);
}
.ftable-wrap::-webkit-scrollbar { width: 7px; height: 7px; }
.ftable-wrap::-webkit-scrollbar-track {
    background: rgba(238,242,255,0.6);
    border-radius: 0 14px 14px 0;
}
.ftable-wrap::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg,#4F46E5,#7C3AED);
    border-radius: 99px;
}
.ftable-wrap::-webkit-scrollbar-corner { background: transparent; }

.ftable {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-family: 'Inter', sans-serif;
    font-size: 0.83rem;
    color: #374151;
}

.ftable thead { position: sticky; top: 0; z-index: 3; }
.ftable thead tr {
    background: linear-gradient(135deg,rgba(79,70,229,0.09),rgba(124,58,237,0.06));
}
.ftable thead th {
    color: #4F46E5 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.68rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    text-align: center !important;
    padding: 10px 14px !important;
    border-bottom: 1px solid rgba(79,70,229,0.18) !important;
    border-right: 1px solid rgba(79,70,229,0.06) !important;
    white-space: nowrap !important;
    background: linear-gradient(135deg,rgba(235,238,255,0.98),rgba(237,233,254,0.98)) !important;
    backdrop-filter: blur(8px) !important;
    box-shadow: 0 1px 0 rgba(79,70,229,0.14) !important;
}
.ftable thead th:last-child { border-right: none !important; }
.ftable thead th.ft-idx {
    color: rgba(79,70,229,0.45) !important;
    background: rgba(79,70,229,0.05) !important;
    border-right: 1px solid rgba(79,70,229,0.12) !important;
    min-width: 40px !important;
}
.ftable tbody tr:nth-child(odd)  { background: rgba(255,255,255,0.60); }
.ftable tbody tr:nth-child(even) { background: rgba(238,242,255,0.38); }
.ftable tbody tr:hover { background: rgba(79,70,229,0.06) !important; }
.ftable tbody td {
    text-align: center !important;
    padding: 8px 14px !important;
    border-bottom: 1px solid rgba(79,70,229,0.05) !important;
    border-right: 1px solid rgba(79,70,229,0.04) !important;
    vertical-align: middle !important;
    white-space: nowrap !important;
}
.ftable tbody td:last-child { border-right: none !important; }
.ftable tbody td.ft-idx {
    color: #9CA3AF !important;
    font-size: 0.75rem !important;
    background: rgba(79,70,229,0.02) !important;
    border-right: 1px solid rgba(79,70,229,0.08) !important;
}
.ftable tbody tr:last-child td { border-bottom: none !important; }

/* ── MISC ── */
.block-container { padding-top: 0.8rem !important; }
header[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }
</style>
"""


def apply_futuristic_style():
    st.markdown(_FONT_LINKS, unsafe_allow_html=True)
    st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

inject_css = apply_futuristic_style


def sidebar_brand(title: str = "Telecom", subtitle: str = "Telecom Analysis"):
    st.sidebar.markdown(
        f'<div style="padding:0.5rem 0 1.25rem 0;">'
        f'<div style="font-family:Orbitron,sans-serif;font-size:1rem;font-weight:700;'
        f'background:linear-gradient(135deg,#4F46E5,#7C3AED);'
        f'-webkit-background-clip:text;-webkit-text-fill-color:transparent;'
        f'background-clip:text;">{title}</div>'
        f'<div style="font-family:Rajdhani,sans-serif;font-size:0.72rem;color:#9CA3AF;'
        f'margin-top:3px;letter-spacing:0.1em;text-transform:uppercase;">{subtitle}</div>'
        f'</div>'
        f'<hr style="border:none;border-top:1px solid rgba(79,70,229,0.12);margin:0 0 0.75rem 0;">',
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = "", icon: str = ""):
    label = f"{icon} {title}" if icon else title
    sub_html = (
        f'<p style="color:#6B7280;font-size:0.875rem;margin:0;font-family:Rajdhani,sans-serif;'
        f'letter-spacing:0.04em;">{subtitle}</p>'
        if subtitle else ""
    )
    st.markdown(
        f'<div style="margin-bottom:1.5rem;padding-bottom:1rem;'
        f'border-bottom:1px solid rgba(79,70,229,0.12);">'
        f'<h1 style="margin-bottom:0.2rem!important;'
        f'background:linear-gradient(135deg,#111827,#4F46E5);'
        f'-webkit-background-clip:text;-webkit-text-fill-color:transparent;'
        f'background-clip:text;">{label}</h1>'
        f'{sub_html}'
        f'</div>',
        unsafe_allow_html=True,
    )


def section_header(title: str, subtitle: str = ""):
    st.markdown(f'<div class="nc-section-header">{title}</div>', unsafe_allow_html=True)


def chart_label(title: str, sub: str = ""):
    st.markdown(
        f'<div class="nc-chart-label">{title}</div>'
        + (f'<div class="nc-chart-sub">{sub}</div>' if sub else ""),
        unsafe_allow_html=True,
    )


def kpi_card(col, title: str, value: str, delta: str = "", icon: str = "",
             color: str = "#4F46E5", subtitle: str = ""):
    delta = delta or subtitle
    with col:
        delta_html = f'<div class="nc-kpi-delta">{delta}</div>' if delta else ""
        st.markdown(
            f'<div class="nc-kpi-card" style="border-color:{color};'
            f'box-shadow:0 4px 20px rgba(0,0,0,0.06),0 0 16px {color}18;">'
            f'<div class="nc-kpi-icon">{icon}</div>'
            f'<div class="nc-kpi-label">{title}</div>'
            f'<div class="nc-kpi-value" style="color:{color};">{value}</div>'
            f'{delta_html}'
            f'</div>',
            unsafe_allow_html=True,
        )


def footer():
    st.markdown(
        '<div style="margin-top:3rem;padding-top:1.25rem;'
        'border-top:1px solid rgba(79,70,229,0.10);'
        'display:flex;justify-content:space-between;align-items:center;">'
        '<div style="font-size:0.72rem;color:#9CA3AF;font-family:Rajdhani,sans-serif;'
        'letter-spacing:0.06em;">APL LOGISTICS · SUPPLY CHAIN INTELLIGENCE PLATFORM</div>'
        '<div style="font-size:0.72rem;color:#9CA3AF;font-family:Rajdhani,sans-serif;">© 2024</div>'
        '</div>',
        unsafe_allow_html=True,
    )


def insight_card(text: str, kind: str = "info"):
    palettes = {
        "success": ("#10B981", "rgba(16,185,129,0.07)"),
        "warning": ("#F59E0B", "rgba(245,158,11,0.07)"),
        "error":   ("#EF4444", "rgba(239,68,68,0.07)"),
        "info":    ("#4F46E5", "rgba(79,70,229,0.07)"),
        "purple":  ("#7C3AED", "rgba(124,58,237,0.07)"),
        "cyan":    ("#06B6D4", "rgba(6,182,212,0.07)"),
    }
    bc, bg = palettes.get(kind, palettes["info"])
    st.markdown(
        f'<div class="nc-insight" style="border-color:{bc};background:{bg};">{text}</div>',
        unsafe_allow_html=True,
    )


def insight(text: str, label: str = "Insight", value: str = "", kind: str = "default"):
    kind_map = {
        "positive": "success", "negative": "error",
        "default": "info", "warning": "warning", "purple": "purple",
    }
    full_text = f"<strong>{label}</strong> — {text}"
    if value:
        full_text += f"<br><code style='font-size:0.8rem;'>{value}</code>"
    insight_card(full_text, kind=kind_map.get(kind, "info"))


def plotly_futuristic_layout(title: str = "", height: int = 380) -> dict:
    layout = dict(**PLOT_LAYOUT)
    layout["height"] = height
    if title:
        layout["title"] = dict(
            text=title,
            font=dict(family="Rajdhani, sans-serif", size=15, color="#1E293B"),
            x=0.01, pad=dict(b=8),
        )
    return layout


def apply_plot_layout(fig, height: int = 380):
    fig.update_layout(height=height, **PLOT_LAYOUT)
    return fig


def chart(fig, title: str = "", height: int = 380):
    apply_plot_layout(fig, height)
    if title:
        fig.update_layout(title=dict(
            text=title,
            font=dict(family="Rajdhani, sans-serif", size=15, color="#1E293B"),
            x=0.01,
        ))
    st.plotly_chart(fig, use_container_width=True)


def df_table(df, show_index: bool = True, max_rows=None, height: int = 420):
    if max_rows is not None:
        df = df.head(max_rows)
    if show_index:
        header = '<th class="ft-idx"></th>' + "".join(f"<th>{col}</th>" for col in df.columns)
    else:
        header = "".join(f"<th>{col}</th>" for col in df.columns)
    rows_html = ""
    for idx, row in df.iterrows():
        if show_index:
            cells = f'<td class="ft-idx">{idx}</td>' + "".join(f"<td>{v}</td>" for v in row)
        else:
            cells = "".join(f"<td>{v}</td>" for v in row)
        rows_html += f"<tr>{cells}</tr>"
    st.markdown(
        f'<div class="ftable-wrap" style="--ftable-height:{height}px;">'
        f'<table class="ftable">'
        f'<thead><tr>{header}</tr></thead>'
        f'<tbody>{rows_html}</tbody>'
        f'</table></div>',
        unsafe_allow_html=True,
    )


def show_table(df, height=None, column_config=None):
    kwargs = dict(use_container_width=True)
    if height is not None:
        kwargs["height"] = height
    if column_config is not None:
        kwargs["column_config"] = column_config
    st.dataframe(df, **kwargs)

def executive_insight(
    what="",
    why="",
    impact="",
    recommendation="",
):
    st.markdown(
        f"""
        <div style="
            background: rgba(255,255,255,0.88);
            border: 1px solid rgba(79,70,229,0.12);
            border-radius: 16px;
            padding: 1rem 1.25rem;
            margin-top: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 20px rgba(79,70,229,0.06);
            line-height: 1.8;
            font-size: 0.92rem;
            color: #374151;
        ">

        <div style="margin-bottom:0.4rem;">
        📊 <strong style="color:#111827;">What:</strong>
        {what}
        </div>

        <div style="margin-bottom:0.4rem;">
        🔎 <strong style="color:#111827;">Why:</strong>
        {why}
        </div>

        <div style="margin-bottom:0.4rem;">
        💼 <strong style="color:#111827;">Business Impact:</strong>
        {impact}
        </div>

        <div>
        ✅ <strong style="color:#111827;">Recommendation:</strong>
        {recommendation}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    
