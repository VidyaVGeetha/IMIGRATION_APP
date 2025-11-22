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
    "Based on the November 2025 Command Paper *A Fairer Pathway to Settlement* (CP 1448), "
    "the House of Commons Library briefing CBP-10267, and the GOV.UK press release on the "
    "new legal migration model. This is a LEARNING TOOL only and NOT official immigration advice."
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
# ROUTE-SPECIFIC LOGIC (mirrors Command Paper baseline & adjustments)
# ---------------------
if route == "High earner on a Skilled Worker / similar route":
    salary = st.number_input(
        "Enter your annual salary in £ (before tax)",
        min_value=0.0,
        step=1000.0,
        help="Example: 50,270 or 125,140"
    )

    st.info(
        "Practice rules for Skilled Worker high earners (Command Paper Table 2 – Contribution):\n"
        "- Baseline qualifying period: 10 years.\n"
        "- If salary is at least £50,270 for the last 3 years → 5-year route (10 − 5 years).\n"
        "- If salary is at least £125,140 for the last 3 years → 3-year fast-track route (10 − 7 years)."
    )

    # Start with baseline 10 years
    years = 10

    # Only if salary meets the first threshold do we ask about 3 years
    if salary >= 50270:
        three_years = st.checkbox(
            "I have earned this salary level for at least the last 3 continuous years"
        )
        if three_years:
            if salary >= 125140:
                years = 3   # 10 - 7 = 3 years
            else:
                years = 5   # 10 - 5 = 5 years

elif route == "Global Talent / Innovator Founder / fast-track route":
    st.info(
        "Command Paper Table 2 (Entry and residence): 3 years continuous residence as a "
        "Global Talent worker or Innovator Founder gives a reduction of up to 7 years. "
        "From a 10-year baseline, this means most qualify after 3 years."
    )
    years = 3

elif route == "Frontline public service (NHS doctor, nurse, teacher etc.)":
    st.info(
        "Command Paper Table 2: specified public service occupations may get a 5-year reduction. "
        "From a 10-year baseline, this gives a 5-year qualifying period."
    )
    years = 5

elif route == "Immediate family of British citizen / Hong Kong BN(O)":
    st.info(
        "Command Paper Table 2 (Entry and residence): partners/parents/children of British "
        "citizens and BN(O) route get a 5-year reduction, not subject to consultation. "
        "From a 10-year baseline, this remains a 5-year route."
    )
    years = 5

elif route == "Health & Care Worker / lower-paid worker (below RQF level 6)":
    st.info(
        "Command Paper: consultation proposal to increase the standard qualifying period for "
        "Skilled Worker roles below RQF level 6 (including many Health and Care roles) to 15 years "
        "instead of the 10-year baseline."
    )
    years = 15

elif route == "General skilled / economic migrant":
    st.info(
        "Command Paper: default earned settlement qualifying period for most economic migrants "
        "is increased from 5 years to 10 years."
    )
    years = 10

elif route == "Relying on benefits / some protection routes (practice example)":
    st.info(
        "Command Paper Table 3 (Contribution – public funds):\n"
        "- Baseline: 10 years.\n"
        "- If you have been in receipt of public funds for less than 12 months in total → +5 years.\n"
        "- If you have been in receipt of public funds for 12 months or more in total → +10 years."
    )

    base_years = 10

    benefits_duration = st.selectbox(
        "How long have you relied on benefits (public funds) in total?",
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
    st.info(
        "Command Paper Table 3 (Entry and residence): entering illegally, entering as a visitor, "
        "or overstaying 6+ months can add up to 20 extra years to the baseline 10 years.\n\n"
        "For this practice tool, we show the **worst case**: 10 + 20 = 30 years."
    )
    years = 30  # 'up to' 30 years – we model the maximum as a simple example

# ---------------------
# ENGLISH LEVEL ADJUSTMENT (Table 2 – Integration)
# ---------------------
st.markdown("---")
st.markdown("### English Level Adjustment (C1 example – Table 2)")

has_c1 = st.checkbox("My English level is C1 or higher")

st.caption(
    "Command Paper Table 2: C1 English earns a reduction of 1 year from the qualifying period. "
    "Here we apply that 1-year reduction after your route-specific total is calculated."
)

if years is not None and has_c1:
    # Reduce by 1 year, but never below 1 year (safety minimum for this demo)
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
                "C1 English selected → 1-year reduction applied (as per Command Paper Table 2). "
                "Real Home Office rules, if implemented, may change after consultation."
            )

        st.warning(
            "⚠ IMPORTANT:\n\n"
            "- This tool is for PRACTICE and CODE LEARNING only.\n"
            "- It imitates the *time adjustment* model in the November 2025 Command Paper (CP 1448), "
            "using the baseline 10 years plus/minus adjustments from Tables 2 and 3.\n"
            "- All of these proposals are still under consultation and may change before becoming law.\n"
            "- For real immigration decisions, always check the latest rules on GOV.UK or speak to a "
            "qualified immigration adviser."
        )

# ---------------------
# REFERENCES SECTION
# ---------------------
st.markdown("---")
st.markdown("## 📚 References / Sources")

st.markdown("""
### 🔗 Official Links Used

1. **A Fairer Pathway to Settlement – Command Paper (CP 1448, November 2025)**  
   https://assets.publishing.service.gov.uk/media/691edda450b16caf978153d8/Command_Paper_final_-_reviewed7.pdf  

2. **GOV.UK – Biggest overhaul of legal migration model in 50 years**  
   https://www.gov.uk/government/news/biggest-overhaul-of-legal-migration-model-in-50-years-announced  

3. **UK Parliament – House of Commons Library Briefing CBP-10267**  
   https://commonslibrary.parliament.uk/research-briefings/cbp-10267/  

4. **Global Talent Visa Information**  
   https://www.gov.uk/global-talent  

5. **UK Income Tax Rates (for £50,270 and £125,140 bands)**  
   https://www.gov.uk/income-tax-rates
""")
