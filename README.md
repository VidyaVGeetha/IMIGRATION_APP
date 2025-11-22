# 🧮 ILR Qualifying Period – Practice Calculator  

A small Streamlit web app that helps you practice how the new **“earned settlement” / ILR qualifying period model** (from the November 2025 Command Paper) might work.  

> ⚠️ **Important:** This app is a **LEARNING TOOL only**.  
> It is not official, not legal advice, and not guaranteed to reflect final Home Office rules.

---

## 🎯 Project Objective  

Understand how the **10-year baseline** ILR qualifying period can change based on:

- Route type (Skilled Worker, Global Talent, Health & Care, Economic Migrant, etc.)  
- Salary thresholds (£50,270 / £125,140 high-earner bands)  
- Use of public funds  
- English language level (C1 = 1-year reduction example)  
- Command Paper Table 2 & Table 3 “contribution” adjustments  

This app helps you learn:

- if/elif logic in Python  
- How to build interactive UI with Streamlit  
- How new ILR “earned settlement” timelines may work  

---

## 🧠 What the App Does  

The app asks you which route applies:

- High earner (Skilled Worker)
- Global Talent / Innovator Founder
- NHS doctor, nurse, teacher (public service)
- Family of British citizen / BN(O)
- Health & Care Worker (below RQF6)
- General skilled / economic migrant
- Relying on benefits (practice example)
- Illegal entry / long overstay (practice)

Using this choice, it calculates a *practice* ILR qualifying period:

### 🔹 Baseline  
**10 years** (earned settlement starting point)

### 🔹 Example Adjustments  
- **High earner**  
  - Salary ≥ £50,270 for 3 years → **5-year** route  
  - Salary ≥ £125,140 for 3 years → **3-year** route  

- **Global Talent / Innovator Founder** → **3 years**  

- **NHS/public service** → **5 years**  

- **Family of British citizen / BN(O)** → **5 years**  

- **Health & Care Worker, lower-paid** → **15 years** (consultation example)  

- **General economic migrant** → **10 years**  

- **Public funds / benefits**  
  - < 1 year on benefits → **15 years**  
  - ≥ 1 year on benefits → **20 years**  

- **Illegal entry / long overstay**  
  - Practice example: **30 years** (10 + 20)  

### 🔹 English Level Adjustment  

If user selects **C1 English**, the app subtracts **1 year** from the total.

---

## 🛠 Tech Stack  

- **Python**  
- **Streamlit**  
- UI elements used:  
  `st.radio`, `st.number_input`, `st.checkbox`, `st.selectbox`,  
  `st.button`, `st.info`, `st.success`, `st.warning`, `st.caption`

---

## ▶️ Running the App  

Install Streamlit:

```bash
pip install streamlit
