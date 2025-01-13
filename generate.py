import streamlit as st
import pandas as pd
import plotly.express as px

# Load the database.csv file
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('database.csv')
        return data
    except FileNotFoundError:
        st.error("The file 'database.csv' was not found in the main directory.")
        return None

# Function to visualize data
def visualize_data():
    st.title("Generate Graphs")

    # Load data
    data = load_data()

    if data is not None:
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
