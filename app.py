# ======================================================
# 🏨 Investigating Hotel Business Using Data Visualization
# Created by Rachapalli Rajeswari
# ======================================================


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# ======================================================
# PAGE CONFIGURATION
# ======================================================


st.set_page_config(
    page_title="Investigating Hotel Business Using Data Visualization",
    page_icon="🏨",
    layout="wide"
)



# ======================================================
# LOAD DATA
# ======================================================


@st.cache_data

def load_data():

    df = pd.read_csv(
        "hotel_bookings_data.csv"
    )


    # Handle Missing Values

    df["children"] = df["children"].fillna(0)

    df["agent"] = df["agent"].fillna(0)

    df["company"] = df["company"].fillna(0)



    # Remove Duplicate Records

    df = df.drop_duplicates()



    # Feature Engineering

    df["total_stay"] = (

        df["stays_in_weekend_nights"]

        +

        df["stays_in_weekdays_nights"]

    )



    return df



df = load_data()



# ======================================================
# SIDEBAR MENU
# ======================================================


st.sidebar.title(
    "🏨 Hotel Booking Analysis"
)


st.sidebar.write("---")



page = st.sidebar.radio(

    "Select Analysis",

    [

        "Dashboard Summary",

        "Hotel Type Analysis",

        "Monthly Booking Analysis",

        "Cancellation Analysis",

        "Stay Duration Analysis",

        "Lead Time Analysis"

    ],

    key="hotel_navigation"

)



st.sidebar.write("---")



st.sidebar.info(
"""
Tools Used:

🐍 Python

🐼 Pandas

📊 Matplotlib

📈 Seaborn

🚀 Streamlit
"""
)



st.sidebar.caption(
"Created by Rachapalli Rajeswari"
)
# ======================================================
# DASHBOARD SUMMARY
# ======================================================


if page == "Dashboard Summary":


    # Main Title (Only First Page)

    st.title(
        "🏨 Investigating Hotel Business Using Data Visualization"
    )


    st.subheader(
        "Hotel Booking Business Analysis"
    )


    st.write(
    """
    This dashboard analyzes hotel booking data to understand:

    • Customer booking patterns

    • Cancellation behaviour

    • Seasonal booking trends

    • Stay duration impact

    • Lead time impact on cancellations


    The objective is to identify business insights and improve
    hotel revenue through data-driven decisions.
    """
    )


    st.divider()



    st.header(
        "📊 Business Performance Overview"
    )


    st.write(
    """
    This dashboard provides insights about booking performance,
    cancellation behaviour and customer booking patterns.
    """
    )


    st.divider()



    # ==================================================
    # KPI CALCULATIONS
    # ==================================================


    total_bookings = len(df)


    cancelled_bookings = (

        df["is_canceled"]

        .sum()

    )


    cancellation_rate = (

        df["is_canceled"]

        .mean()

        *100

    )


    avg_lead_time = (

        df["lead_time"]

        .mean()

    )


    avg_stay = (

        df["total_stay"]

        .mean()

    )


    avg_adr = (

        df["adr"]

        .mean()

    )



    # ==================================================
    # KPI CARDS
    # ==================================================


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "📋 Total Bookings",
            f"{total_bookings:,}"
        )


    with col2:

        st.metric(
            "❌ Cancelled Bookings",
            f"{cancelled_bookings:,}"
        )


    with col3:

        st.metric(
            "📉 Cancellation Rate",
            f"{cancellation_rate:.1f}%"
        )



    col4, col5, col6 = st.columns(3)



    with col4:

        st.metric(
            "⏳ Average Lead Time",
            f"{avg_lead_time:.1f} Days"
        )


    with col5:

        st.metric(
            "🛏️ Average Stay",
            f"{avg_stay:.1f} Nights"
        )


    with col6:

        st.metric(
            "💰 Average Daily Rate",
            f"{avg_adr:.2f}"
        )



    st.divider()



    # ==================================================
    # BUSINESS FINDINGS
    # ==================================================


    st.subheader(
        "📌 Key Business Findings"
    )


    hotel_share = (

        df["hotel"]

        .value_counts(normalize=True)

        *100

    )


    st.write(
    f"""
    🏙️ City Hotels contribute **{hotel_share['City Hotel']:.1f}%**
    of total bookings.


    🏖️ Resort Hotels contribute **{hotel_share['Resort Hotel']:.1f}%**
    of total bookings.


    ❌ City Hotels show higher cancellation behaviour.


    ⏳ Longer lead time increases cancellation risk.


    📅 Peak travel months generate higher booking demand.


    🛏️ Stay duration impacts customer decisions.
    """
    )



    st.divider()



    # ==================================================
    # BUSINESS OBJECTIVE
    # ==================================================


    st.subheader(
        "💡 Business Objective"
    )


    st.write(
    """
    The objective is to improve hotel occupancy,
    reduce cancellation rates, optimize pricing strategies
    and increase revenue using data-driven decisions.
    """
    )
# ======================================================
# HOTEL TYPE ANALYSIS
# ======================================================


elif page == "Hotel Type Analysis":


    st.header(
        "📊 Hotel Type Analysis"
    )


    st.write(
    """
    This section compares City Hotel and Resort Hotel
    booking performance and cancellation behaviour.
    """
    )


    st.divider()



    # ==================================================
    # BOOKING SHARE
    # ==================================================


    st.subheader(
        "🏨 Booking Share by Hotel Type"
    )



    hotel_counts = (

        df["hotel"]

        .value_counts()

    )



    col1, col2 = st.columns(2)



    with col1:


        fig, ax = plt.subplots(
            figsize=(5,5)
        )


        ax.pie(

            hotel_counts.values,

            labels=hotel_counts.index,

            autopct="%1.1f%%",

            startangle=90

        )


        ax.set_title(
            "Booking Contribution"
        )


        st.pyplot(fig)



    with col2:


        st.subheader(
            "📋 Booking Count"
        )


        st.dataframe(

            hotel_counts.rename(
                "Number of Bookings"
            ),

            use_container_width=True

        )



        city_percentage = (

            hotel_counts["City Hotel"]

            /

            hotel_counts.sum()

            *100

        )


        resort_percentage = (

            hotel_counts["Resort Hotel"]

            /

            hotel_counts.sum()

            *100

        )



        st.write(
        f"""
        🏙️ City Hotel:

        **{city_percentage:.1f}%** of total bookings


        🏖️ Resort Hotel:

        **{resort_percentage:.1f}%** of total bookings
        """
        )



    st.divider()



    # ==================================================
    # CANCELLATION RATE
    # ==================================================


    st.subheader(
        "❌ Cancellation Rate by Hotel Type"
    )



    cancel_rate = (

        df.groupby("hotel")

        ["is_canceled"]

        .mean()

        *100

    )



    fig, ax = plt.subplots(

        figsize=(8,4)

    )



    ax.bar(

        cancel_rate.index,

        cancel_rate.values

    )



    ax.set_title(
        "Cancellation Rate Comparison"
    )


    ax.set_xlabel(
        "Hotel Type"
    )


    ax.set_ylabel(
        "Cancellation Rate (%)"
    )



    for i, value in enumerate(cancel_rate.values):

        ax.text(

            i,

            value + 0.5,

            f"{value:.1f}%",

            ha="center"

        )



    st.pyplot(fig)



    st.divider()



    # ==================================================
    # INSIGHTS
    # ==================================================


    st.subheader(
        "💡 Business Insights"
    )


    st.write(
    """
    • City Hotels generate higher booking volume.


    • City Hotels show higher cancellation behaviour.


    • Resort Hotels can focus on seasonal packages.


    • Deposit policies can help reduce cancellations.
    """
    )
# ======================================================
# MONTHLY BOOKING ANALYSIS
# ======================================================


elif page == "Monthly Booking Analysis":


    st.header(
        "📅 Monthly Booking Analysis"
    )


    st.write(
    """
    This analysis shows monthly booking trends
    for City Hotel and Resort Hotel.
    """
    )


    st.divider()



    month_order = [

        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"

    ]



    monthly_bookings = (

        df.groupby(
            ["arrival_date_month", "hotel"]
        )
        .size()
        .reset_index(
            name="Bookings"
        )

    )



    monthly_bookings["arrival_date_month"] = pd.Categorical(

        monthly_bookings["arrival_date_month"],

        categories=month_order,

        ordered=True

    )



    monthly_bookings = (

        monthly_bookings

        .sort_values(
            "arrival_date_month"
        )

    )



    fig, ax = plt.subplots(

        figsize=(12,5)

    )



    sns.lineplot(

        data=monthly_bookings,

        x="arrival_date_month",

        y="Bookings",

        hue="hotel",

        marker="o",

        ax=ax

    )



    ax.set_title(
        "Monthly Booking Trend by Hotel Type"
    )


    ax.set_xlabel(
        "Month"
    )


    ax.set_ylabel(
        "Number of Bookings"
    )


    plt.xticks(
        rotation=45
    )



    st.pyplot(fig)



    st.divider()



    st.subheader(
        "💡 Seasonal Insights"
    )


    st.write(
    """
    • Peak travel months generate higher booking demand.


    • City Hotels maintain higher booking volume.


    • Seasonal pricing strategies can improve revenue.


    • Off-season offers can improve occupancy.
    """
    )





# ======================================================
# CANCELLATION ANALYSIS
# ======================================================


elif page == "Cancellation Analysis":


    st.header(
        "❌ Cancellation Analysis"
    )


    st.write(
    """
    This section analyzes cancellation behaviour
    and identifies revenue risk factors.
    """
    )


    st.divider()



    st.subheader(
        "Cancellation Rate by Hotel Type"
    )



    cancel_rate = (

        df.groupby("hotel")

        ["is_canceled"]

        .mean()

        *100

    )



    fig, ax = plt.subplots(

        figsize=(8,4)

    )



    ax.bar(

        cancel_rate.index,

        cancel_rate.values

    )



    ax.set_title(
        "Cancellation Rate Comparison"
    )


    ax.set_xlabel(
        "Hotel Type"
    )


    ax.set_ylabel(
        "Cancellation Rate (%)"
    )



    for i, value in enumerate(cancel_rate.values):

        ax.text(

            i,

            value + 0.5,

            f"{value:.1f}%",

            ha="center"

        )



    st.pyplot(fig)



    st.divider()



    st.subheader(
        "📌 Cancellation Insights"
    )


    st.write(
    """
    • City Hotels show higher cancellation behaviour.


    • Longer lead time increases cancellation risk.


    • Reminder notifications can improve booking confirmation.


    • Deposit policies can reduce revenue loss.
    """
    )
# ======================================================
# STAY DURATION ANALYSIS
# ======================================================


elif page == "Stay Duration Analysis":


    st.header(
        "🛏️ Stay Duration Analysis"
    )


    st.write(
    """
    This analysis explains how stay duration
    impacts cancellation behaviour.
    """
    )


    st.divider()



    stay_cancel = (

        df.groupby(
            ["hotel", "total_stay"]
        )
        ["is_canceled"]
        .mean()
        .reset_index()

    )



    stay_cancel["Cancellation Rate"] = (

        stay_cancel["is_canceled"] * 100

    )



    fig, ax = plt.subplots(

        figsize=(12,5)

    )



    sns.lineplot(

        data=stay_cancel,

        x="total_stay",

        y="Cancellation Rate",

        hue="hotel",

        marker="o",

        ax=ax

    )



    ax.set_title(
        "Cancellation Rate by Stay Duration"
    )


    ax.set_xlabel(
        "Total Stay (Nights)"
    )


    ax.set_ylabel(
        "Cancellation Rate (%)"
    )



    st.pyplot(fig)



    st.divider()



    st.subheader(
        "💡 Stay Duration Insights"
    )


    st.write(
    """
    • Stay duration influences cancellation behaviour.


    • Longer stays require better customer commitment.


    • Hotels can introduce attractive long-stay packages.


    • Non-refundable offers can reduce cancellation risk.
    """
    )





# ======================================================
# LEAD TIME ANALYSIS
# ======================================================


elif page == "Lead Time Analysis":


    st.header(
        "⏳ Lead Time Analysis"
    )


    st.write(
    """
    This analysis studies the relationship between
    advance booking period and cancellation risk.
    """
    )


    st.divider()



    lead_cancel = (

        df.groupby(
            ["hotel", "lead_time"]
        )
        ["is_canceled"]
        .mean()
        .reset_index()

    )



    lead_cancel["Cancellation Rate"] = (

        lead_cancel["is_canceled"] * 100

    )



    fig, ax = plt.subplots(

        figsize=(12,5)

    )



    sns.lineplot(

        data=lead_cancel,

        x="lead_time",

        y="Cancellation Rate",

        hue="hotel",

        ax=ax

    )



    ax.set_title(
        "Cancellation Rate by Lead Time"
    )


    ax.set_xlabel(
        "Lead Time (Days)"
    )


    ax.set_ylabel(
        "Cancellation Rate (%)"
    )



    st.pyplot(fig)



    st.divider()



    st.subheader(
        "💡 Lead Time Insights"
    )


    st.write(
    """
    • Longer advance bookings show higher cancellation risk.


    • Reminder messages can improve booking confirmation.


    • Partial deposit policies can reduce cancellations.


    • Better booking management improves revenue stability.
    """
    )





