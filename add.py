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
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
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
        st.subheader("Add New Entry")
        
        # Create a dictionary with columns as keys and empty values for new row
        new_row = {col: "" for col in data.columns}
        editable_row = pd.DataFrame([new_row])  # Create a DataFrame for editing

        # Use the st.data_editor component for easier data entry
        edited_row = st.data_editor(
            editable_row,
            num_rows="fixed",
            use_container_width=True,
            key="data_entry_editor",
        )

        # Button to save the new row
        if st.button("Save Row", key="save_row_button"):
            # Convert edited_row to a dictionary and add it to the database
            add_row_to_database(edited_row.iloc[0].to_dict())
    else:
        st.warning("No data to display. Ensure 'database.csv' exists in the main directory.")
