import streamlit as st

# ---------------------
# Page Setup
# ---------------------
st.set_page_config(
    page_title="ILR Qualifying Period Calculator (Practice)",
    page_icon="🧮",
    layout="centered"
)

# ---------------------
# Add Header Image
# ---------------------
st.image("UK-Immigration.png", use_column_width=True)

st.title("🧮 ILR Qualifying Period – Practice Calculator")

st.caption(
    "Based on the November 2025 Command Paper *A Fairer Pathway to Settlement* (CP 1448), "
    "the House of Commons Library briefing CBP-10267, and the GOV.UK press release on the "
    "new legal migration model. This is a LEARNING TOOL only and NOT official immigration advice.\n\n"
    "By Vidya V.G — Data Analyst Aspirant, Scotland, UK\n"
    "GitHub: https://github.com/VidyaVGeetha/IMIGRATION_APP\n"
    "Email: vidyavgk@gmail.com"
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
        "Practice rules for Skilled Worker high earners (Command Paper Table 2 – Contribution):\n"
        "- Baseline qualifying period: 10 years.\n"
        "- If salary is at least £50,270 for the last 3 years → 5-year route (10 − 5 years).\n"
        "- If salary is at least £125,140 for the last 3 years → 3-year fast-track route (10 − 7 years)."
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
    st.info(
        "Table 2: 3 years continuous residence as Global Talent / Innovator Founder reduces up to 7 years."
    )
    years = 3

elif route == "Frontline public service (NHS doctor, nurse, teacher etc.)":
    st.info(
        "Table 2: public service roles may get a 5-year reduction → 5-year route."
    )
    years = 5

elif route == "Immediate family of British citizen / Hong Kong BN(O)":
    st.info(
        "Table 2: partners/parents/children get a 5-year reduction → 5-year route."
    )
    years = 5

elif route == "Health & Care Worker / lower-paid worker (below RQF level 6)":
    st.info(
        "Consultation proposal: increase qualifying period to 15 years for lower-paid roles."
    )
    years = 15

elif route == "General skilled / economic migrant":
    st.info(
        "Default earned settlement qualifying period increased to 10 years."
    )
    years = 10

elif route == "Relying on benefits / some protection routes (practice example)":
    st.info(
        "Table 3 – Public funds contribution:\n"
        "- < 12 months on benefits → +5 years.\n"
        "- ≥ 12 months → +10 years."
    )

    base_years = 10

    benefits_duration = st.selectbox(
        "How long have you relied on benefits (public funds) in total?",
        ["Less than 1 year in total", "1 year or more in total"]
    )

    if benefits_duration == "Less than 1 year in total":
        years = base_years + 5
    else:
        years = base_years + 10

elif route == "Illegal migrant / long overstay":
    st.info(
        "Table 3: entering illegally or overstaying 6+ months may add up to 20 years."
    )
    years = 30  # baseline 10 + risk of up to +20

# ---------------------
# ENGLISH LEVEL ADJUSTMENT
# ---------------------
st.markdown("---")
st.markdown("### English Level Adjustment (C1 example – Table 2)")

has_c1 = st.checkbox("My English level is C1 or higher")

st.caption(
    "Table 2: C1 English earns a reduction of 1 year from the qualifying period."
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

        if has_c1 and years is not None:
            st.caption(
                "C1 English selected → 1-year reduction applied according to Table 2."
            )

        st.warning(
            "⚠ IMPORTANT:\n\n"
            "- This tool is for PRACTICE and CODE LEARNING only.\n"
            "- Based on the November 2025 Command Paper (CP 1448) — proposals only.\n"
            "- Real ILR rules may change after consultation.\n"
            "- Always check GOV.UK or consult an immigration adviser."
        )

# ---------------------
# REFERENCES SECTION
# ---------------------
st.markdown("---")
st.markdown("## 📚 References / Sources")

st.markdown("""
### 🔗 Official Links Used

1. **A Fairer Pathway to Settlement – Command Paper (CP 1448, Nov 2025)**  
https://assets.publishing.service.gov.uk/media/691edda450b16caf978153d8/Command_Paper_final_-_reviewed7.pdf
2. **GOV.UK – Overhaul of legal migration model**  
https://www.gov.uk/government/news/biggest-overhaul-of-legal-migration-model-in-50-years-announced
3. **House of Commons Library Briefing CBP-10267**  
https://commonslibrary.parliament.uk/research-briefings/cbp-10267/
4. **Global Talent Visa guidance**  
5. **UK Income Tax Rates (50,270 and 125,140 thresholds)**  
https://www.gov.uk/income-tax-rates
""")
