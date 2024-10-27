import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv('sales_data_past_2_years.csv')
    return df

df = load_data()

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Feature engineering: Extracting month, year, and day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['Day'] = df['Date'].dt.day

# Select features and target variable
X = df[['Month', 'Year']]
y = df['Daily Total Sales (USD)']

# Divide the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the SVR model
@st.cache_data
def train_model():
    model = SVR(kernel='linear')
    model.fit(X_train, y_train)
    return model

model = train_model()

# Create the Streamlit app
st.title('Sales Prediction')

# User input to select year range
year_selected = st.slider('Select Year Range:', min_value=2020, max_value=2026, value=(2022, 2023))

# User input to select months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_selected = st.multiselect('Select Months:', months)

# Convert month names to numbers
month_selected_num = [months.index(month) + 1 for month in month_selected]

# Initialize day selection
day_selected = []

# User input to select days based on the selected months and years
if month_selected_num:
    days_available = sorted(df[(df['Month'].isin(month_selected_num)) & 
                               (df['Year'] >= year_selected[0]) & 
                               (df['Year'] <= year_selected[1])]['Day'].unique())
    day_selected = st.multiselect('Select Days:', days_available)

# Get selected dates based on the chosen years, months, and days
selected_dates = []
if day_selected and month_selected_num:
    for year in range(year_selected[0], year_selected[1] + 1):
        for month in month_selected_num:
            for day in day_selected:
                try:
                    selected_dates.append(datetime(year, month, day))
                except ValueError:
                    st.warning(f"Invalid date: {year}-{month}-{day}")

# Predict sales for the selected dates
predicted_sales = []
for date in selected_dates:
    features = [[date.month, date.year]]
    sales = model.predict(features)[0]
    predicted_sales.append((date, sales))

# Display predicted sales
for date, sales in predicted_sales:
    st.write(f"Predicted sales for {date.strftime('%d %B %Y')}: ${sales:.2f}")

# Filter the actual sales data for the selected dates
df_filtered = df[df['Date'].isin(selected_dates)]

# Plot the graph with actual and predicted sales
fig, ax = plt.subplots(figsize=(12, 8))

# Plot actual sales as blue points
ax.plot(df_filtered['Date'], df_filtered['Daily Total Sales (USD)'], 'bo-', 
        label='Actual Sales', markersize=8)

# Mark predicted sales with larger red crosses
for date, sales in predicted_sales:
    ax.scatter(date, sales, color='red', marker='x', s=200, 
               label=f'Predicted: ${sales:.2f}', linewidths=3)

# Set title and labels with bold fonts
ax.set_title('Actual Sales vs Predicted Sales', fontsize=18, fontweight='bold')
ax.set_xlabel('Date', fontsize=14, fontweight='bold')
ax.set_ylabel('Sales (USD)', fontsize=14, fontweight='bold')

# Customize x-axis date format
ax.xaxis.set_major_formatter(DateFormatter('%d-%b'))

# Display legend with larger font
ax.legend(fontsize=12)

# Add grid with better styling
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot in Streamlit app
st.pyplot(fig)

# If no days are selected, display a message
if not day_selected:
    st.write("Please select days to predict sales.")
