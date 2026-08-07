# 🏨 Investigating Hotel Business Using Data Visualization

## 📌 Project Overview

This project analyzes hotel booking data to understand customer booking behaviour, cancellation patterns, seasonal demand, stay duration, and lead-time behaviour.

The project uses **Python, Pandas, Matplotlib, Seaborn, and Streamlit** to perform data analysis and present business insights through an interactive dashboard.

## 🎯 Business Objective

The objective of this project is to help hotels:

* Understand booking patterns
* Identify cancellation behaviour
* Analyze seasonal booking trends
* Understand the impact of stay duration
* Analyze lead time and cancellation risk
* Improve occupancy
* Reduce cancellation losses
* Support data-driven pricing and booking decisions

## ❓ Business Questions

This analysis answers questions such as:

1. Which hotel type receives more bookings?
2. What is the cancellation rate by hotel type?
3. How does booking demand change by month?
4. Does stay duration affect cancellation behaviour?
5. Does longer lead time increase cancellation risk?
6. What business strategies can help reduce cancellations?

## 📊 Dataset

The project uses a hotel booking dataset containing information about hotel reservations, including:

* Hotel type
* Booking cancellation status
* Lead time
* Arrival month
* Weekend stay nights
* Weekday stay nights
* Average Daily Rate (ADR)
* Guest information
* Booking-related attributes

## 🧹 Data Cleaning

The following data preparation steps were performed:

* Handled missing values
* Removed duplicate records
* Created a `total_stay` feature
* Prepared data for business analysis
* Grouped booking data for trend analysis
* Calculated cancellation rates

## 🔧 Feature Engineering

A new feature was created:

### Total Stay

```python
df["total_stay"] = (
    df["stays_in_weekend_nights"]
    + df["stays_in_weekdays_nights"]
)
```

This feature helps analyze the relationship between stay duration and cancellation behaviour.

## 📈 Key Analysis

### 1. Hotel Type Analysis

The project compares:

* City Hotel
* Resort Hotel

Booking volume and cancellation rates are analyzed for both hotel types.

### 2. Monthly Booking Analysis

Monthly booking trends are analyzed to identify seasonal demand patterns and differences between hotel types.

### 3. Cancellation Analysis

Cancellation rates are compared across hotel types to identify potential revenue risks.

### 4. Stay Duration Analysis

The relationship between total stay duration and cancellation behaviour is analyzed.

### 5. Lead Time Analysis

The project examines whether advance bookings are associated with increased cancellation risk.

## 💡 Business Insights

The analysis provides insights such as:

* City Hotels account for a larger share of bookings.
* Hotel types show different cancellation behaviour.
* Booking demand varies across months.
* Longer lead times can be associated with higher cancellation risk.
* Stay duration can influence cancellation behaviour.

## 💼 Business Recommendations

Based on the analysis, hotels can consider:

* Using seasonal pricing strategies
* Offering attractive off-season packages
* Using partial deposits for advance bookings
* Sending booking confirmation reminders
* Offering suitable non-refundable plans
* Designing long-stay packages

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Streamlit**

## 📂 Project Structure

```text
hotel-booking-business-analysis/
│
├── app.py
├── hotel_bookings_data.csv
├── requirements.txt
└── README.md
```

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/rachapallirajeswari12/hotel-booking-business-analysis.git
```

### 2. Navigate to the project folder

```bash
cd hotel-booking-business-analysis
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🚀 Deployment

The Streamlit application can be deployed using **Streamlit Community Cloud**.

Deployment configuration:

```text
Repository: rachapallirajeswari12/hotel-booking-business-analysis
Branch: main
Main file: app.py
```

## 👩‍💻 Author

**Rachapalli Rajeswari**

### Skills Demonstrated

Python | Pandas | Data Visualization | Business Analysis | Streamlit

---

⭐ This project demonstrates how hotel booking data can be transformed into meaningful business insights using data analysis and visualization.
