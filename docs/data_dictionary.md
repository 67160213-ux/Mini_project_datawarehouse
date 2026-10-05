# 📚 CHRONI-SENSE LABS: SOCKONE Data Dictionary
### Clinical Multimodal Telemetry Specification

เอกสารนี้ระบุรายละเอียดโครงสร้างข้อมูลเซนเซอร์ (Data Schema Specification) ของถุงเท้าอัจฉริยะ **SOCKONE** สำหรับประเมินความเจ็บปวดเรื้อรังและความเหนื่อยล้า

---

## 1. ข้อมูลทางประชากรศาสตร์และระเบียนผู้ป่วย (Demographic & Clinical Context)
- **`Patient_ID`** (`string`, Primary Key): รหัสประจำตัวผู้ป่วยที่ผ่านการนิรนาม (De-identification) ตามมาตรฐาน HIPAA/PDPA รูปแบบ `PT-XXXX`
- **`Patient_Name`** (`string`): ชื่อ-นามสกุลย่อของผู้ป่วย
- **`Age`** (`integer`): อายุ (18 - 95 ปี)
- **`Gender`** (`string`): เพศสภาพทางชีววิทยา (`Male`, `Female`, `Other`)
- **`Diagnosis`** (`string`): การวินิจฉัยโรคหลัก เช่น:
  - Diabetic Peripheral Neuropathy (โรคเส้นประสาทส่วนปลายเสื่อมจากเบาหวาน)
  - Fibromyalgia Syndrome (กลุ่มอาการปวดกล้ามเนื้อเรื้อรัง)
  - Post-Op Knee Arthroplasty (หลังผ่าตัดเปลี่ยนข้อเข่าเทียม)
  - Lumbar Radiculopathy (โรครากประสาทกระดูกสันหลังส่วนเอวถูกกดทับ)
  - Osteoarthritis Knee (โรคข้อเข่าเสื่อม)

---

## 2. ข้อมูลจากเซนเซอร์ทางสรีรวิทยา (Physiological Sensors - Optical PPG)
- **`Heart_Rate_BPM`** (`float`, หน่วย: beats per minute):
  - อัตราการเต้นของหัวใจแบบเรียลไทม์
  - ช่วงปกติขณะพัก: 60.0 - 100.0 BPM
- **`HRV_RMSSD`** (`float`, หน่วย: milliseconds):
  - Root Mean Square of Successive Differences (ความแปรผันของช่วงการเต้นของหัวใจ)
  - **Clinical Meaning:** สะท้อนถึงการทำงานของระบบประสาทพาราซิมพาเทติก (Vagal Tone)
  - **เกณฑ์การแปลผล:**
    - `> 40 ms`: สภาวะผ่อนคลาย ระบบประสาทสมดุล
    - `20 - 39 ms`: ความเครียดทางสรีรวิทยาหรือความล้าระดับปานกลาง
    - `< 20 ms`: ภาวะ **Sympathetic Crisis** เกิดอาการปวดเฉียบพลันหรือปวดเรื้อรังกำเริบ (Pain Flare-up)

---

## 3. ข้อมูลจากเซนเซอร์แรงกดฝ่าเท้า (Multi-Zone Plantar Pressure Matrix)
- **`Peak_Heel_Pressure_kPa`** (`float`, หน่วย: kilopascals):
  - แรงกดสูงสุดที่กระดูกส้นเท้า (Calcaneus) ช่วง Heel-Strike (ปกติ 180 - 320 kPa)
- **`Peak_Forefoot_Pressure_kPa`** (`float`, หน่วย: kilopascals):
  - แรงกดสูงสุดที่เนินปลายเท้า (Metatarsals) ช่วง Push-Off (ปกติ 150 - 280 kPa)
- **`Pressure_Asymmetry_Pct`** (`float`, หน่วย: %):
  - เปอร์เซ็นต์ความแตกต่างของแรงกดระหว่างเท้าซ้ายและเท้าขวา
  - **Clinical Meaning:** ตัวชี้วัดการเดินกะเผลกหลีกเลี่ยงความเจ็บปวด (Antalgic Offloading Guarding)
  - **เกณฑ์การแปลผล:**
    - `< 10%`: สมมาตรปกติ
    - `10 - 20%`: มีการระวังการลงน้ำหนักเล็กน้อย
    - `> 20%`: ภาวะ Antalgic Gait รุนแรง บ่งบอกว่าผู้ป่วยหลีกเลี่ยงการลงน้ำหนักที่ขาข้างที่มีอาการปวด

---

## 4. ข้อมูลจากเซนเซอร์ตรวจจับการเคลื่อนไหว (6-Axis IMU)
- **`Cadence_SPM`** (`float`, หน่วย: steps/minute):
  - ความถี่การก้าวเดิน (ปกติ 95 - 120 steps/min) ลดลงอย่างมีนัยสำคัญเมื่อเกิด Neuromuscular Fatigue
- **`Gait_Symmetry_Score`** (`float`, หน่วย: %):
  - คะแนนความสมมาตรของการก้าวขาซ้าย-ขวาจากการแกว่งและเร่งตัวของข้อเท้า (0 - 100%)
  - `< 70%`: ภาวะผิดปกติรุนแรง
- **`Stride_Time_Variability_Pct`** (`float`, หน่วย: %):
  - ค่าสัมประสิทธิ์ความแปรปรวนของระยะเวลาก้าว (ปกติ < 4.0%) หาก > 6.0% เสี่ยงต่อการสะดุดหกล้ม

---

## 5. ดัชนีปัญญาประดิษฐ์และระบบเตือนภัย (AI & Clinical Decision Outputs)
- **`Fatigue_Level`** (`string`): ระดับความล้า (`Low`, `Moderate`, `High`, `Severe`)
- **`Pain_Score_AI`** (`float`, สเกล 0.0 - 10.0):
  - ค่าคะแนนความเจ็บปวดที่ประมวลผลด้วย Edge-AI XGBoost & Multimodal Regressor
  - สอดคล้องกับมาตรฐานทางคลินิก Visual Analogue Scale (VAS)
- **`Alert_Status`** (`string`): สถานะคัดกรองความเร่งด่วน (`Normal`, `Warning`, `Critical`)
- **`Recommended_Action`** (`string`): คำสั่งทางการแพทย์และการดูแลเฉพาะบุคคลจากระบบ CDSS
