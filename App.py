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
        "- If salary ≥ £50,270 → 5 years (higher-skilled earner example).\n"
        "- If salary ≥ £125,140 AND you’ve earned this for 3 continuous years → 3 years "
        "(treated like an ultra high-earner / Global Talent-style route)."
    )

    # Start with baseline
    years = 10

    # Mid–high earners: 5 years
    if salary >= 50270:
        years = 5

    # Ultra high earner: £125,140+ for at least 3 continuous years → 3 years
    if salary >= 125140:
        three_years = st.checkbox(
            "I have earned £125,140 or more for at least 3 continuous years"
        )
        if three_years:
            years = 3  # 7-year reduction from 10 → 3

elif route == "Global Talent / Innovator Founder / fast-track route":
    st.info(
        "Fast-track route for the 'brightest and best' (e.g. Global Talent, Innovator Founder "
        "and some very high earners). For practice, we assume a 3-year qualifying period."
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
        "Practice example based on the proposals: migrants reliant on benefits or in some "
        "protection routes may face a 20-year wait."
    )
    years = 20

elif route == "Illegal migrant / long overstay":
    years = 30

# ---------------------
# INTEGRATION / ENGLISH EXAMPLE
# ---------------------
st.markdown("---")
st.markdown("### Integration / English Example (VERY simplified)")

has_integration = st.checkbox(
    "I meet strong integration standards (e.g. high English level, stable work, regular volunteering)"
)

st.caption(
    "The consultation mentions possible reductions for contribution and integration "
    "(English, work history, volunteering, tax). There is NO official formula yet. "
    "This checkbox only shows a simple example for learning."
)

if years is not None and has_integration and years > 5:
    # Example rule for demonstration:
    # reduce by 1 years, but never below 5 years
    years_adjusted = max(5, years - 1)
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

        if has_integration and years is not None and years > 5:
            st.caption(
                "Integration box ticked → example reduction of 1 years (minimum 5 years). "
                "Real Home Office rules, if implemented, may be very different."
            )

        st.warning(
            "⚠ IMPORTANT:\n\n"
            "- This tool is for PRACTICE and CODE LEARNING only.\n"
            "- It loosely follows proposals in the 2025 immigration white paper and GOV.UK announcements.\n"
            "- Proposals are subject to consultation and may change before any law comes into force.\n"
            "- For real immigration decisions, always check the latest rules on GOV.UK "
            "or speak to a qualified immigration adviser."
        )
