import streamlit as st

# ---------------------
# Page Setup
# ---------------------
st.set_page_config(
    page_title="ILR Qualifying Period Calculator (Practice)",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 ILR Qualifying Period – Practice Calculator")

st.caption(
    "Based on examples from the 2025 immigration white paper, the House of Commons Library briefing CBP-10267 "
    "and the GOV.UK press release on the new legal migration model. "
    "This is a LEARNING TOOL only and NOT official immigration advice."
)

# ---------------------
# ROUTE SELECTION
# ---------------------
route = st.radio(
    "Select the option that best describes your situation (for practice):",
    (
        "High earner on a Skilled Worker / similar route",
        "Global Talent / Innovator Founder / fast-track route",
        "Frontline public service (NHS doctor, nurse, teacher etc.)",
        "Immediate family of British citizen / Hong Kong BN(O)",
        "Health & Care Worker / lower-paid worker (below RQF level 6)",
        "General skilled / economic migrant",
        "Relying on benefits / some protection routes (practice example)",
        "Illegal migrant / long overstay",
    )
)

years = None  # total qualifying period in YEARS

# ---------------------
# ROUTE-SPECIFIC LOGIC
# ---------------------
if route == "High earner on a Skilled Worker / similar route":
    salary = st.number_input(
        "Enter your annual salary in £ (before tax)",
        min_value=0.0,
        step=1000.0,
        help="Example: 50,270 or 125,140"
    )

    st.info(
        "Practice rules for Skilled Worker high earners:\n"
        "- Baseline: 10 years.\n"
        "- If salary is at least £50,270 held for last 3 years → 5-year route.\n"
        "- If salary is at least £125,140 and above for last 3 years → 3-year fast-track route."
    )

    years = 10  # baseline

    if salary >= 50270:
        three_years = st.checkbox(
            "I have earned this salary level for at least the last 3 continuous years"
        )
        if three_years:
            if salary >= 125140:
                years = 3
            else:
                years = 5

elif route == "Global Talent / Innovator Founder / fast-track route":
    years = 3

elif route == "Frontline publ
