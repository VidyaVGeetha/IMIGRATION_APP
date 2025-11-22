import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------
# Page Setup
# ---------------------
st.set_page_config(page_title="Scotland Dashboard & ILR Calculator", page_icon="📊", layout="wide")

st.title("📊 Scotland Life Expectancy & ILR Calculator (Demo App)")
st.write("This app has two parts: a sample life expectancy dashboard and a practice ILR calculator based on the YouTube summary.")

# ---------------------
# Tabs
# ---------------------
tab1, tab2 = st.tabs(["📈 Life Expectancy Dashboard", "🧮 ILR Qualifying Period Calculator"])

# =====================
# TAB 1: LIFE EXPECTANCY DASHBOARD
# =====================
with tab1:
    st.subheader("📊 Scotland Life Expectancy Dashboard (Sample Data)")
    st.write("This dashboard uses hard-coded sample data (no CSV required).")

    # Sample Hard-coded Data
    data = {
        "Region": [
            "North", "North", "North", "South", "South", "South",
            "West", "West", "West"
        ],
        "Year": [
            2019, 2020, 2021,
            2019, 2020, 2021,
            2019, 2020, 2021
        ],
        "LifeExpectancy": [
            79.5, 79.2, 79.0,
            80.1, 79.8, 79.4,
            78.8, 78.5, 78.2
        ]
    }

    df = pd.DataFrame(data)

    # Sidebar Filter (only affects this tab logically)
    st.sidebar.header("Dashboard Filters")
    regions = df["Region"].unique()
    selected_region = st.sidebar.selectbox("Select Region", ["All"] + list(regions))

    if selected_region != "All":
        df_filtered = df[df["Region"] == selected_region]
    else:
        df_filtered = df

    # Line Chart
    st.subheader("📈 Life Expectancy Over Time")

    fig = px.line(
        df_filtered,
        x="Year",
        y="LifeExpectancy",
        color="Region",
        markers=True,
        title="Life Expectancy Trend (Sample Data)"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Data Table
    st.subheader("📋 Underlying Data")
    st.dataframe(df_filtered)

# =====================
# TAB 2: ILR QUALIFYING PERIOD CALCULATOR (STREAMLIT VERSION)
# =====================
with tab2:
    st.subheader("🧮 ILR Qualifying Period – Practice Calculator")
    st.caption("Based on the YouTube transcript you shared. This is NOT official immigration advice.")

    # Route selection
    route = st.radio(
        "Select the option that best describes your situation:",
        (
            "High earner on a skilled route",
            "Frontline public service (doctor, nurse, teacher)",
            "Immediate family of British citizen / Hong Kong BN(O)",
            "Health & Care Worker / lower-paid worker (below RQF level 6)",
            "General skilled/economic migrant",
            "Relying on public funds / some refugees",
            "Illegal migrant / long overstay",
        )
    )

    years = None

    # Extra inputs based on route
    if route == "High earner on a skilled route":
        salary = st.number_input(
            "Enter your annual salary in £",
            min_value=0.0,
            step=1000.0,
            help="Example: 50000"
        )
        st.info("Assumption: salary at this level for at least 3 years (as in the example).")

        # Logic from transcript
        if salary >= 135000:
            years = 3
        elif salary >= 50000:
            years = 5
        else:
            years = 10  # baseline

    elif route == "Frontline public service (doctor, nurse, teacher)":
        years = 5

    elif route == "Immediate family of British citizen / Hong Kong BN(O)":
        years = 5

    elif route == "Health & Care Worker / lower-paid worker (below RQF level 6)":
        years = 15

    elif route == "General skilled/economic migrant":
        years = 10

    elif route == "Relying on public funds / some refugees":
        public_funds_duration = st.selectbox(
            "How long have you taken public funds?",
            [
                "Less than 12 months in total",
                "12 months or more in total"
            ]
        )
        if public_funds_duration == "Less than 12 months in total":
            years = 15   # 10 + 5
        else:
            years = 20   # 10 + 10

    elif route == "Illegal migrant / long overstay":
        years = 30

    # English level adjustment
    st.markdown("---")
    st.markdown("### Integration / English Level Adjustment")
    has_c1 = st.checkbox("My English level is C1 or higher")

    if years is not None and has_c1 and years > 3:
        years_adjusted = years - 1
    else:
        years_adjusted = years

    if st.button("Calculate ILR Qualifying Period"):
        if years is None:
            st.error("Please complete the inputs above.")
        else:
            st.success(f"Estimated ILR qualifying period: **{years_adjusted} years**")
            if has_c1 and years > 3:
                st.caption("C1 English detected → reduced by 1 year from the baseline.")
            st.warning(
                "This is a simple practice tool based on a YouTube summary, "
                "not official Home Office guidance or legal advice."
            )
