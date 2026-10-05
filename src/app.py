"""
CHRONI-SENSE LABS | SOCKONE STORYTELLING DASHBOARD
Smart Sock Multimodal Chronic Pain & Fatigue Assessment System
Framework: Streamlit + Plotly
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from styles import (
    CUSTOM_CSS, get_plotly_layout,
    PRIMARY_COLOR, ACCENT_COLOR, ALERT_COLOR, WARNING_COLOR, SUCCESS_COLOR
)
from data_loader import load_cohort_data, load_longitudinal_data

# Page Configuration
st.set_page_config(
    page_title="SOCKONE | Chroni-Sense Labs Dashboard",
    page_icon="🧦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Load Datasets
df_cohort = load_cohort_data()
df_longitudinal = load_longitudinal_data()

# ==============================================================================
# SIDEBAR CONTROLS & BRANDING
# ==============================================================================
with st.sidebar:
    st.markdown(
        f"""
        <div style="text-align: center; padding: 1rem 0; border-bottom: 1px solid #E2E8F0;">
            <div style="font-size: 2.5rem; line-height: 1;">🧦</div>
            <h2 style="color: {PRIMARY_COLOR}; margin: 0.4rem 0 0.1rem 0; font-weight: 700; font-size: 1.5rem;">SOCKONE</h2>
            <p style="color: {ACCENT_COLOR}; font-weight: 600; font-size: 0.8rem; letter-spacing: 1px; margin: 0;">CHRONI-SENSE LABS</p>
            <p style="color: #64748B; font-size: 0.75rem; margin-top: 0.2rem;">Chronic Pain & Fatigue Intelligence</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("### 🎛️ Control Panel")
    
    # Diagnosis Filter
    diagnoses = ["All Diagnoses"] + sorted(df_cohort["Diagnosis"].unique().tolist())
    selected_diag = st.selectbox("🏥 Filter by Diagnosis:", diagnoses)
    
    # Alert Status Filter
    alert_filters = ["All Statuses", "Critical", "Warning", "Normal"]
    selected_status = st.selectbox("🚨 Triage Alert Status:", alert_filters)
    
    # Apply Filters to Cohort
    filtered_df = df_cohort.copy()
    if selected_diag != "All Diagnoses":
        filtered_df = filtered_df[filtered_df["Diagnosis"] == selected_diag]
    if selected_status != "All Statuses":
        filtered_df = filtered_df[filtered_df["Alert_Status"] == selected_status]

    st.markdown("---")
    st.markdown("### 📋 Patient Quick Select")
    selected_patient_id = st.selectbox(
        "Select Patient for Deep Dive:",
        options=df_cohort["Patient_ID"].tolist(),
        format_func=lambda x: f"{x} - {df_cohort[df_cohort['Patient_ID'] == x]['Patient_Name'].values[0]} ({df_cohort[df_cohort['Patient_ID'] == x]['Alert_Status'].values[0]})"
    )

    st.markdown("---")
    st.markdown(
        """
        <div style="font-size: 0.76rem; color: #64748B; line-height: 1.4;">
            <b>Course:</b> Business Idea Creation<br>
            <b>Product:</b> SOCKONE Smart Insole/Sock<br>
            <b>Hardware:</b> Optical PPG + 6-Axis IMU + Multi-zone Force Sensors<br>
            <b>Version:</b> 2.4.0 Clinical Release
        </div>
        """,
        unsafe_allow_html=True
    )

# ==============================================================================
# HEADER BANNER
# ==============================================================================
st.markdown(
    f"""
    <div class="brand-header">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
            <div>
                <h1>SOCKONE: Multimodal Pain & Fatigue Tele-Monitoring</h1>
                <p>ระบบถุงเท้าอัจฉริยะประเมินความเจ็บปวดเรื้อรังและความล้าด้วยการผสานข้อมูล HRV และ Dynamic Gait Biomechanics</p>
            </div>
            <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(8px); padding: 0.6rem 1.2rem; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.25); text-align: right;">
                <div style="font-size: 0.75rem; color: #A7F3D0; font-weight: 600; text-transform: uppercase;">System Status</div>
                <div style="font-size: 1.1rem; font-weight: 700; color: #FFFFFF;">● Live Ingest Active</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
# SECTION 1: EXECUTIVE OVERVIEW & REAL-TIME ALERT
# ==============================================================================
st.markdown(
    """
    <div class="story-section">
        <div class="story-section-title">
            <span>📊</span> Section 1: Executive Overview & Real-time Alert
        </div>
        <div class="story-section-subtitle">
            ภาพรวมกลุ่มผู้ป่วยภายใต้การดูแล (Cohort Overview) และระบบคัดกรองความเร่งด่วนอัตโนมัติ (Automated Clinical Triage)
        </div>
    """,
    unsafe_allow_html=True
)

# Key Performance Indicators
c1, c2, c3, c4 = st.columns(4)

total_pts = len(filtered_df)
critical_alerts = len(filtered_df[filtered_df["Alert_Status"] == "Critical"])
warning_alerts = len(filtered_df[filtered_df["Alert_Status"] == "Warning"])
avg_pain = round(filtered_df["Pain_Score_AI"].mean(), 1) if not filtered_df.empty else 0.0
avg_hrv = round(filtered_df["HRV_RMSSD"].mean(), 1) if not filtered_df.empty else 0.0

with c1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Monitored Cohort</div>
            <div class="metric-value">{total_pts} <span style="font-size: 1rem; color: #64748B;">pts</span></div>
            <div class="metric-delta" style="color: {SUCCESS_COLOR};">● 98.4% Telemetry Active</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
        <div class="metric-card" style="border-left: 4px solid {ALERT_COLOR};">
            <div class="metric-title">Critical Flare Alerts</div>
            <div class="metric-value" style="color: {ALERT_COLOR};">{critical_alerts}</div>
            <div class="metric-delta" style="color: {ALERT_COLOR};">▲ Requires Tele-intervention</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Mean Cohort Pain Index</div>
            <div class="metric-value">{avg_pain} <span style="font-size: 1rem; color: #64748B;">/ 10</span></div>
            <div class="metric-delta" style="color: {ACCENT_COLOR};">▼ -1.4 pts vs Baseline</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Mean HRV (RMSSD)</div>
            <div class="metric-value">{avg_hrv} <span style="font-size: 1rem; color: #64748B;">ms</span></div>
            <div class="metric-delta" style="color: {SUCCESS_COLOR};">▲ Normalizing Vagal Tone</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# Triage Distribution & Patient List Table
col_chart, col_table = st.columns([1, 2])

with col_chart:
    st.markdown("##### 🚨 Triage Distribution")
    status_counts = df_cohort["Alert_Status"].value_counts().reset_index()
    status_counts.columns = ["Alert_Status", "Count"]
    
    color_map = {
        "Critical": ALERT_COLOR,
        "Warning": WARNING_COLOR,
        "Normal": SUCCESS_COLOR
    }
    
    fig_donut = px.pie(
        status_counts,
        names="Alert_Status",
        values="Count",
        hole=0.6,
        color="Alert_Status",
        color_discrete_map=color_map
    )
    fig_donut.update_layout(get_plotly_layout("", height=260))
    fig_donut.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_donut, use_container_width=True)

with col_table:
    st.markdown("##### 🩺 Real-Time Patient Triage Roster")
    display_cols = [
        "Patient_ID", "Patient_Name", "Diagnosis", "Pain_Score_AI",
        "HRV_RMSSD", "Gait_Symmetry_Score", "Alert_Status", "Recommended_Action"
    ]
    st.dataframe(
        filtered_df[display_cols].style.map(
            lambda v: 'color: #E63946; font-weight: bold;' if v == 'Critical'
            else ('color: #D97706; font-weight: bold;' if v == 'Warning'
            else ('color: #0F766E;' if v == 'Normal' else '')),
            subset=['Alert_Status']
        ),
        use_container_width=True,
        height=260
    )

st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# SECTION 2: PHYSIOLOGICAL CORRELATION
# ==============================================================================
st.markdown(
    """
    <div class="story-section">
        <div class="story-section-title">
            <span>🔬</span> Section 2: Physiological Correlation
        </div>
        <div class="story-section-subtitle">
            การพิสูจน์ความสัมพันธ์เชิงวิทยาศาสตร์: ปฏิสัมพันธ์ระหว่าง HRV Vagal Suppression และ Gait Biomechanics ต่อระดับความเจ็บปวด
        </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="clinical-callout">
        💡 <b>The Clinical Story behind SOCKONE:</b> 
        ความเจ็บปวดเรื้อรังทำให้ระบบประสาทอัตโนมัติเข้าสู่ภาวะ <i>Sympathetic Overdrive</i> ส่งผลให้ค่า <b>HRV (RMSSD) ดิ่งลงต่ำกว่า 20 ms</b> 
        ในขณะเดียวกัน ผู้ป่วยจะเกิดพฤติกรรมหลีกเลี่ยงความเจ็บปวด (Antalgic Guarding) ทำให้ <b>Gait Symmetry ลดลงต่ำกว่า 70%</b> 
        และการลงน้ำหนักเท้าซ้าย-ขวาเกิดความเหลื่อมล้ำ (Pressure Asymmetry > 20%) การตรวจจับ 2 แกนร่วมกันช่วยให้ AI ประเมินความเจ็บปวดได้แม่นยำ 94.2% โดยไม่ต้องพึ่งพาความรู้สึกส่วนตัวเพียงอย่างเดียว
    </div>
    """,
    unsafe_allow_html=True
)

col_corr1, col_corr2 = st.columns([3, 2])

with col_corr1:
    fig_scatter = px.scatter(
        df_cohort,
        x="HRV_RMSSD",
        y="Pain_Score_AI",
        size="Pressure_Asymmetry_Pct",
        color="Alert_Status",
        color_discrete_map={"Critical": ALERT_COLOR, "Warning": WARNING_COLOR, "Normal": SUCCESS_COLOR},
        hover_name="Patient_Name",
        hover_data=["Patient_ID", "Diagnosis", "Gait_Symmetry_Score", "Cadence_SPM"],
        labels={
            "HRV_RMSSD": "Heart Rate Variability RMSSD (ms) - Vagal Tone",
            "Pain_Score_AI": "AI Estimated Pain Score (0 - 10)",
            "Pressure_Asymmetry_Pct": "Pressure Asymmetry (%)"
        },
        title="Multimodal Cluster: HRV Suppression vs AI Pain Score"
    )
    fig_scatter.add_vline(x=20, line_dash="dash", line_color=ALERT_COLOR, annotation_text="Sympathetic Crisis (<20ms)", annotation_position="top right")
    fig_scatter.add_hline(y=7.0, line_dash="dash", line_color=ALERT_COLOR, annotation_text="Severe Pain Threshold (≥7.0)", annotation_position="bottom right")
    fig_scatter.update_layout(get_plotly_layout("Autonomic Stress (HRV) vs Objective Pain Severity", height=380))
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_corr2:
    # Biomechanical Comparison: Critical vs Normal Patient
    crit_sample = df_cohort[df_cohort["Alert_Status"] == "Critical"].iloc[0]
    norm_sample = df_cohort[df_cohort["Alert_Status"] == "Normal"].iloc[0]
    
    categories = ['HRV Norm (ms)', 'Gait Symmetry (%)', 'Cadence (spm)', 'Foot Balance (%)', 'Stride Stability']
    
    val_crit = [
        min(100, crit_sample["HRV_RMSSD"] * 1.5),
        crit_sample["Gait_Symmetry_Score"],
        (crit_sample["Cadence_SPM"] / 120) * 100,
        max(10, 100 - (crit_sample["Pressure_Asymmetry_Pct"] * 2.5)),
        max(10, 100 - (crit_sample["Stride_Time_Variability_Pct"] * 10))
    ]
    val_norm = [
        min(100, norm_sample["HRV_RMSSD"] * 1.5),
        norm_sample["Gait_Symmetry_Score"],
        (norm_sample["Cadence_SPM"] / 120) * 100,
        max(10, 100 - (norm_sample["Pressure_Asymmetry_Pct"] * 2.5)),
        max(10, 100 - (norm_sample["Stride_Time_Variability_Pct"] * 10))
    ]
    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=val_crit,
        theta=categories,
        fill='toself',
        name=f"Flare Alert ({crit_sample['Patient_ID']})",
        line=dict(color=ALERT_COLOR, width=2),
        fillcolor='rgba(230, 57, 70, 0.25)'
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=val_norm,
        theta=categories,
        fill='toself',
        name=f"Controlled ({norm_sample['Patient_ID']})",
        line=dict(color=ACCENT_COLOR, width=2),
        fillcolor='rgba(0, 168, 150, 0.25)'
    ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color="#94A3B8"),
            bgcolor="#FFFFFF"
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=40, r=40, t=45, b=25),
        height=380,
        legend=dict(orientation="h", y=-0.15, x=0.5, xanchor="center")
    )
    st.plotly_chart(fig_radar, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# SECTION 3: RECOVERY & TREND ANALYSIS
# ==============================================================================
st.markdown(
    """
    <div class="story-section">
        <div class="story-section-title">
            <span>📈</span> Section 3: Recovery & Trend Analysis
        </div>
        <div class="story-section-subtitle">
            การติดตามผลการฟื้นฟูระยะยาว (Longitudinal Recovery Trajectory) และผลกระทบต่อการลดภาระค่าใช้จ่ายโรงพยาบาล
        </div>
    """,
    unsafe_allow_html=True
)

# Patient Longitudinal Trajectory
patient_long = df_longitudinal[df_longitudinal["Patient_ID"] == selected_patient_id]
patient_meta = df_cohort[df_cohort["Patient_ID"] == selected_patient_id].iloc[0]

st.markdown(f"##### 👤 Longitudinal 30-Day Recovery Journey: **{patient_meta['Patient_Name']}** ({selected_patient_id}) - *{patient_meta['Diagnosis']}*")

col_trend1, col_trend2 = st.columns([3, 2])

with col_trend1:
    fig_long = go.Figure()
    
    # Pain Score AI line
    fig_long.add_trace(go.Scatter(
        x=patient_long["Date"],
        y=patient_long["Pain_Score_AI"],
        name="AI Pain Score (0-10)",
        mode="lines+markers",
        line=dict(color=ALERT_COLOR, width=3),
        yaxis="y1"
    ))
    
    # HRV RMSSD line
    fig_long.add_trace(go.Scatter(
        x=patient_long["Date"],
        y=patient_long["HRV_RMSSD"],
        name="HRV RMSSD (ms)",
        mode="lines+markers",
        line=dict(color=ACCENT_COLOR, width=2.5, dash="dot"),
        yaxis="y2"
    ))
    
    # Gait Symmetry line
    fig_long.add_trace(go.Scatter(
        x=patient_long["Date"],
        y=patient_long["Gait_Symmetry_Score"],
        name="Gait Symmetry (%)",
        mode="lines",
        line=dict(color=PRIMARY_COLOR, width=2),
        yaxis="y2"
    ))
    
    # Clinical Milestone Annotation at Day 12
    fig_long.add_vline(
        x=patient_long.iloc[11]["Date"],
        line_width=2,
        line_dash="dash",
        line_color="#2563EB",
        annotation_text="Clinical Intervention (Day 12):<br>Offload Insole & Med Titration",
        annotation_position="top left"
    )
    
    fig_long.update_layout(
        title="<b>Multimodal Recovery Trajectory (30-Day Tracking)</b>",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#FFFFFF",
        font=dict(family="Poppins, Noto Sans Thai", color=PRIMARY_COLOR),
        margin=dict(l=40, r=40, t=50, b=40),
        height=380,
        legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center"),
        xaxis=dict(gridcolor="#F1F5F9", tickangle=-30),
        yaxis=dict(
            title=dict(text="Pain Score (0-10)", font=dict(color=ALERT_COLOR)),
            range=[0, 10],
            gridcolor="#F1F5F9"
        ),
        yaxis2=dict(
            title=dict(text="HRV (ms) / Gait Symmetry (%)", font=dict(color=ACCENT_COLOR)),
            overlaying="y",
            side="right",
            range=[0, 110],
            showgrid=False
        )
    )
    st.plotly_chart(fig_long, use_container_width=True)

with col_trend2:
    # Healthcare Economic Impact & Hospital Burden Reduction
    st.markdown("##### 🏥 Hospital Burden & ER Reduction Impact")
    
    impact_data = pd.DataFrame({
        "Metric": ["Unscheduled ER Visits", "Unplanned Outpatient Visits", "Acute Readmissions", "Physical Therapy Dropout"],
        "Conventional_Care": [100, 100, 100, 100],
        "SOCKONE_Enabled": [32, 48, 56, 21]
    })
    
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(
        name="Standard Episodic Care",
        x=impact_data["Metric"],
        y=impact_data["Conventional_Care"],
        marker_color="#94A3B8"
    ))
    fig_bar.add_trace(go.Bar(
        name="SOCKONE Continuous Monitoring",
        x=impact_data["Metric"],
        y=impact_data["SOCKONE_Enabled"],
        marker_color=ACCENT_COLOR
    ))
    
    fig_bar.update_layout(
        barmode='group',
        title="<b>Relative Utilization Index (% of Baseline)</b>",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#FFFFFF",
        font=dict(family="Poppins, Noto Sans Thai", color=PRIMARY_COLOR),
        margin=dict(l=35, r=20, t=50, b=60),
        height=380,
        xaxis=dict(tickangle=-20),
        yaxis=dict(title="Relative Burden (%)", range=[0, 115], gridcolor="#F1F5F9"),
        legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center")
    )
    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# SECTION 4: CLINICAL & BUSINESS ACTIONABLE INSIGHTS
# ==============================================================================
st.markdown(
    """
    <div class="story-section">
        <div class="story-section-title">
            <span>🎯</span> Section 4: Clinical & Business Actionable Insights
        </div>
        <div class="story-section-subtitle">
            ข้อเสนอแนะเชิงคลินิกเฉพาะบุคคล (Prescriptive Decision Support) และคุณค่าทางธุรกิจต่อระบบสาธารณสุข
        </div>
    """,
    unsafe_allow_html=True
)

tab_clinical, tab_business = st.tabs(["🩺 Clinical Decision Support (CDSS)", "💼 Business & Health Economics ROI"])

with tab_clinical:
    col_pinfo, col_recom = st.columns([1, 2])
    
    with col_pinfo:
        st.markdown(
            f"""
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.4rem; border-radius: 12px;">
                <h4 style="color: {PRIMARY_COLOR}; margin-top: 0;">Patient Dossier</h4>
                <p style="margin: 0.3rem 0;"><b>Patient ID:</b> {patient_meta['Patient_ID']}</p>
                <p style="margin: 0.3rem 0;"><b>Name:</b> {patient_meta['Patient_Name']}</p>
                <p style="margin: 0.3rem 0;"><b>Age/Gender:</b> {patient_meta['Age']} yrs / {patient_meta['Gender']}</p>
                <p style="margin: 0.3rem 0;"><b>Diagnosis:</b> {patient_meta['Diagnosis']}</p>
                <p style="margin: 0.3rem 0;"><b>Status:</b> 
                    <span class="badge-tag {'badge-critical' if patient_meta['Alert_Status']=='Critical' else ('badge-warning' if patient_meta['Alert_Status']=='Warning' else 'badge-normal')}">
                        {patient_meta['Alert_Status']}
                    </span>
                </p>
                <hr style="margin: 0.8rem 0; border: 0; border-top: 1px solid #E2E8F0;">
                <p style="margin: 0.3rem 0;"><b>Daily Steps:</b> {patient_meta['Daily_Step_Count']:,}</p>
                <p style="margin: 0.3rem 0;"><b>Heel Pressure:</b> {patient_meta['Peak_Heel_Pressure_kPa']} kPa</p>
                <p style="margin: 0.3rem 0;"><b>Forefoot Pressure:</b> {patient_meta['Peak_Forefoot_Pressure_kPa']} kPa</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col_recom:
        st.markdown("##### 🤖 ChroniSense AI Clinical Directives")
        
        if patient_meta["Alert_Status"] == "Critical":
            st.error(f"""
            **URGENT CLINICAL ALERT:** ผู้ป่วยเกิดภาวะ Acute Flare-up รุนแรง
            - **สัญญาณบ่งชี้:** ค่า HRV RMSSD ดิ่งลงสู่ {patient_meta['HRV_RMSSD']} ms พร้อมอาการลงน้ำหนักไม่สมดุล (Pressure Discrepancy {patient_meta['Pressure_Asymmetry_Pct']}%)
            - **คำสั่งทางการแพทย์ที่แนะนำ:**
              1. นัดหมาย Tele-consultation ด่วนภายใน 2-4 ชั่วโมง
              2. สั่งปรับลดน้ำหนักลงเท้า (Weight-bearing Offloading) ด้วย Smart Insoles Re-calibration
              3. พิจารณาปรับขนาดยาแก้ปวดกลุ่ม Neuropathic / Anti-inflammatory
            """)
        elif patient_meta["Alert_Status"] == "Warning":
            st.warning(f"""
            **SUB-ACUTE MONITORING:** ผู้ป่วยมีแนวโน้มความล้าและความเจ็บปวดระดับปานกลาง
            - **สัญญาณบ่งชี้:** ความเจ็บปวดอยู่ที่ {patient_meta['Pain_Score_AI']}/10 และ Cadence ลดลงเหลือ {patient_meta['Cadence_SPM']} steps/min
            - **คำสั่งทางการแพทย์ที่แนะนำ:**
              1. แนะนำโปรแกรม Active Pacing (พักระหว่างวันทุก 45 นาที)
              2. นัดติดตามผลอาการผ่าน Chatbot พรุ่งนี้เวลา 10:00 น.
            """)
        else:
            st.success(f"""
            **STABLE REHABILITATION:** ผู้ป่วยอยู่ในเกณฑ์ฟื้นตัวดีเยี่ยม
            - **สัญญาณบ่งชี้:** Gait Symmetry สูงถึง {patient_meta['Gait_Symmetry_Score']}% และ HRV อยู่ในเกณฑ์ผ่อนคลาย ({patient_meta['HRV_RMSSD']} ms)
            - **คำแนะนำ:** รักษาตารางกายภาพบำบัดต่อเนื่อง ปรับเพิ่มเป้าหมายก้าวเดิน +500 ก้าว/วัน
            """)

with tab_business:
    b1, b2, b3 = st.columns(3)
    with b1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Cost per Monitored Patient / Mo</div>
                <div class="metric-value">฿1,850</div>
                <div class="metric-delta" style="color: {ACCENT_COLOR};">Hardware Rental + AI SaaS</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with b2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Acute Hospitalization Averted</div>
                <div class="metric-value" style="color: {SUCCESS_COLOR};">฿24,600</div>
                <div class="metric-delta" style="color: {SUCCESS_COLOR};">▼ Direct Savings per Patient/Quarter</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with b3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">ROI for Hospital / Payers</div>
                <div class="metric-value">4.4x</div>
                <div class="metric-delta" style="color: {SUCCESS_COLOR};">▲ Net Economic Value</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        ##### 💡 Health Economics & Commercialization Model
        1. **B2B Remote Patient Monitoring (RPM):** โรงพยาบาลและศูนย์เวชศาสตร์ฟื้นฟูเป็นผู้สั่งจ่าย (Prescribe) ถุงเท้า SOCKONE ให้ผู้ป่วยสวมใส่ที่บ้าน สามารถเบิกจ่ายตามสิทธิประกันสุขภาพหรือ CPT Reimbursement Codes สำหรับ Continuous Physiological Telemetry
        2. **Value-Based Care Alignment:** ลดอัตราการ Re-admission ภายใน 30 วันลงกว่า 44% ช่วยให้โรงพยาบาลประหยัดต้นทุนในระบบ DRG (Diagnosis-Related Group) Capitation
        3. **MedTech Recurring SaaS:** รายได้ประจำจากการสมัครสมาชิกซอฟต์แวร์วิเคราะห์ข้อมูล AI สำหรับคลินิกเฉพาะทางและบริษัทยาวิจัย
        """
    )

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div style="text-align: center; color: #94A3B8; font-size: 0.8rem; margin: 2rem 0 1rem 0;">
        CHRONI-SENSE LABS © 2026 | Project SOCKONE | Business Idea Creation Project Submission
    </div>
    """,
    unsafe_allow_html=True
)
