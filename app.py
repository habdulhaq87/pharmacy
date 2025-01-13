import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page configuration
st.set_page_config(page_title="Database App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])

# Load the database.csv file
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('database.csv')
        return data
    except FileNotFoundError:
        st.error("The file 'database.csv' was not found in the main directory.")
        return None

# Home Page
if page == "Home":
    st.title("Database Visualization")

    # Load data
    data = load_data()

    if data is not None:
        # Display raw data with an expander
        st.subheader("Raw Data")
        with st.expander("Click to view the raw data"):
            st.dataframe(data)

        # Display basic statistics
        st.subheader("Data Summary")
        st.write(data.describe())

        # Select columns for visualization
        st.subheader("Visualize Data")
        columns = data.columns.tolist()

        if columns:
            x_axis = st.selectbox("Choose the X-axis:", options=columns)
            y_axis = st.selectbox("Choose the Y-axis:", options=columns)
            chart_type = st.radio(
                "Select Chart Type:",
                options=["Scatter", "Line", "Bar"]
            )

            if st.button("Generate Chart"):
                # Create and display the chart
                if chart_type == "Scatter":
                    fig = px.scatter(data, x=x_axis, y=y_axis, title=f"{chart_type} Chart")
                elif chart_type == "Line":
                    fig = px.line(data, x=x_axis, y=y_axis, title=f"{chart_type} Chart")
                elif chart_type == "Bar":
                    fig = px.bar(data, x=x_axis, y=y_axis, title=f"{chart_type} Chart")

                st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("The dataset has no columns to visualize.")

    else:
        st.warning("No data to display. Ensure 'database.csv' is in the main directory.")

# About Page
elif page == "About":
    st.title("About This App")
    st.write("""
        This application is designed to visualize data from a file named `database.csv` located in the main directory. 
        It provides the following features:

        - **Raw Data View**: Explore the dataset in a tabular format.
        - **Data Summary**: View basic statistical summaries of the dataset.
        - **Interactive Charts**: Create scatter, line, or bar charts by selecting columns for the X and Y axes.

        ### How to Use:
        1. Place the `database.csv` file in the same directory as this application.
        2. Navigate to the **Home** page to interact with the data.
        3. Use the sidebar to switch between pages.

        For best results, ensure that the `database.csv` file is properly formatted with clear column headers.
    """)
