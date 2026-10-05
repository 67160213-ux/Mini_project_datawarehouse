"""
CHRONI-SENSE LABS - SOCKONE
Styling, Brand Palette & Plotly Theme Definitions
"""

PRIMARY_COLOR = "#0F172A"      # Deep Navy
ACCENT_COLOR = "#00A896"       # Medical Cyan
ALERT_COLOR = "#E63946"        # Pulse Coral
WARNING_COLOR = "#F4A261"      # Amber Warning
SUCCESS_COLOR = "#2A9D8F"      # Emerald Clinical Success
BG_COLOR = "#F8FAF8"           # Clinical Clean
CARD_BG = "#FFFFFF"            # Pure White Card
TEXT_MUTED = "#64748B"         # Slate Gray Muted
BORDER_COLOR = "#E2E8F0"       # Subtle Slate Border

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', 'Noto Sans Thai', sans-serif !important;
    color: #0F172A;
    background-color: #F8FAF8;
}

/* Header Banner */
.brand-header {
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 70%, #00A896 100%);
    padding: 1.8rem 2.2rem;
    border-radius: 16px;
    color: #FFFFFF;
    margin-bottom: 1.8rem;
    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.2);
    border-left: 6px solid #00A896;
}

.brand-header h1 {
    font-size: 2.1rem;
    font-weight: 700;
    margin: 0;
    letter-spacing: -0.5px;
    color: #FFFFFF !important;
}

.brand-header p {
    font-size: 0.95rem;
    color: #CBD5E1;
    margin-top: 0.4rem;
    margin-bottom: 0;
}

/* Metric Cards */
.metric-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0, 168, 150, 0.12);
}

.metric-title {
    font-size: 0.82rem;
    font-weight: 600;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.3rem;
}

.metric-value {
    font-size: 1.9rem;
    font-weight: 700;
    color: #0F172A;
    line-height: 1.1;
}

.metric-delta {
    font-size: 0.78rem;
    font-weight: 500;
    margin-top: 0.35rem;
}

/* Section Containers */
.story-section {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 1.8rem;
    margin-bottom: 2rem;
    box-shadow: 0 4px 15px rgba(15, 23, 42, 0.03);
}

.story-section-title {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-size: 1.35rem;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 0.3rem;
}

.story-section-subtitle {
    font-size: 0.9rem;
    color: #64748B;
    margin-bottom: 1.2rem;
}

.badge-tag {
    display: inline-block;
    padding: 0.2rem 0.65rem;
    font-size: 0.72rem;
    font-weight: 600;
    border-radius: 20px;
}

.badge-critical {
    background-color: #FEE2E2;
    color: #E63946;
    border: 1px solid #FECACA;
}

.badge-warning {
    background-color: #FEF3C7;
    color: #D97706;
    border: 1px solid #FDE68A;
}

.badge-normal {
    background-color: #CCFBF1;
    color: #0F766E;
    border: 1px solid #99F6E4;
}

/* Callout Box */
.clinical-callout {
    background: #F0FDFA;
    border-left: 4px solid #00A896;
    padding: 1rem 1.2rem;
    border-radius: 0 10px 10px 0;
    margin: 1rem 0;
    font-size: 0.88rem;
    color: #134E4A;
}
</style>
"""

def get_plotly_layout(title="", height=380):
    """Standardizes Plotly chart aesthetics to match SOCKONE design identity."""
    return dict(
        title=dict(
            text=f"<b>{title}</b>",
            font=dict(family="Poppins, Noto Sans Thai", size=15, color=PRIMARY_COLOR),
            x=0.02,
            y=0.96
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#FFFFFF",
        font=dict(family="Poppins, Noto Sans Thai", color=PRIMARY_COLOR, size=12),
        margin=dict(l=45, r=30, t=55, b=45),
        height=height,
        hoverlabel=dict(
            bgcolor=PRIMARY_COLOR,
            font_size=12,
            font_family="Poppins, Noto Sans Thai"
        ),
        xaxis=dict(
            gridcolor="#F1F5F9",
            zerolinecolor="#E2E8F0",
            linecolor="#CBD5E1",
            tickfont=dict(color="#64748B")
        ),
        yaxis=dict(
            gridcolor="#F1F5F9",
            zerolinecolor="#E2E8F0",
            linecolor="#CBD5E1",
            tickfont=dict(color="#64748B")
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=11)
        )
    )
