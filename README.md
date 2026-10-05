# 🧦 SOCKONE: Smart Chronic Pain & Fatigue Assessment System
### Multimodal Telemetric Insole & Sensory Sock Platform for Remote Patient Monitoring
**CHRONI-SENSE LABS** | *Business Idea Creation Project*

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.20%2B-00A896.svg)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-0F172A.svg)](LICENSE)
[![Status](https://img.shields.io/badge/System_Status-Clinical_Demo_Ready-2A9D8F.svg)]()

---

## 📌 1. โครงการและแนวคิดธุรกิจ (Executive Summary & Problem Statement)

อาการปวดเรื้อรัง (Chronic Pain) และความเหนื่อยล้าทางสรีรวิทยา (Neuromuscular Fatigue) ในกลุ่มผู้ป่วยโรคเบาหวาน (Diabetic Peripheral Neuropathy), โรคปวดกล้ามเนื้อเรื้อรัง (Fibromyalgia), และผู้ป่วยหลังผ่าตัดกระดูกและข้อ (Post-Operative Arthroplasty) มักถูกประเมินผ่าน **แบบสอบถามส่วนตัว (Subjective VAS/NRS Questionnaires)** ซึ่งมักขาดความแม่นยำและไม่สามารถตรวจจับความเจ็บปวดที่เกิดขึ้นระหว่างใช้ชีวิตประจำวันได้แบบ Real-time

**SOCKONE โดย CHRONI-SENSE LABS** จึงถือกำเนิดขึ้นเพื่อแก้ปัญหานี้ โดยเป็น **ถุงเท้าและแผ่นรองพื้นอัจฉริยะ (Smart Sensor-embedded Sock & Insole)** ที่ทำการประเมินความเจ็บปวดและระดับความล้าของผู้ป่วยอย่างเป็นรูปธรรม (Objective Biomarkers) ผ่านการผสานสัญญาณชีวภาพ (HRV) ร่วมกับจลนศาสตร์การเดิน (Gait Dynamics) เพื่อส่งสัญญาณเตือนก่อนเกิดภาวะวิกฤต (Pain Flare-up) และลดอัตราการเข้าห้องฉุกเฉินหรือการกลับมานอนโรงพยาบาลซ้ำ

---

## 🏗️ 2. สถาปัตยกรรมการตรวจวัด (Multimodal Sensor Architecture)

SOCKONE ฝังเซนเซอร์ตรวจวัดทางการแพทย์ 3 ระบบลงในเนื้อผ้าสัมผัสนุ่มและแผ่นรองฝ่าเท้า:

```
+-----------------------------------------------------------------------------------+
|                            SOCKONE SENSORY HARDWARE                               |
|                                                                                   |
|  [Medial Malleolus]                   [Insole Matrix]        [Ankle Collar]       |
|  +--------------------+               +------------------+   +------------------+ |
|  | Optical PPG Sensor |               | Multi-Zone Force |   |   6-Axis IMU     | |
|  | - Heart Rate (BPM) |               | - Heel Load      |   | - 3D Accel       | |
|  | - HRV (RMSSD)      |               | - Midfoot/Arch   |   | - 3D Gyroscope   | |
|  |                    |               | - Forefoot/Toes  |   | - Cadence & Sym  | |
|  +---------+----------+               +--------+---------+   +--------+---------+ |
+------------|-----------------------------------|----------------------|-----------+
             |                                   |                      |
             +--------------------> [ Edge-AI Hub ] <-------------------+
                                        | (Bluetooth Low Energy 5.3)
                                        v
                     +--------------------------------------+
                     |  CHRONI-SENSE Clinical Cloud Core    |
                     |  - Predictive Pain Score (0-10)      |
                     |  - Neuromuscular Fatigue Index       |
                     |  - Triage & Flare Alerting Engine    |
                     +--------------------------------------+
                                        |
                                        v
                     [ Storytelling Clinical Dashboard (Streamlit) ]
```

1. **Optical Photoplethysmography (PPG) at Ankle:** ตรวจวัดความแปรปรวนของการเต้นของหัวใจ (Heart Rate Variability: HRV - RMSSD) เพื่อตรวจจับการกระตุ้นของระบบประสาท Sympathetic เมื่อเกิดความปวดเฉียบพลัน
2. **Multi-Zone Plantar Pressure Matrix:** เซนเซอร์วัดแรงกดฝ่าเท้า 4 จุดหลัก (ส้นเท้า, กลางเท้า, ฝ่าเท้าส่วนหน้า, นิ้วหัวแม่เท้า) ตรวจวัดน้ำหนักและการชดเชยการลงน้ำหนัก (Antalgic Offloading)
3. **6-Axis Inertial Measurement Unit (IMU):** ตรวจวัดความถี่ก้าวเดิน (Cadence), ความสมมาตรในการก้าว (Gait Symmetry Score %), และความแปรปรวนของรอบก้าว (Stride Time Variability)

---

## 📂 3. โครงสร้างการจัดเก็บไฟล์ใน Repository (GitHub Directory Tree)

```text
Mini_project_datawarehouse/
├── .streamlit/
│   └── config.toml                  # การกำหนด Theme สี Brand Identity และ Font
├── assets/
│   ├── logo_chronisense.svg         # ตราสัญลักษณ์ CHRONI-SENSE LABS
│   └── banner_preview.png           # ภาพประกอบ Mockup Dashboard
├── data/
│   ├── sockone_schema.json          # มาตรฐาน Schema ข้อมูลเซนเซอร์ (JSON Schema)
│   ├── sockone_mock_dataset.csv     # ข้อมูลจำลองผู้ป่วยรายบุคคล (Cohort Snapshot)
│   └── sockone_longitudinal_dataset.csv # ข้อมูลจำลองการติดตามผลการรักษา 30 วัน
├── docs/
│   ├── data_dictionary.md           # พจนานุกรมข้อมูล (Clinical Data Dictionary)
│   ├── storytelling_architecture.md # ผังโครงสร้างการเล่าเรื่อง (Narrative Arc Plan)
│   └── presentation_slides.md       # สคริปต์สไลด์นำเสนอ (Slide-by-slide script)
├── presentation/
│   └── index.html                   # สไลด์นำเสนอ Interactive Slide Deck (เปิดใน Browser ได้ทันที)
├── src/
│   ├── __init__.py
│   ├── app.py                       # แอปพลิเคชัน Streamlit Dashboard หลัก
│   ├── data_loader.py               # โมดูลสร้างและโหลดข้อมูลผู้ป่วยจำลอง
│   └── styles.py                    # โมดูลตกแต่ง CSS และ Plotly Brand Styling
├── tests/
│   └── test_app.py                  # Unit testing สคริปต์ความถูกต้องของข้อมูล
├── .gitignore                       # ละเว้นไฟล์ที่ไม่ต้องการติดตามใน Git
├── requirements.txt                 # รายการ Dependencies ภาษา Python
└── README.md                        # เอกสารคู่มือโครงการและสรุปผลงาน
```

---

## 📊 4. ข้อกำหนดชุดข้อมูล (Data Specification & Data Dictionary)

| Column Name | Data Type | Physical Unit | Sensor Source | Clinical Normal Range | Description / Clinical Rationale |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `Patient_ID` | `String` | - | Master Registry | `PT-1001` - `PT-9999` | รหัสประจำตัวผู้ป่วยแบบนิรนาม (De-identified) |
| `Patient_Name` | `String` | - | Clinical Record | - | ชื่อ-สกุล หรือชื่อสมมติของผู้ป่วย |
| `Age` | `Integer` | Years | Demographic | 18 - 95 | อายุของผู้ป่วย |
| `Gender` | `String` | - | Demographic | Male / Female | เพศทางสรีรวิทยา |
| `Diagnosis` | `String` | - | EHR Record | Categorical | การวินิจฉัยโรคหลัก (เช่น DPN, Fibromyalgia, Post-Op) |
| `Timestamp` | `DateTime` | ISO 8601 | Device Clock | YYYY-MM-DD HH:MM | เวลาที่ทำการอ่านค่าและประมวลผลข้อมูล |
| `Heart_Rate_BPM` | `Float` | bpm | PPG Sensor | 60.0 - 100.0 | อัตราการเต้นของหัวใจแบบ Real-time |
| `HRV_RMSSD` | `Float` | ms | PPG Sensor | 30.0 - 65.0 | ดัชนีระบบประสาทพาราซิมพาเทติก (<20ms = Sympathetic Crisis/Pain) |
| `Gait_Symmetry_Score` | `Float` | % | 6-Axis IMU | 85.0% - 100.0% | ดัชนีความสมมาตรของการก้าวเดิน (<70% = เดินกะเผลกหลีกเลี่ยงความเจ็บปวด) |
| `Pressure_Asymmetry_Pct` | `Float` | % | Insole Sensor | < 10.0% | ความต่างของการถ่ายน้ำหนักระหว่างเท้าซ้าย-ขวา (>20% = Antalgic Guarding) |
| `Cadence_SPM` | `Float` | steps/min | 6-Axis IMU | 95.0 - 120.0 | จำนวนก้าวเดินต่อนาที (ลดฮวบเมื่อเกิดความเหนื่อยล้าทางประสาทกล้ามเนื้อ) |
| `Stride_Time_Variability_Pct` | `Float` | % | 6-Axis IMU | < 4.0% | ความไม่สม่ำเสมอของรอบก้าว (>6% เสี่ยงต่อการล้มสูง) |
| `Peak_Heel_Pressure_kPa` | `Float` | kPa | Insole Sensor | 180.0 - 320.0 | แรงกดสูงสุดบริเวณส้นเท้าขณะก้าวลงน้ำหนัก |
| `Peak_Forefoot_Pressure_kPa`| `Float` | kPa | Insole Sensor | 150.0 - 280.0 | แรงกดสูงสุดบริเวณกระดูกฝ่าเท้าส่วนหน้าขณะส่งตัว |
| `Daily_Step_Count` | `Integer` | steps | Pedometer | 4,000 - 10,000 | จำนวนก้าวสะสมในรอบวัน |
| `Fatigue_Level` | `String` | Level | AI Multimodal | Low / Moderate / High / Severe | ระดับความเหนื่อยล้าของร่างกายและระบบประสาท |
| `Pain_Score_AI` | `Float` | 0 - 10 | Multimodal AI | 0.0 - 10.0 | ดัชนีความเจ็บปวดเชิงวัตถุวิสัยที่ AI คำนวณจาก HRV + Gait |
| `Alert_Status` | `String` | Categorical | Triage Engine | Normal / Warning / Critical | ระดับการเตือนภัยทางคลินิกเพื่อส่งต่อบุคลากรทางการแพทย์ |
| `Recommended_Action` | `String` | Text | Clinical CDSS | Prescriptive Directive | ข้อเสนอแนะการรักษาหรือการปรับพฤติกรรมทันที |

---

## 🎨 5. การออกแบบ Dashboard เชิงเล่าเรื่อง (Storytelling Dashboard Design)

### 5.1 อัตลักษณ์ของแบรนด์ (Brand Identity)
- **Primary Color:** Deep Navy (`#0F172A`) — ความน่าเชื่อถือ สุขุม และมาตรฐานระดับสากล
- **Brand Accent:** Medical Cyan (`#00A896`) — ความล้ำสมัยด้านเทคโนโลยีชีวการแพทย์ และความสะอาด
- **Alert Accent:** Pulse Coral (`#E63946`) — การเตือนภัยทางคลินิกเมื่อสัญญาณชีพหรือความปวดเข้าสู่ภาวะวิกฤต
- **Background:** Clinical Clean (`#F8FAF8`) — ความสบายตา สะอาด บริสุทธิ์ เหมาะกับบุคลากรทางการแพทย์
- **Typography:** Google Fonts `Poppins` (ข้อมูลเชิงตัวเลขและภาษาอังกฤษ) คู่กับ `Noto Sans Thai` (ภาษาไทย)

### 5.2 ลำดับการเล่าเรื่อง (Narrative Arc) 4 ส่วน
1. **Section 1: Executive Overview & Real-time Alert**
   - การแสดงบัตรตัวเลข KPI 4 ช่อง: จำนวนผู้ป่วยในการดูแล, จำนวนเคสวิกฤต (Critical Flare-ups), ค่าเฉลี่ยระดับความปวดทั้งกลุ่ม, และค่าเฉลี่ย HRV
   - แผนภูมิ Donut Chart แสดงสัดส่วน Triage Alert Status และตารางผู้ป่วยที่แยกสีความเร่งด่วนตามสถานะ
2. **Section 2: Physiological Correlation**
   - Interactive Scatter Plot พิสูจน์ความสัมพันธ์ระหว่างค่า HRV RMSSD (แกน X) กับ AI Pain Score (แกน Y) โดยปรับขนาดตาม Pressure Asymmetry %
   - Radar Chart เปรียบเทียบ Biomarkers 5 มิติ ระหว่างผู้ป่วยที่มีอาการปวดกำเริบ (Critical) กับผู้ป่วยที่ควบคุมอาการได้ดี (Normal)
3. **Section 3: Recovery & Trend Analysis**
   - Time-series Tracking แสดงผล 30 วันของผู้ป่วยรายบุคคล แสดงจุดเปลี่ยนทางคลินิก (Clinical Milestone Day 12) ที่ค่าความปวดลดลงและ HRV/Gait ดีขึ้นอย่างเห็นได้ชัด
   - Grouped Bar Chart แสดงผลลัพธ์การลดภาระโรงพยาบาล (ER visits ลดลง 68%, การนอนโรงพยาบาลซ้ำลดลง 44%)
4. **Section 4: Clinical & Business Actionable Insights**
   - ระบบ Clinical Decision Support System (CDSS) ให้คำแนะนำการแพทย์เฉพาะบุคคล
   - โมเดลทางธุรกิจ Health Economics ROI ประเมินความคุ้มค่าของการลงทุน (4.4x ROI) และการประหยัดค่าใช้จ่ายฉุกเฉิน 24,600 บาทต่อไตรมาส

---

## 🚀 6. ขั้นตอนการติดตั้งและรัน Dashboard (Installation & Quickstart)

### ข้อกำหนดเบื้องต้น (Prerequisites)
- มีการติดตั้ง **Python 3.10 ขึ้นไป**
- มีโปรแกรม Git หรือดาวน์โหลด Source Code ลงในเครื่อง

### ขั้นตอนการรัน
```bash
# 1. Clone repository หรือเข้าสู่โฟลเดอร์โครงการ
cd Mini_project_datawarehouse

# 2. (แนะนำ) สร้างและเปิดใช้งาน Virtual Environment
python -m venv venv
# สำหรับ Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# สำหรับ macOS/Linux:
source venv/bin/activate

# 3. ติดตั้ง Dependencies ที่จำเป็น
pip install -r requirements.txt

# 4. สร้างชุดข้อมูลจำลอง (หากยังไม่มีไฟล์ CSV ในโฟลเดอร์ data/)
python src/data_loader.py

# 5. สั่งรัน Streamlit Application
streamlit run src/app.py
```

เมื่อรันคำสั่งสำเร็จ ระบบจะเปิด Web Browser ขึ้นมาที่ `http://localhost:8501` โดยอัตโนมัติ

### 🖥️ 6.1 การเปิดสไลด์นำเสนอ (Interactive Presentation Deck)
สามารถเปิดไฟล์สไลด์นำเสนอผ่าน Web Browser ได้ทันทีโดยไม่ต้องติดตั้งเซิร์ฟเวอร์:
- ดับเบิลคลิกไฟล์ [presentation/index.html](file:///d:/Mini_project_datawarehouse/presentation/index.html) เพื่อเริ่มนำเสนอ
- อ่านบทสคริปต์การนำเสนอฉบับเต็มได้ที่ [docs/presentation_slides.md](file:///d:/Mini_project_datawarehouse/docs/presentation_slides.md)
- **คีย์ลัดสำหรับการนำเสนอ:**
  - `ลูกศรขวา` หรือ `Spacebar` หรือ `Page Down`: เลื่อนไปสไลด์ถัดไป
  - `ลูกศรซ้าย` หรือ `Page Up`: ย้อนกลับสไลด์ก่อนหน้า
  - `Home` / `End`: ไปยังสไลด์แรก / สไลด์สุดท้าย
  - `F`: สลับโหมดเต็มหน้าจอ (Fullscreen Mode)
  - `Ctrl + P`: สั่งพิมพ์หรือ Save as PDF Slide Deck

---

## 👥 7. ข้อมูลสมาชิกกลุ่มผู้จัดทำ (Group Member Registration Template)

**รายวิชา:** Business Idea Creation  
**ชื่อกลุ่มโครงการ:** CHRONI-SENSE LABS (ผลิตภัณฑ์ SOCKONE)  

| ลำดับ | รหัสนักศึกษา | ชื่อ - นามสกุล | บทบาทหน้าที่ในโครงการ (Role) | ขอบเขตงานที่รับผิดชอบ (Key Responsibilities & Deliverables) | สัดส่วนงาน (%) |
| :---: | :---: | :--- | :--- | :--- | :---: |
| 1 | `67160213` | นาย/นางสาว [หัวหน้าโครงการ] | **Product Owner & Business Strategist** | กำหนดวิสัยทัศน์ผลิตภัณฑ์, วิเคราะห์ Business Model & Health Economics ROI, บริหารภาพรวม | 25% |
| 2 | `6716xxxx` | นาย/นางสาว [วิศวกรข้อมูล/AI] | **AI & Data Engineer Specialist** | ออกแบบ Data Schema, พัฒนาอัลกอริทึมจำลองสัญญาณเซนเซอร์ (PPG/IMU), คำนวณ Pain Score AI | 25% |
| 3 | `6716xxxx` | นาย/นางสาว [ผู้ออกแบบ UX/UI] | **UX/UI Storytelling Dashboard Lead** | ออกแบบ Narrative Arc, สร้าง Interactive Dashboard ด้วย Streamlit + Plotly, วางระบบ Brand Identity | 25% |
| 4 | `6716xxxx` | นาย/นางสาว [ที่ปรึกษาคลินิก] | **Clinical Domain & Medical Market Analyst** | ศึกษาความสัมพันธ์ทางสรีรวิทยา (HRV & Antalgic Gait), จัดทำ CDSS Rule-based Guidelines, เขียนเอกสารสรุป | 25% |

---

## 📜 8. ลิขสิทธิ์และการอนุญาตให้ใช้งาน (License)

โครงการนี้พัฒนาขึ้นเพื่อการเรียนการสอนในรายวิชา Business Idea Creation ภายใต้สัญญาอนุญาต [MIT License](LICENSE)