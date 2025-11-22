🧮 ILR Qualifying Period – Practice Calculator
A small Streamlit web app that helps you practice how the new “earned settlement” / ILR qualifying period model (from the November 2025 Command Paper) might work.
⚠️ Important: This app is a LEARNING TOOL only.
It is not official, not legal advice, and not guaranteed to reflect final Home Office rules.
🎯 Project Objective
Understand how the 10-year baseline ILR qualifying period can be increased or reduced based on:
Route type (Skilled Worker, Global Talent, Health & Care, etc.)
Salary level (e.g. £50,270 / £125,140 high-earner thresholds)
Public funds / benefits usage
English level (C1 or above – 1 year reduction example)
Practice:
If / elif logic in Python
Using Streamlit radio buttons, checkboxes, number inputs, and buttons
Showing output and warnings clearly for users
🧠 What the App Does
The app asks you to choose the option that best describes your situation (for practice):
High earner on a Skilled Worker / similar route
Global Talent / Innovator Founder / fast-track route
Frontline public service (NHS doctor, nurse, teacher etc.)
Immediate family of British citizen / Hong Kong BN(O)
Health & Care Worker / lower-paid worker (below RQF level 6)
General skilled / economic migrant
Relying on benefits / some protection routes (practice example)
Illegal migrant / long overstay
Based on that choice, it:
Starts from a baseline of 10 years (earned settlement model).
Applies route-specific adjustments, following the style of Command Paper tables 2 and 3 (as a learning approximation), for example:
🌟 High earner Skilled Worker
Baseline: 10 years
If salary ≥ £50,270 for 3 continuous years → 5-year route
If salary ≥ £125,140 for 3 continuous years → 3-year route
🌍 Global Talent / Innovator Founder → usually 3-year qualifying period
🏥 Frontline public service / NHS etc. → 5-year qualifying period
🏠 Family of British citizen / BN(O) → 5-year qualifying period
🩺 Health & Care / lower-paid (below RQF 6) → practice example 15-year period
💼 General skilled / economic migrant → 10-year period
💷 Relying on benefits / public funds →
< 1 year on benefits → 10 + 5 = 15 years
≥ 1 year on benefits → 10 + 10 = 20 years
🚫 Illegal entry / long overstay → practice worst-case: 30 years (10 + 20)
Then applies an English level adjustment (Command Paper Table 2 – Integration):
If you tick “My English level is C1 or higher”, the app subtracts 1 year from the total
It never goes below 1 year (safety floor for this demo)
When you click “Calculate (Practice Only)”, it shows:
The estimated ILR qualifying period in years
A reminder that this is for practice only and may not match final law
🛠️ Tech Stack
Language: Python
Framework: Streamlit
Main file: ilr_practice_calculator.py (or similar)
UI elements used:
st.radio – route selection
st.number_input – salary input
st.checkbox – C1 English, salary continuity
st.selectbox – benefits duration
st.button, st.info, st.success, st.warning, st.caption
