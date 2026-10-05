# 🎨 SOCKONE Storytelling Dashboard Architecture
### CHRONI-SENSE LABS | UX/UI Narrative Arc Design Document

---

## 🎯 1. แก่นเรื่องหลัก (Core Narrative Concept)
> **"From Subjective Guesswork to Objective Telemetric Precision"**  
> จากความเจ็บปวดที่วัดยากด้วยคำพูด สู่ตัวเลขชีวการแพทย์ที่แม่นยำเพื่อการรักษาตรงจุดและลดภาระระบบสาธารณสุข

การออกแบบ Dashboard นี้ไม่ได้มุ่งเน้นเพียงแค่การแสดงข้อมูล (Data Display) แต่เน้น **การพาผู้ชมและผู้ตัดสินใจเดินทางผ่านลำดับการรับรู้ (Narrative Arc)** เพื่อสร้างความตระหนักรู้ เห็นความสำคัญ และนำไปสู่การตัดสินใจเชิงธุรกิจและการแพทย์

---

## 📐 2. การจัดวางโทนสีและ Typography (Design System)

| Token Name | Hex Code | Semantic Role | Rationale |
| :--- | :---: | :--- | :--- |
| **Deep Navy** | `#0F172A` | Primary Surface / Text | ให้ความรู้สึกหนักแน่น น่าเชื่อถือ และเป็นมาตรฐานระดับองค์กรแพทย์ |
| **Medical Cyan** | `#00A896` | Brand Accent / Positive | สื่อถึงความสะอาด นวัตกรรมชีวการแพทย์ และการฟื้นฟูสุขภาพ |
| **Pulse Coral** | `#E63946` | Critical Alert / High Pain | ดึงดูดสายตาทันทีเมื่อเกิดวิกฤตความเจ็บปวด โดยไม่สร้างความตระหนกจนเกินไป |
| **Clinical Clean** | `#F8FAF8` | Canvas Background | สบายตา ลดความล้าของสายตาแพทย์ที่ต้องอ่านแดชบอร์ดทั้งวัน |
| **Slate Gray** | `#64748B` | Secondary / Metadata | ข้อมูลบริบทและคำอธิบายเสริม |

- **Header Font:** `Poppins` (Bold / Semi-bold) — โมเดิร์น คมชัด อ่านตัวเลขได้รวดเร็ว
- **Body Font:** `Noto Sans Thai` — รองรับภาษาไทยทางการแพทย์อย่างเป็นธรรมชาติ

---

## 🎬 3. ผังการเล่าเรื่อง 4 องก์ (The 4-Part Narrative Arc)

### องก์ที่ 1: สถานการณ์ปัจจุบันและสัญญาณเตือนภัย (Executive Overview & Real-time Alert)
- **จุดมุ่งหมาย:** ให้ผู้บริหารหรือแพทย์หัวหน้าแผนกเห็น "ภาพรวมทันทีภายใน 5 วินาทีแรก"
- **การจัดวาง:**
  - KPI Cards 4 ช่อง (จำนวนผู้ป่วย, เคสวิกฤต, ค่าเฉลี่ยความปวด, ค่าเฉลี่ย HRV)
  - Donut Chart แจกแจงอัตราส่วนความเร่งด่วน (Triage Ratio)
  - Interactive Table ที่ไฮไลต์สีผู้ป่วย Critical เพื่อให้ทีมลงมือแก้ไขได้ทันที

### องก์ที่ 2: ไขปริศนาความสัมพันธ์ทางสรีรวิทยา (Physiological Correlation)
- **จุดมุ่งหมาย:** พิสูจน์ให้เห็นว่า **ทำไม SOCKONE ถึงแม่นยำ?**
- **การจัดวาง:**
  - Multimodal Bubble Scatter: แสดงให้เห็นจุดตัดชัดเจนว่าเมื่อใดที่ HRV RMSSD < 20 ms และ Pressure Asymmetry > 20% ระดับความเจ็บปวดจะพุ่งขึ้นทันที
  - Spider Radar Chart: เปรียบเทียบ Biomarkers 5 แกน ระหว่างผู้ป่วยปกติกับผู้ป่วยกำเริบ แสดงการเสียสมดุลทางกายวิภาค

### องก์ที่ 3: เส้นทางการฟื้นตัวและการลดภาระ (Recovery & Trend Analysis)
- **จุดมุ่งหมาย:** แสดงผลกระทบเชิงประจักษ์เมื่อนำ SOCKONE ไปใช้งานจริงในการดูแลผู้ป่วยต่อเนื่อง
- **การจัดวาง:**
  - Longitudinal Time-Series 30 วัน: ชี้ให้เห็นจุดเปลี่ยน (Milestone Day 12) ที่เริ่มปรับการรักษา ทำให้กราฟความปวดลดลงและสมรรถนะการเดินฟื้นตัว
  - Healthcare Impact Grouped Bar: พิสูจน์ตัวเลขการลดการเข้าห้องฉุกเฉิน (-68%) และการกลับมานอน รพ. ซ้ำ (-44%)

### องก์ที่ 4: ข้อเสนอแนะเชิงคลินิกและคุณค่าทางธุรกิจ (Actionable Insights & Health Economics)
- **จุดมุ่งหมาย:** เปลี่ยนข้อมูลเชิงลึกเป็น **"การกระทำจริงและการสร้างผลตอบแทนทางธุรกิจ"**
- **การจัดวาง:**
  - CDSS Algorithmic Directives: คำสั่งการรักษาเฉพาะบุคคล (ปรับลดน้ำหนักลงเท้า, นัดหมายพบแพทย์ด่วน, ปรับขนาดยา)
  - ROI Calculator & Remote Patient Monitoring (RPM) Business Model: แสดงจุดคุ้มทุน (ROI 4.4x) และการสร้างรายได้แบบ Recurring Subscription
