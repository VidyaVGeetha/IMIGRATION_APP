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

years = None  # base qualifying period in YEARS

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

    # Start with baseline
    years = 10

    if salary >= 50270:
        three_years = st.checkbox(
            "I have earned £50,270 or more for at least 3 continuous years"
        )
        if three_years:
            years = 3      # fast-track
        else:
            years = 5      # higher earner but not 3 years continuously

elif route == "Global Talent / Innovator Founder / fast-track route":
    st.info(
        "Fast-track route for the 'brightest and best' (e.g. Global Talent, Innovator Founder). "
        "For this practice tool, we assume a 3-year qualifying period."
    )
    years = 3

elif route == "Frontline public service (NHS doctor, nurse, teacher etc.)":
    years = 5

elif route == "Immediate family of British citizen / Hong Kong BN(O)":
    years = 5

elif route == "Health & Care Worker / lower-paid worker (below RQF level 6)":
    years = 15

elif route == "General skilled / economic migrant":
    years = 10

elif route == "Relying on benefits / some protection routes (practice example)":
    st.info(
        "Practice rule for this tool:\n"
        "- Baseline: 10 years.\n"
        "- If you have relied on benefits for less than 1 year in total → +5 years = 15 years.\n"
        "- If you have relied on benefits for 1 year or more in total → +10 years = 20 years."
    )

    base_years = 10

    benefits_duration = st.selectbox(
        "How long have you relied on benefits (in total)?",
        [
            "Less than 1 year in total",
            "1 year or more in total"
        ]
    )

    if benefits_duration == "Less than 1 year in total":
        years = base_years + 5   # 15 years
    else:
        years = base_years + 10  # 20 years

elif route == "Illegal migrant / long overstay":
    years = 30

# ---------------------
# ENGLISH LEVEL ADJUSTMENT
# ---------------------
st.markdown("---")
st.markdown("### English Level Adjustment (C1 example)")

has_c1 = st.checkbox("My English level is C1 or higher")

st.caption(
    "For this practice tool, C1 English reduces your qualifying period by 1 year. "
    "This is NOT an official Home Office rule – just a simple learning example."
)

if years is not None and has_c1:
    # Reduce by 1 year, but never below 1 year (safety minimum for demo)
    years_adjusted = max(1, years - 1)
else:
    years_adjusted = years

# ---------------------
# CALCULATE BUTTON
# ---------------------
if st.button("Calculate (Practice Only)"):
    if years is None:
        st.error("Please complete the inputs above.")
    else:
        st.success(f"Estimated ILR qualifying period (practice only): **{years_adjusted} years**")

        if has_c1 and years is not None:
            st.caption(
                "C1 English selected → 1-year reduction applied to the practice estimate. "
                "Real Home Office rules, if implemented, may be different."
            )

        st.warning(
            "⚠ IMPORTANT:\n\n"
            "- This tool is for PRACTICE and CODE LEARNING only.\n"
            "- It loosely follows proposals in the 2025 immigration white paper and GOV.UK announcements.\n"
            "- Proposals are subject to consultation and may change before any law comes into force.\n"
            "- For real immigration decisions, always check the latest rules on GOV.UK "
            "or speak to a qualified immigration adviser."
        )

# ---------------------
# REFERENCES SECTION
# ---------------------
st.markdown("---")
st.markdown("## 📚 References / Sources")

st.markdown("""
### 🔗 Official Links Used

1. **GOV.UK – Biggest overhaul of legal migration model in 50 years**  
   https://www.gov.uk/government/news/biggest-overhaul-of-legal-migration-model-in-50-years-announced

2. **UK Parliament – House of Commons Library Briefing CBP-10267**  
   https://commonslibrary.parliament.uk/research-briefings/cbp-10267/

3. **Global Talent Visa Information**  
   https://www.gov.uk/global-talent

4. **UK Income Tax Rates (for £125,140 high-earner band)**  
   https://www.gov.uk/income-tax-rates
""")
