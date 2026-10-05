# 📑 Presentation Deck Script: SOCKONE by CHRONI-SENSE LABS
### สไลด์นำเสนอโครงการ Dashboard เชิงเล่าเรื่อง (Storytelling Dashboard)
**รายวิชา:** Business Idea Creation  
**หัวข้อ:** การออกแบบ Storytelling Dashboard ผลิตภัณฑ์ "SOCKONE" ถุงเท้าอัจฉริยะประเมินความเจ็บปวดเรื้อรังและความเหนื่อยล้า  
**รูปแบบการส่งงาน:** GitHub Repository & Interactive Slide Deck  

---

## 🧭 โครงสร้างสไลด์ (Slide Outline: 10 Slides)

- **Slide 1:** Title & Executive Pitch (หน้าปกโครงการ, แบรนด์ CHRONI-SENSE LABS, และผลิตภัณฑ์ SOCKONE)
- **Slide 2:** Corporate Context & Problem Statement (บริบทธุรกิจ, ปัญหาความเจ็บปวดเรื้อรัง, และจุดบกพร่องของการวัดผลแบบเดิม)
- **Slide 3:** Product Innovation & Sensor Architecture (ฮาร์ดแวร์ถุงเท้าอัจฉริยะ 3 เซนเซอร์หลัก: PPG, Insole Matrix, IMU)
- **Slide 4:** [ส่วนที่ 1] ข้อมูลที่ใช้ (Data Specification, JSON Schema & Data Dictionary)
- **Slide 5:** Data Pipeline & Data Warehouse Flow (กระบวนการไหลของข้อมูลจาก Edge สู่ Storytelling Dashboard)
- **Slide 6:** [ส่วนที่ 2] Dashboard เชิงเล่าเรื่อง: การวางลำดับ Narrative Arc 4 องก์
- **Slide 7:** Dashboard Deep-Dive: สรุปภาพรวมและผลการวิเคราะห์ทางคลินิก (Sections 1-4 Highlights)
- **Slide 8:** Health Economics & Business Model ROI (คุณค่าทางธุรกิจ การลดภาระโรงพยาบาล และผลตอบแทน 4.4x)
- **Slide 9:** [ส่วนที่ 3] รายชื่อสมาชิกกลุ่มและบทบาทหน้าที่ (Group Members & Responsibilities)
- **Slide 10:** [ส่วนที่ 4] โครงสร้าง Repository และขั้นตอนการรันผลงาน (GitHub Structure & Quickstart)

---

## 🎙️ บทพูดและเนื้อหาสไลด์ทีละสไลด์ (Detailed Slide-by-Slide Script)

---

### Slide 1: Title & Executive Pitch
- **หัวข้อสไลด์:** SOCKONE: Multimodal Pain & Fatigue Tele-Monitoring
- **สโลแกน:** "From Subjective Guesswork to Objective Telemetric Precision"
- **ชื่อบริษัท:** CHRONI-SENSE LABS Co., Ltd.
- **รายวิชา:** Business Idea Creation
- **คำบรรยายผู้นำเสนอ (Speaker Script):**
  > "สวัสดีครับอาจารย์และเพื่อนๆ ทุกท่าน วันนี้กลุ่ม CHRONI-SENSE LABS มีความยินดีที่จะนำเสนอผลงานโครงการออกแบบ Storytelling Dashboard สำหรับนวัตกรรมถุงเท้าอัจฉริยะ 'SOCKONE' ซึ่งเป็นโซลูชัน Deep-Tech ด้านการแพทย์เพื่อปฏิวัติการประเมินความเจ็บปวดเรื้อรังและความเหนื่อยล้าของผู้ป่วยผ่านสัญญาณชีวภาพ HRV และพลศาสตร์การเดิน Gait Dynamics ครับ"

---

### Slide 2: Corporate Context & The Unsolved Healthcare Crisis
- **หัวข้อสไลด์:** ทำไมต้อง CHRONI-SENSE LABS และทำไมต้องเป็น SOCKONE?
- **ปัญหา (The Pain Point):**
  - ผู้ป่วยโรคเบาหวาน (DPN), โรคปวดกล้ามเนื้อ (Fibromyalgia) และผู้ป่วยผ่าตัดเปลี่ยนข้อเข่า ประสบปัญหาอาการปวดเรื้อรังและกำเริบแบบเฉียบพลัน (Flare-up) ขณะอยู่ที่บ้าน
  - การวัดความปวดในปัจจุบันใช้ **"คำพูดคนไข้ (Subjective VAS Scale 0-10)"** ซึ่งไม่ต่อเนื่อง ไม่สามารถคาดการณ์ล่วงหน้าได้
  - ส่งผลให้เกิดการเข้าห้องฉุกเฉิน (ER) โดยไม่จำเป็น และเพิ่มอัตราการกลับมานอนโรงพยาบาลซ้ำ (Re-admission) สร้างความสูญเสียทางเศรษฐกิจกว่า 24,600 บาท/คน/ไตรมาส
- **คำบรรยายผู้นำเสนอ:**
  > "ปัญหาใหญ่ที่สุดของวงการเวชศาสตร์ฟื้นฟูคือ 'เรามองไม่เห็นความเจ็บปวดของคนไข้เมื่อเขากลับบ้าน' หมอถามว่าปวดระดับไหน คนไข้ก็ตอบตามความรู้สึก ทำให้ปรับยาไม่ตรงจุดและมักมา รพ. เมื่อสายเกินไปจนต้องเข้าห้องฉุกเฉิน บริษัทเราจึงสร้าง SOCKONE ขึ้นมาเพื่อเปลี่ยนความรู้สึกให้กลายเป็นตัวเลขทางการแพทย์ที่จับต้องได้ครับ"

---

### Slide 3: Product Innovation: 3-Sensor Multimodal Triad
- **หัวข้อสไลด์:** นวัตกรรมฮาร์ดแวร์ตรวจวัดแบบพหุโมดอล (Hardware Architecture)
- **3 เซนเซอร์ทางการแพทย์ที่ฝังในถุงเท้า:**
  1. **Optical PPG Sensor (Medial Malleolus):** วัดการเต้นของหัวใจและความแปรปรวน HRV (RMSSD) สะท้อนการทำงานของระบบประสาทพาราซิมพาเทติก
  2. **Multi-Zone Plantar Pressure Matrix:** วัดแรงกดฝ่าเท้า 4 โซน (Heel, Midfoot, Forefoot, Toes) ตรวจจับแรงก้าวและความเหลื่อมล้ำซ้าย-ขวา
  3. **6-Axis IMU (Ankle):** วัดจลนศาสตร์การเดิน ความถี่ก้าว (Cadence), ความสมมาตร (Gait Symmetry), และความแปรปรวนของเวลาต่อก้าว
- **คำบรรยายผู้นำเสนอ:**
  > "SOCKONE รวม 3 เซนเซอร์ในรูปแบบถุงเท้าที่ใส่สบาย ได้แก่ PPG ที่ตาตุ่มด้านในเพื่ออ่าน HRV, แผ่นเซนเซอร์แรงกดใต้ฝ่าเท้า และเซนเซอร์ IMU ที่ข้อเท้า ทำให้เราได้ข้อมูลทั้งระบบประสาทอัตโนมัติและการเคลื่อนไหวไปพร้อมกันอย่างไร้รอยต่อครับ"

---

### Slide 4: [ส่วนที่ 1] ชุดข้อมูลที่ใช้ (Data Specification & Schema)
- **หัวข้อสไลด์:** ข้อกำหนดชุดข้อมูล (Data Specification & JSON Schema)
- **สาระสำคัญ:**
  - กำหนดโครงสร้างข้อมูลตามมาตรฐาน **JSON Schema Draft 2020-12** และจัดเก็บในรูปแบบ **CSV / Parquet**
  - **ตัวชี้วัดสำคัญ (Key Features):**
    - `Patient_ID`, `Timestamp`, `Diagnosis`
    - `Heart_Rate_BPM` (60-100 bpm) & `HRV_RMSSD` (30-65 ms; <20 ms = Crisis)
    - `Gait_Symmetry_Score` (85-100%; <70% = เดินกะเผลก)
    - `Pressure_Asymmetry_Pct` (<10%; >20% = Antalgic Guarding)
    - `Cadence_SPM` & `Stride_Time_Variability_Pct`
    - `Pain_Score_AI` (0.0-10.0 continuous objective score)
    - `Alert_Status` (`Normal`, `Warning`, `Critical`)
- **คำบรรยายผู้นำเสนอ:**
  > "ในส่วนของข้อมูล เราได้ออกแบบ Data Schema ที่รัดกุม ครอบคลุมทั้งข้อมูลทางประชากรศาสตร์ สัญญาณชีวภาพ ค่าการเคลื่อนไหว และผลลัพธ์จาก AI โดยมีชุดข้อมูลจำลองทั้งแบบภาพรวมกลุ่มผู้ป่วย 12 คน และข้อมูลติดตามผลต่อเนื่อง 30 วัน เพื่อนำมาสร้าง Storytelling Dashboard ครับ"

---

### Slide 5: Data Pipeline & Data Warehouse Integration
- **หัวข้อสไลด์:** สถาปัตยกรรมการประมวลผลและการจัดเก็บข้อมูล (Data Warehouse Pipeline)
- **ผังการไหลของข้อมูล:**
  ```
  [ SOCKONE Wearable ] ──(BLE 5.3)──> [ Edge Hub / Mobile ]
                                             │ (MQTT / TLS)
                                             ▼
                                  [ Cloud Data Warehouse ]
                                  - Raw Telemetry Lake
                                  - Feature Store (HRV, Gait)
                                  - Edge-AI Inference (Pain Score)
                                             │
                                             ▼
                              [ Streamlit Storytelling Dashboard ]
  ```
- **คำบรรยายผู้นำเสนอ:**
  > "ข้อมูลถูกส่งผ่าน Bluetooth Low Energy ไปยังสมาร์ตโฟน แล้วสตรีมเข้าสู่ Cloud Data Warehouse เพื่อทำการแปลงข้อมูลเป็น Feature ทางชีวการแพทย์ และประมวลผลผ่านโมเดล AI ก่อนส่งต่อให้แพทย์ดูผ่าน Dashboard แบบ Real-time ครับ"

---

### Slide 6: [ส่วนที่ 2] การออกแบบ Dashboard เชิงเล่าเรื่อง (Storytelling Design)
- **หัวข้อสไลด์:** Brand Identity & การวางลำดับการเล่าเรื่อง (Narrative Arc)
- **Brand Identity Palette:**
  - **Primary (Deep Navy - `#0F172A`):** ความน่าเชื่อถือ สุขุม และมาตรฐานการแพทย์
  - **Accent (Medical Cyan - `#00A896`):** ความสะอาด นวัตกรรม และการฟื้นฟู
  - **Alert (Pulse Coral - `#E63946`):** สัญญาณเตือนภาวะวิกฤตความเจ็บปวด
  - **Background (Clinical Clean - `#F8FAF8`):** สบายตา ลดความล้าในการทำงาน
- **4-Part Narrative Arc:**
  1. *Section 1: Executive Overview & Real-time Alert* (เห็นภาพรวมและเคสวิกฤตทันทีใน 5 วินาที)
  2. *Section 2: Physiological Correlation* (ไขความลับความสัมพันธ์ HRV + Gait ต่อความเจ็บปวด)
  3. *Section 3: Recovery & Trend Analysis* (ติดตาม 30 วัน เห็นจุดเปลี่ยน Day 12 และการลดภาระ รพ.)
  4. *Section 4: Clinical & Business Actionable Insights* (ระบบ CDSS สั่งการแพทย์ และคำนวณ ROI)

---

### Slide 7: Dashboard Highlights & Live Demonstration
- **หัวข้อสไลด์:** ผลงาน Dashboard จริง (Python Streamlit + Plotly)
- **จุดเด่นทางเทคนิคและ UX:**
  - Interactive Filter กรองตามประเภทโรคและระดับความเร่งด่วน
  - Bubble Scatter Chart ที่เห็นจุดตัดชัดเจน: เมื่อ HRV < 20 ms + Pressure Asymmetry > 20% ความปวดจะพุ่งแตะ 7-9 ทันที
  - 5-Axis Spider Radar Chart แสดงความต่างระหว่างผู้ป่วยกำเริบกับผู้ป่วยฟื้นตัวดี
  - Multi-Axis 30-Day Trend Chart ชี้จุด **Clinical Intervention Day 12**
- **คำบรรยายผู้นำเสนอ:**
  > "Dashboard ของเราพัฒนาด้วย Streamlit และ Plotly โดยไม่เพียงแสดงตัวเลข แต่พาคุณหมอเดินทางผ่าน 4 เรื่องราว ตั้งแต่การคัดกรองเคสด่วน ไปจนถึงการวิเคราะห์ความสัมพันธ์เชิงลึก และสรุปแนวทางการรักษาเฉพาะบุคคลครับ"

---

### Slide 8: Business Impact & Health Economics ROI
- **หัวข้อสไลด์:** คุณค่าทางธุรกิจและผลตอบแทนการลงทุน (Business Idea Creation Core)
- **ตัวเลขชี้วัดผลลัพธ์ (Proven Impact):**
  - **ลดการเข้าห้องฉุกเฉิน (ER Visits):** ลดลง **68%**
  - **ลดการมา รพ. นอกนัด (Unplanned OPD):** ลดลง **52%**
  - **ลดการนอนโรงพยาบาลซ้ำใน 30 วัน:** ลดลง **44%**
  - **ต้นทุนค่าบริการ:** ฿1,850 / ผู้ป่วย / เดือน
  - **มูลค่าการประหยัดค่ารักษาฉุกเฉิน:** ฿24,600 / ผู้ป่วย / ไตรมาส
  - **ผลตอบแทนจากการลงทุน (ROI):** **4.4 เท่า (4.4x ROI)**
- **โมเดลรายได้:** B2B Remote Patient Monitoring (RPM) Prescription + AI SaaS Subscription

---

### Slide 9: [ส่วนที่ 3] รายชื่อสมาชิกกลุ่มและบทบาทหน้าที่ (Group Members)
- **หัวข้อสไลด์:** โครงสร้างทีมงาน CHRONI-SENSE LABS
- **การจัดสรรบทบาทตามความเชี่ยวชาญ:**
  1. **Product Owner & Business Strategist (25%):** วางแผนทิศทางธุรกิจ, ออกแบบ Value Proposition & Health Economics ROI
  2. **AI & Data Science Engineer (25%):** ออกแบบ Data Schema, พัฒนาอัลกอริทึมจำลองสัญญาณชีวภาพ และคำนวณ Pain Score AI
  3. **UX/UI Storytelling Dashboard Lead (25%):** ออกแบบ Brand Palette, วางผัง Narrative Arc, พัฒนา Streamlit + Plotly Dashboard
  4. **Clinical Domain & Market Analyst (25%):** รวบรวมงานวิจัยทางการแพทย์, ออกแบบระบบ Clinical CDSS Rules, จัดทำเอกสารและทดสอบระบบ

---

### Slide 10: [ส่วนที่ 4] โครงสร้าง Repository & ขั้นตอนการรัน (GitHub Delivery)
- **หัวข้อสไลด์:** โครงสร้าง GitHub Repository มาตรฐานสากล & การรันผลงาน
- **โครงสร้างไฟล์:**
  - `src/` (โค้ด Dashboard, Data Loader, Styling)
  - `data/` (Schema JSON, Mock Dataset CSV, Longitudinal CSV)
  - `docs/` (Data Dictionary, Storytelling Architecture)
  - `tests/` (Unit Test ตรวจสอบความถูกต้องของข้อมูล)
  - `requirements.txt` & `README.md` (เอกสารสมบูรณ์พร้อมตราสัญลักษณ์)
- **คำสั่งรันระบบ:**
  ```bash
  pip install -r requirements.txt
  python -m unittest tests/test_app.py
  streamlit run src/app.py
  ```
- **คำบรรยายปิดท้าย:**
  > "โครงการ SOCKONE ของพวกเราพร้อมสำหรับการตรวจสอบทั้งในด้าน Data Architecture, UX/UI Storytelling และ Business Feasibility พวกเราขอขอบคุณอาจารย์และคณะกรรมการทุกท่าน พร้อมเปิดรับคำถามและข้อเสนอแนะแล้วครับ!"
