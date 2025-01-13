import streamlit as st
import pandas as pd

# Load the database.csv file
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('database.csv')
        return data
    except FileNotFoundError:
        st.error("The file 'database.csv' was not found in the main directory.")
        return None

# Function to append a new row to the database
def add_row_to_database(new_row):
    try:
        data = pd.read_csv('database.csv')
        data = data.append(new_row, ignore_index=True)
        data.to_csv('database.csv', index=False)
        st.success("New row added successfully!")
    except FileNotFoundError:
        st.error("The file 'database.csv' was not found. Ensure it exists in the main directory.")
    except Exception as e:
        st.error(f"An error occurred while adding the row: {e}")

# Streamlit interface for adding new rows
def add_new_row():
    st.title("Add New Row to Database")

    # Load data to show column names
    data = load_data()

    if data is not None:
        st.subheader("Database Columns")
        st.write(data.columns.tolist())

        # Dynamically create input fields for each column
        new_row = {}
        for column in data.columns:
            new_row[column] = st.text_input(f"Enter value for {column}:")

        # Button to save new row
        if st.button("Add Row"):
            add_row_to_database(new_row)
    else:
        st.warning("No data to display. Ensure 'database.csv' exists in the main directory.")
