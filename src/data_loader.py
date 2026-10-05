"""
CHRONI-SENSE LABS - SOCKONE
Data Loader & Mock Dataset Generator for Storytelling Dashboard
"""

import os
import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
CSV_PATH = os.path.join(DATA_DIR, "sockone_mock_dataset.csv")
LONGITUDINAL_CSV_PATH = os.path.join(DATA_DIR, "sockone_longitudinal_dataset.csv")

def generate_mock_datasets():
    """Generates realistic cohort and longitudinal patient data for SOCKONE."""
    os.makedirs(DATA_DIR, exist_ok=True)
    np.random.seed(42)

    patients = [
        {"id": "PT-1001", "name": "Somchai P.", "age": 58, "gender": "Male", "diagnosis": "Diabetic Peripheral Neuropathy"},
        {"id": "PT-1002", "name": "Kanya R.", "age": 46, "gender": "Female", "diagnosis": "Fibromyalgia Syndrome"},
        {"id": "PT-1003", "name": "Vichai T.", "age": 67, "gender": "Male", "diagnosis": "Post-Op Knee Arthroplasty"},
        {"id": "PT-1004", "name": "Apinya S.", "age": 52, "gender": "Female", "diagnosis": "Lumbar Radiculopathy"},
        {"id": "PT-1005", "name": "Prasert M.", "age": 71, "gender": "Male", "diagnosis": "Osteoarthritis Knee"},
        {"id": "PT-1006", "name": "Malai K.", "age": 63, "gender": "Female", "diagnosis": "Diabetic Peripheral Neuropathy"},
        {"id": "PT-1007", "name": "Anan W.", "age": 39, "gender": "Male", "diagnosis": "Post-Op Knee Arthroplasty"},
        {"id": "PT-1008", "name": "Narumol B.", "age": 49, "gender": "Female", "diagnosis": "Fibromyalgia Syndrome"},
        {"id": "PT-1009", "name": "Chaiwat C.", "age": 62, "gender": "Male", "diagnosis": "Lumbar Radiculopathy"},
        {"id": "PT-1010", "name": "Supaporn D.", "age": 55, "gender": "Female", "diagnosis": "Osteoarthritis Knee"},
        {"id": "PT-1011", "name": "Kittisak L.", "age": 69, "gender": "Male", "diagnosis": "Diabetic Peripheral Neuropathy"},
        {"id": "PT-1012", "name": "Ratana J.", "age": 43, "gender": "Female", "diagnosis": "Fibromyalgia Syndrome"}
    ]

    records = []
    base_time = datetime(2026, 10, 4, 14, 30, 0)

    for i, p in enumerate(patients):
        # Determine health condition archetype
        if i in [0, 2, 7]:  # High risk / acute flare-up
            pain_score = round(float(np.random.uniform(7.2, 9.1)), 1)
            hrv_rmssd = round(float(np.random.uniform(11.5, 19.8)), 1)  # Low HRV (Sympathetic overdrive)
            gait_sym = round(float(np.random.uniform(55.0, 68.5)), 1)   # Severe asymmetry
            press_asym = round(float(np.random.uniform(24.0, 36.5)), 1) # Antalgic offloading
            cadence = round(float(np.random.uniform(62.0, 78.0)), 1)
            fatigue = "Severe" if pain_score > 8.0 else "High"
            alert = "Critical"
            action = "Immediate Tele-consult & Offloading Protocol"
        elif i in [3, 5, 8, 10]:  # Moderate / early warning
            pain_score = round(float(np.random.uniform(4.5, 6.8)), 1)
            hrv_rmssd = round(float(np.random.uniform(22.0, 34.0)), 1)
            gait_sym = round(float(np.random.uniform(72.0, 83.0)), 1)
            press_asym = round(float(np.random.uniform(14.0, 21.0)), 1)
            cadence = round(float(np.random.uniform(82.0, 96.0)), 1)
            fatigue = "Moderate"
            alert = "Warning"
            action = "Titrate Analgesics & Active Pacing Advice"
        else:  # Stable / controlled
            pain_score = round(float(np.random.uniform(1.2, 3.8)), 1)
            hrv_rmssd = round(float(np.random.uniform(42.0, 68.0)), 1)  # Healthy vagal tone
            gait_sym = round(float(np.random.uniform(88.0, 96.5)), 1)   # Balanced gait
            press_asym = round(float(np.random.uniform(3.0, 9.5)), 1)
            cadence = round(float(np.random.uniform(102.0, 118.0)), 1)
            fatigue = "Low"
            alert = "Normal"
            action = "Continue Routine Rehabilitation Plan"

        heart_rate = round(float(np.random.uniform(68, 92) + (pain_score * 2.5)), 1)
        heel_press = round(float(np.random.uniform(180, 320)), 1)
        forefoot_press = round(float(np.random.uniform(140, 280)), 1)
        stride_var = round(float(np.random.uniform(1.8, 8.5)), 2)
        step_count = int(np.random.uniform(2400, 8500))
        rec_time = (base_time - timedelta(minutes=int(np.random.uniform(2, 45)))).strftime("%Y-%m-%d %H:%M:%S")

        records.append({
            "Patient_ID": p["id"],
            "Patient_Name": p["name"],
            "Age": p["age"],
            "Gender": p["gender"],
            "Diagnosis": p["diagnosis"],
            "Timestamp": rec_time,
            "Heart_Rate_BPM": heart_rate,
            "HRV_RMSSD": hrv_rmssd,
            "Gait_Symmetry_Score": gait_sym,
            "Pressure_Asymmetry_Pct": press_asym,
            "Cadence_SPM": cadence,
            "Stride_Time_Variability_Pct": stride_var,
            "Peak_Heel_Pressure_kPa": heel_press,
            "Peak_Forefoot_Pressure_kPa": forefoot_press,
            "Daily_Step_Count": step_count,
            "Fatigue_Level": fatigue,
            "Pain_Score_AI": pain_score,
            "Alert_Status": alert,
            "Recommended_Action": action
        })

    df_cohort = pd.DataFrame(records)
    df_cohort.to_csv(CSV_PATH, index=False)

    # Generate 30-day longitudinal trend data for key patients to demonstrate recovery & intervention
    longitudinal_records = []
    start_date = datetime(2026, 9, 5)

    for p in patients:
        # Base recovery trajectory
        for day in range(30):
            current_date = start_date + timedelta(days=day)
            
            # Simulate treatment milestone at Day 12 (Medication titration + smart insole alignment)
            progress_factor = day / 30.0
            flare = np.random.normal(0, 0.4)
            if day == 8:
                flare += 1.8  # Acute flare-up before intervention
            elif day >= 12:
                flare -= (day - 12) * 0.12  # Post-intervention improvement

            if p["id"] == "PT-1003":  # Post-Op Arthroplasty (rehab arc)
                base_pain = max(1.5, 8.2 - (progress_factor * 5.0) + flare)
                base_rmssd = min(62.0, 16.0 + (progress_factor * 35.0) - (flare * 3.5))
                base_sym = min(95.0, 56.0 + (progress_factor * 34.0) - (flare * 4.0))
            elif p["id"] == "PT-1001":  # DPN Chronic management
                base_pain = max(3.0, 7.8 - (progress_factor * 3.2) + flare)
                base_rmssd = min(48.0, 18.0 + (progress_factor * 22.0) - (flare * 2.5))
                base_sym = min(90.0, 62.0 + (progress_factor * 24.0) - (flare * 3.0))
            else:
                base_pain = max(1.0, 5.5 - (progress_factor * 2.5) + flare)
                base_rmssd = min(58.0, 30.0 + (progress_factor * 20.0) - (flare * 2.0))
                base_sym = min(94.0, 75.0 + (progress_factor * 18.0) - (flare * 2.0))

            longitudinal_records.append({
                "Date": current_date.strftime("%Y-%m-%d"),
                "Day": day + 1,
                "Patient_ID": p["id"],
                "Diagnosis": p["diagnosis"],
                "Pain_Score_AI": round(float(base_pain), 1),
                "HRV_RMSSD": round(float(base_rmssd), 1),
                "Gait_Symmetry_Score": round(float(base_sym), 1),
                "Daily_Steps": int(3000 + (progress_factor * 3800) + np.random.randint(-300, 300)),
                "Intervention_Active": "Yes" if day >= 12 else "Baseline/Pre-intervention"
            })

    df_longitudinal = pd.DataFrame(longitudinal_records)
    df_longitudinal.to_csv(LONGITUDINAL_CSV_PATH, index=False)
    print(f"Mock datasets created: {CSV_PATH} and {LONGITUDINAL_CSV_PATH}")

def load_cohort_data():
    """Loads cohort snapshot dataset."""
    if not os.path.exists(CSV_PATH):
        generate_mock_datasets()
    return pd.read_csv(CSV_PATH)

def load_longitudinal_data():
    """Loads 30-day longitudinal trend dataset."""
    if not os.path.exists(LONGITUDINAL_CSV_PATH):
        generate_mock_datasets()
    return pd.read_csv(LONGITUDINAL_CSV_PATH)

if __name__ == "__main__":
    generate_mock_datasets()
