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
        "Practice rules:\n"
        "- Baseline: 10 years.\n"
        "- If salary ≥ £50,270 → 5 years.\n"
        "- If salary ≥ £125,140 AND earned for 3 continuous years → 3 years (fast-track)."
    )

    years = 10  # baseline

    if salary >= 50270:
        years = 5

    if salary >= 125140:
        three_years = st.checkbox(
            "I have earned £125,140 or more for at least 3 continuous years"
        )
        if three_years:
            years = 3

elif route == "Global Talent / Innovator Founder / fast-track route":
    st.info("Fast-track route assumed at 3 years for Global Talent / Innovator Founder.")
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
        "Rule:\n"
        "- Baseline 10 years.\n"
        "- Benefits < 1 year → +5 years = 15 years.\n"
        "- Benefits ≥ 1 year → +10 years = 20 years."
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
        years = base_years + 5
    else:
        years = base_years + 10

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
    "This is not an official Home Office rule."
)

if years is not None and has_c1:
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

        if has_c1:
            st.caption(
                "C1 English selected → 1-year reduction applied. "
                "Real Home Office rules may differ."
            )

        st.warning(
            "⚠ IMPORTANT:\n\n"
            "- This tool is for PRACTICE and CODE LEARNING only.\n"
            "- It loosely follows proposals in the 2025 immigration white paper and GOV.UK announcements.\n"
            "- Proposals may change before becoming law."
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
