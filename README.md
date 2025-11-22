ILR Qualifying Period – Practice Calculator
Streamlit App by Vidya VG
This project is a practice ILR qualifying period calculator based on the proposed UK immigration “earned settlement” model described in:
Command Paper CP 1448 – A Fairer Pathway to Settlement (Nov 2025)
House of Commons Library Briefing CBP-10267
GOV.UK Press Release: “Biggest overhaul of legal migration model in 50 years”
Important:
This tool is not official Home Office guidance.
It is created only for learning, portfolio development, and demonstrating policy-to-logic conversion in Python.
Purpose of the App
This Streamlit app models how ILR qualifying periods may change under the proposed earned settlement scheme.
It demonstrates practical translation of government policy into structured decision logic.
The calculator adjusts ILR timelines based on:
Salary level and number of continuous years
English language level
Skilled Worker category
Health & Care Worker category
Public service occupations
Family routes
Benefits/public funds history
Illegal entry or long overstays
This project highlights Python conditional logic, user input handling, and Streamlit interface development.
Logic Summary (Based on the Command Paper)
Baseline qualifying period
General economic migrants: 10 years
Below RQF Level 6 / many Health & Care roles: 15 years
Global Talent / Innovator Founder route: 3 years
Illegal entry or long overstays: up to 30 years
Salary contribution reductions (held for last 3 continuous years)
Salary £50,270 or above → ILR in 5 years
Salary £125,140 or above → ILR in 3 years
Public service occupations
NHS doctors, nurses, teachers → ILR in 5 years
Family routes
British citizen family routes → ILR in 5 years
BN(O) family routes → ILR in 5 years
Benefits/public funds penalties
Benefits less than 12 months total → +5 years
Benefits 12 months or more total → +10 years
English language (C1 level)
C1 English reduces final ILR period by 1 year
Tech Stack
Python
Streamlit
Conditional logic modelling
Policy interpretation and implementation
